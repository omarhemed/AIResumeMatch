import React, { useState } from "react";

function UploadForm() {
  const [file, setFile] = useState(null); // State to store the selected file
  const [jobDescription, setJobDescription] = useState(""); // State for job description
  const [message, setMessage] = useState(""); // State to display upload messages

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
    formData.append("job_description", jobDescription); // Add job description to the form data

    try {
      const response = await fetch("http://127.0.0.1:5000/upload-resume", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("File upload failed.");
      }

      const data = await response.json();
      setMessage(`Upload successful: ${data.message}`);
      console.log(data); // Log the response to the console
    } catch (error) {
      console.error("Error uploading file:", error);
      setMessage("Error uploading file. Please try again.");
    }
  };

  return (
    <div>
      <h2>Upload Resume and Job Description Below!</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Resume:
            <input type="file" onChange={handleFileChange} />
          </label>
        </div>
        <div>
          <label>
            Job Description:
            <textarea
              placeholder="Paste job description here..."
              value={jobDescription}
              onChange={handleDescriptionChange}
            />
          </label>
        </div>
        <button type="submit">Upload</button>
      </form>
      {message && <p>{message}</p>} {/* Display upload messages */}
    </div>
  );
}

export default UploadForm;
