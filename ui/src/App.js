import './App.css';
import destructionImage from './data/test.jpg'
import React, { useState } from 'react';

const getTextFromFile = async (filePath) => {
  return await fetch(`${process.env.PUBLIC_URL}/${filePath}`)
    .then(data => data.text());
}

function App() {
  return (
    <div className='code-image-container'>
      <div className='code-container'>
        Code
      </div>
      <div className='image-container'>
        <img className='image' src={destructionImage} alt='Replacement Text'/>
      </div>
    </div>
  );
}

export default App;
