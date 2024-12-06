from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
import docx

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OpenAI API key is missing. Check your .env file.")

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't exist
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(filepath):
    """Extract text from a PDF or DOCX file"""
    ext = filepath.rsplit('.', 1)[1].lower()
    
    if ext == 'pdf':
        with open(filepath, 'rb') as file:
            reader = PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text

    elif ext == 'docx':
        doc = docx.Document(filepath)
        text = ''
        for para in doc.paragraphs:
            text += para.text + '\n'
        return text
    
    return None  # In case the file type is not supported

def analyze_resume_with_gpt(resume_text, job_description):
    prompt = f"""
    As a resume evaluator, analyze the following resume in relation to the given job description:
    
    Job Description:
    {job_description}
    
    Resume:
    {resume_text}
    
    Tasks:
    1. Rate the resume's relevance to the job description on a scale of 0-100%.
    2. Provide specific feedback on how the resume could be improved to better match the job description.
    3. Suggest additional skills or experiences the candidate should emphasize or acquire.
    4. Make sure to provide these results in short sentences and make them straight to the point.
    """
    try:
        # Updated API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional resume evaluator."},
                {"role": "user", "content": prompt}
            ]
        )
        # Accessing the output in the new API structure
        analysis = response["choices"][0]["message"]["content"].strip()
        return analysis
    except Exception as e:
        return f"Error while analyzing resume: {str(e)}"

@app.route("/upload-and-analyze", methods=["POST"])
def upload_and_analyze():
    if "file" not in request.files or "job_description" not in request.form:
        return jsonify({"error": "File and job description are required"}), 400

    file = request.files["file"]
    job_description = request.form["job_description"]

    if file.filename == "" or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type. Allowed types are: pdf, doc, docx"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename))
    file.save(filepath)

    # Extract text from the file
    resume_text = extract_text_from_file(filepath)
    if not resume_text:
        return jsonify({"error": "Failed to extract text from the uploaded file"}), 400

    # Now call the GPT model to analyze the resume
    analysis_result = analyze_resume_with_gpt(resume_text, job_description)

    return jsonify({"message": "File uploaded and analyzed successfully", "analysis": analysis_result})

# Testing script for GPT function
if __name__ == "__main__":
    # Test inputs
    resume_text = """
    Experienced software engineer with 5+ years of experience in Python, JavaScript, and cloud computing. 
    Proficient in backend systems, database management, and team collaboration.
    """
    job_description = """
    Seeking a software engineer with strong backend development skills, experience with cloud computing 
    platforms (AWS, Azure, or Google Cloud), and the ability to work in an agile environment.
    """

    # Call the GPT function for testing
    print("Testing GPT API connection...")
    result = analyze_resume_with_gpt(resume_text, job_description)
    print("\nGPT Analysis Result:")
    print(result)

    # Run Flask app
    app.run(host="0.0.0.0", port=5000)
