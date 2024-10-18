import './DestructionView.css';
import CodeView from './CodeView';
import ImageView from './ImageView';
import React from 'react';

const DestructionView = () => {

  return (
    <div className='code-image-container'>
      <CodeView />
      <ImageView />
    </div>
  );
}

export default DestructionView;