from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Define a folder to save uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't exist
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Endpoint 1: Upload Resume
@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save the file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    return jsonify({"message": "File uploaded successfully", "file_path": filepath})


# Endpoint 2: Submit Job Description
@app.route("/submit-job-description", methods=["POST"])
def submit_job_description():
    data = request.json
    if "job_description" not in data:
        return jsonify({"error": "No job description provided"}), 400

    job_description = data["job_description"]
    return jsonify({"message": "Job description received", "job_description": job_description})


# Endpoint 3: Analyze Resume and Job Description
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")

    if not resume_text or not job_description:
        return jsonify({"error": "Both resume text and job description are required"}), 400

    # Here, you would call your AI model to analyze and return a score and suggestions.
    # For now, return a placeholder response:
    score = 85  # Example score
    suggestions = ["Add more relevant keywords", "Improve formatting"]

    return jsonify({
        "score": score,
        "suggestions": suggestions
    })


if __name__ == "__main__":
    app.run(debug=True)
