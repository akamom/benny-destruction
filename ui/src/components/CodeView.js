import './CodeView.css';
import React, { useState, useEffect } from 'react';
import { Compressor } from '../util/compress';
import { Differencer } from '../util/difference';
import destructionImage from '../data/destroyme.jpg'
import originalImage from '../data/original.jpg'
import { useScramble } from "use-scramble";

const CodeView = () => {
    const [original, setOriginal] = useState(null);
    const [code, setCode] = useState([]);

    const { ref } = useScramble({
        text: code.join(' '),
        speed: 0.10,
        tick: 10000.00,
        step: 50000,
        overflow: true,
        scramble: 2,
        overdrive: false
    });

    useEffect(() => {
        loadImage(originalImage)
            .then(image => {
                const canves = createCanvas(image);
                const compressedCanvas = compress(canves);
                setOriginal(compressedCanvas)
            })
    }, [])

    useEffect(() => {
        if (original === null) {
            return
        }

        const intervalId = setInterval(() => generateDifference(), 1000);
        return () => clearInterval(intervalId);
    }, [original])

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
            const compressor = new Compressor(40, 40);
            const avgChunks = compressor.execute(imageData, canves.width, canves.height);
            return avgChunks;
        }
    }

    function difference(destroy) {
        console.log(original)
        console.log(destroy)
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
            {/* {code.join('\t')} */}
            <p ref={ref} />
        </div>
    );
}

export default CodeView;