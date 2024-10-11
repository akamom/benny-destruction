import './App.css';
import destructionImage from './data/destroyme.jpg'
import React, { useState, useEffect } from 'react';

function App() {
  const [fileContent, setFileContent] = useState("");

  useEffect(() => {
    fetch("/myfile.txt")
      .then((response) => response.text())
      .then((text) => setFileContent(text))
      .catch((error) => console.error("Error fetching the file:", error));
  }, []);

  return (
    <div className='code-image-container'>
      <div className='code-container'>
        {fileContent}
      </div>
      <div className='image-container'>
        <img className='image' src={destructionImage} alt='Replacement Text'/>
      </div>
    </div>
  );
}

export default App;
