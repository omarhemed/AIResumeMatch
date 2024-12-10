import React, { useState } from "react";
import './UploadForm.css'; // Import CSS file for styling

function UploadForm() {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [message, setMessage] = useState("");
  const [analysis, setAnalysis] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleDescriptionChange = (event) => {
    setJobDescription(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      setMessage("Please select a file first.");
      return;
    }

    if (!jobDescription) {
      setMessage("Please provide a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    try {
      const response = await fetch("http://127.0.0.1:5000/upload-and-analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("File upload failed.");
      }

      const data = await response.json();
      setMessage(`Upload successful: ${data.message}`);
      console.log(data);

      const analysisData = data.analysis.split("\n").map((line, index) => {
        return <li key={index}>{line}</li>;
      });
      setAnalysis(analysisData);
    } catch (error) {
      console.error("Error uploading file:", error);
      setMessage("Error uploading file. Please try again.");
    }
  };

  return (
    <div className="upload-form-container">
      <h2>Upload Your Resume and Job Description</h2>
      <form onSubmit={handleSubmit} className="upload-form">
        <div className="file-input-container">
          <label htmlFor="resume">
            <strong>Resume:</strong>
            <input type="file" id="resume" onChange={handleFileChange} />
          </label>
        </div>
        <div className="description-input-container">
          <label htmlFor="jobDescription">
            <strong>Job Description:</strong>
            <textarea
              id="jobDescription"
              placeholder="Paste job description here..."
              value={jobDescription}
              onChange={handleDescriptionChange}
            />
          </label>
        </div>
        <button type="submit" className="submit-button">RUN!</button>
      </form>
      {message && <p className="message">{message}</p>}

      {analysis && (
        <div className="analysis-container">
          <h3>Analysis Result:</h3>
          <ul className="analysis-list">
            {analysis}
          </ul>
        </div>
      )}
    </div>
  );
}

export default UploadForm;
