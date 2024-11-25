import './App.css';
import UploadForm from "./UploadForm";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* Removed the React logo */}
        <h1>AI ResumeMatch</h1> {/* Add a custom title */}
      </header>
      <main>
        <UploadForm />
      </main>
    </div>
  );
}

export default App;
