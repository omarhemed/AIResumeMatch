# AI ResumeMatch

AI ResumeMatch is a web application designed to help job seekers determine if their resume is a good fit for a specific job description. It analyzes the relevance of a resume to a job description and provides feedback on missing skills, areas for improvement, and additional skills to emphasize. The tool uses GPT (Generative Pre-trained Transformer) to evaluate the resume’s content and match it with the requirements outlined in the job description.

## Motivation

While applying for jobs, I often found myself wondering if my resume was truly a good fit for the job description. I struggled to determine whether I was missing key skills or if my experience aligned with the employer’s expectations. This uncertainty led me to create **AI ResumeMatch**. The goal of this project is to provide users with valuable insights about their resume and job description alignment, helping them make better decisions when applying for jobs.

## Features

- **Resume and Job Description Analysis**: The tool analyzes a resume and compares it with the provided job description, rating the relevance on a scale of 0-100%.
- **Skill Gap Identification**: If the resume is missing essential skills, the tool will clearly list them in bullet points.
- **Concise Feedback**: Provides actionable feedback on how to improve the resume to better match the job description.
- **Real-time Updates**: Users can upload their resume and job description, and instantly receive analysis and feedback.

## Technologies Used

### **Frontend**

- **React**: The front-end of the web application is built using React. It allows for efficient and responsive UI updates and provides a dynamic user experience.
- **CSS**: Custom styles and responsive design were created using CSS, ensuring that the website is clean, attractive, and mobile-friendly.
- **fetch/axios**: Used to send HTTP requests to the backend to upload files and fetch analysis results.

### **Backend**

- **Flask**: A Python-based web framework was used to handle API requests and serve the backend logic. It processes the resume and job description, sends data to the OpenAI API for analysis, and returns the results to the frontend.
- **OpenAI GPT-3**: OpenAI’s GPT-3 API is utilized to evaluate the relevance of the resume against the job description, identify missing skills, and provide feedback on how to improve the resume.
- **python-docx, PyPDF2**: Libraries for extracting text from `.docx` and `.pdf` files. These are used to parse the resume files that users upload.
- **dotenv**: Used to securely load environment variables like the OpenAI API key.

### **Development Tools**

- **Git & GitHub**: Version control was managed using Git, and the code was pushed to GitHub for easy collaboration and version tracking.
- **Visual Studio Code**: Used as the primary Integrated Development Environment (IDE) for both frontend and backend development.
- **npm**: Used for managing dependencies in the React project and running the development server.

## Features and Improvements to Be Made

While this project currently provides resume analysis, it is still in progress and could be further improved. Some areas for future development include:

- **Improved Text Extraction**: The current resume text extraction works with `.pdf` and `.docx` files, but more formats like `.txt` and `.rtf` could be supported.
- **User Authentication**: Allow users to create accounts and save their past analyses or customize the analysis feedback.
- **Skill Recommendation System**: Use machine learning or data from job boards to suggest popular or trending skills that could be added to resumes.
- **Real-time Collaboration**: Allow users to share their resumes and job descriptions with others for collaborative review and feedback.
- 
## DEMO
https://drive.google.com/file/d/1wjwxQToo79W1Npgq6Ub2us-6J4mXc75C/view?usp=sharing

## How It Works

1. **Upload Your Resume and Job Description**:
   - Select a `.pdf` or `.docx` file for your resume and paste a job description into the provided fields.
   
2. **Submit for Analysis**:
   - The tool processes the resume and job description, sending them to the backend where the OpenAI GPT model analyzes the content.

3. **View the Results**:
   - The tool returns a percentage representing the relevance of the resume to the job description.
   - If the resume is missing any skills, they are listed as bullet points.
   - Suggestions for improvement and additional skills are provided in clear, concise feedback.

## Future Plans

I plan to continue enhancing this project by:

- **Adding more integrations** with other job boards or resume optimization tools.
- **Improving the AI feedback** to make it more detailed and personalized based on the user’s career field.
- **Making the application more intuitive** by refining the user interface and improving error handling.
- **Increasing the number of file formats supported** for resume uploads.

## Conclusion

This project started as a solution to a personal problem I faced while applying for jobs, and it has evolved into a tool that can help many others in the same situation. I believe that this tool can significantly reduce the uncertainty job seekers face when applying for positions, giving them valuable insights into how well their resume matches the job description.

Feel free to contribute, suggest new features, or provide feedback. I will continue to improve this tool and update it regularly to make it more useful and effective for job seekers everywhere.

---

## Installation

If you'd like to run the project locally, follow these steps:

### 1. Clone the repository to your desktop:

```
git clone https://github.com/your-username/ai-resumematch.git

```

### 2. Open the project in Visual Studio Code:
- Open Visual Studio Code and use `File -> Open Folder` to open the `ai-resumematch` folder.

### 3. Set up the backend:
- Navigate to the backend directory:

```
cd ai-resumematch/backend
```
Run:
```
python app.py
```

### 4. Set up the frontend:
- Navigate to the frontend directory:
```
cd ai-resumematch/frontend
```
Run:
```
npm install
```
```
npm start
```


### 5. Upload your resume and job description:
- Open your browser and go to 'http://localhost:3000' to access the app.
- Upload your resume and paste a job description.
- Hit RUN and watch the magic happen as the tool analyzes the relevance of your resume to the job description and provides valuable feedback!
