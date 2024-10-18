export class Compressor {
    constructor(chunksX, chunksY) {
        this.chunksX = chunksX;
        this.chunksY = chunksY;
    }

    // Splitting the image into chunks
    _chunk(imageData, width, height) {
        const xChunkSize = Math.floor(width / this.chunksX);
        const yChunkSize = Math.floor(height / this.chunksY);
        const chunks = [];

        for (let i = 0; i < this.chunksX; i++) {
            for (let j = 0; j < this.chunksY; j++) {
                const chunkPixels = [];
                const left = i * xChunkSize;
                const top = j * yChunkSize;

                // Extracting pixel data for each chunk
                for (let x = left; x < left + xChunkSize; x++) {
                    for (let y = top; y < top + yChunkSize; y++) {
                        const index = (y * width + x) * 4; // 4 values per pixel (R, G, B, A)
                        chunkPixels.push({
                            r: imageData.data[index],
                            g: imageData.data[index + 1],
                            b: imageData.data[index + 2],
                        });
                    }
                }
                chunks.push(chunkPixels);
            }
        }

        return chunks;
    }

    // Calculating the average color of each chunk
    _calculateAverageColor(chunk) {
        let r = 0, g = 0, b = 0;

        for (let pixel of chunk) {
            r += pixel.r;
            g += pixel.g;
            b += pixel.b;
        }

        const pixelCount = chunk.length;
        return [r / pixelCount, g / pixelCount, b / pixelCount];
    }

    // Executing the chunking and averaging
    execute(imageData, width, height) {
        const chunks = this._chunk(imageData, width, height);
        const avgChunks = [];

        for (let chunk of chunks) {
            avgChunks.push(this._calculateAverageColor(chunk));
        }

        return avgChunks;
    }
}

// Load an image and process it
const img = new Image();
img.src = 'your_image.jpg'; // Path to the JPEG image

img.onload = function () {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = img.width;
    canvas.height = img.height;

    // Draw the image onto the canvas
    ctx.drawImage(img, 0, 0);

    // Get the image data (pixels)
    const imageData = ctx.getImageData(0, 0, img.width, img.height);

    // Initialize the compressor
    const compressor = new Compressor(4, 4); // 4x4 grid of chunks

    // Execute and get the average RGB for each chunk
    const avgChunks = compressor.execute(imageData, img.width, img.height);

    console.log(avgChunks); // Output the average color of each chunk
};