import './ImageView.css';
import React from 'react';
import destructionImage from '../data/destroyme.jpg'

const ImageView = () => {

    return (
        <div className='image-container'>
            <img className='image' src={destructionImage} alt='Replacement Text'/>
        </div>
    );
}

export default ImageView;