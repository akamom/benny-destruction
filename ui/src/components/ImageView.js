import './ImageView.css';
import React, { useEffect, useState } from 'react';
import destructionImage from '../data/test.jpg'

const ImageView = () => {

    return (
        <div className='image-container'>
            <img className='image' src={destructionImage} alt='Replacement Text'/>
        </div>
    );
}

export default ImageView;