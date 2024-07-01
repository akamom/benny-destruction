import './App.css';
import React, { useState } from 'react';

const getTextFromFile = async (filePath) => {
  return await fetch(`${process.env.PUBLIC_URL}/${filePath}`)
    .then(data => data.text());
}

function App() {
  const [text, setText] = useState("");

  const startTag = '<font color="green">';
  const endTag = '</font>'
  getTextFromFile('out')
    .then(res => 'Bonjour. <font color="green"> Was mache ich hier.</font> Ich heisse Hermann.')
    .then(res => res[10] = endTag)
    .then(res => setText(res));
  
  console.log(text[5]);

  return (
    <div className='wrapper'>
      <div className='infinit-scroll-text'>
        <span dangerouslySetInnerHTML={{ __html: text}}/>
      </div>
    </div>
  );
}

export default App;
