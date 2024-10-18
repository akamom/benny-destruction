import './CodeView.css';
import React, { useState, useEffect } from 'react';
import { Compressor } from '../util/compress';
import { Differencer } from '../util/difference';
import destructionImage from '../data/test.jpg'
import originalImage from '../data/frida.jpg'

const CodeView = () => {
    const [original, setOriginal] = useState(null);
    const [code, setCode] = useState([]);

    useEffect(() => {
        loadImage(originalImage)
            .then(image => {
                const canves = createCanvas(image);
                const compressedCanvas = compress(canves);
                setOriginal(compressedCanvas)
            })
        const intervalId = setInterval(() => generateDifference(), 1000);
        return () => clearInterval(intervalId);
    }, [])

    function generateDifference() {
        loadImage(destructionImage)
            .then(image => {
                const canves = createCanvas(image);
                const compressedCanvas = compress(canves);
                const newCode = difference(compressedCanvas);
                setCode(newCode);
            })
    }

    function compress(canves) {
        if (canves !== null) {
            const ctx = canves.getContext('2d');
            const imageData = ctx.getImageData(0, 0, canves.width, canves.height);
            const compressor = new Compressor(20, 20);
            const avgChunks = compressor.execute(imageData, canves.width, canves.height);
            return avgChunks;
        }
    }

    function difference(destroy) {
        const differencer = new Differencer(original, destroy);
        return differencer.execute();
    }

    function loadImage(path) {
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.src = path;
            img.onload = () => resolve(img);
            img.onerror = (err) => reject(err)
        });
    }

    function createCanvas(image) {
        const canvas = document.createElement('canvas');
        canvas.width = image.width;
        canvas.height = image.height;

        const ctx = canvas.getContext('2d');
        ctx.drawImage(image, 0, 0);
        return canvas;
    }

    return (
        <div className='code-container'>
            {code.join('\t')}
        </div>
    );
}

export default CodeView;