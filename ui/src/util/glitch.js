export class Glitch {
    constructor(glitchHeightFactor, widthBaseFactor, glitchWidthFactor, image) {
        this.canvas = image;
        this.context = this.canvas.getContext('2d');
        this.width = image.width;
        this.height = image.height;
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        
        // Draw image on the canvas
        this.context.drawImage(image, 0, 0, this.width, this.height);

        // Get pixel data from the image
        this.pixelData = this.context.getImageData(0, 0, this.width, this.height);
        this.shiftWidth = Math.floor(this.width * glitchWidthFactor);
        this.shiftHeight = Math.floor(this.height * glitchHeightFactor);
        this.baseWidth = Math.floor(this.width * widthBaseFactor);
    }

    _createShiftWidth() {
        const glitchWidth = [];

        for (let i = 0; i < this.shiftWidth; i++) {
            const currentWidth = this.baseWidth + i;
            if (currentWidth >= this.width) {
                break;
            }
            glitchWidth.push(currentWidth);
        }

        return glitchWidth;
    }

    randomize() {
        this.shiftWidth = Math.floor(this.width * (Math.random() * (0.1 - 0.002) + 0.002));
        this.shiftHeight = Math.floor(this.height * (Math.random() * (0.03 - 0.01) + 0.01));
        this.baseWidth = Math.floor(Math.random() * this.width);
    }

    execute() {
        const lastShiftedHeight = this.height - this.shiftHeight;
        const shiftWidthArray = this._createShiftWidth();
        const pixelData = this.pixelData.data; // Image pixel data as a 1D array [r, g, b, a, ...]

        for (let currentHeight = 0; currentHeight < this.height; currentHeight++) {
            for (const currentWidth of shiftWidthArray) {
                let glitchHeight, glitchWidth;

                if (currentHeight < lastShiftedHeight) {
                    glitchHeight = currentHeight + this.shiftHeight;
                    glitchWidth = currentWidth;
                } else {
                    glitchHeight = (currentHeight + this.shiftHeight) - this.height;
                    glitchWidth = currentWidth + this.shiftWidth + 1;
                }

                if (glitchWidth >= this.width) {
                    // Set pixel to black if glitchWidth exceeds canvas width
                    this._setPixel(currentWidth, currentHeight, [0, 0, 0, 255]);
                } else {
                    // Copy the pixel from the glitch position to the current position
                    const pixelValue = this._getPixel(glitchWidth, glitchHeight);
                    this._setPixel(currentWidth, currentHeight, pixelValue);
                }
            }
        }

        // Update canvas with the new pixel data
        this.context.putImageData(this.pixelData, 0, 0);

        return this.canvas;
    }

    _getPixel(x, y) {
        const index = (y * this.width + x) * 4; // 4 values per pixel (r, g, b, a)
        return [
            this.pixelData.data[index],     // Red
            this.pixelData.data[index + 1], // Green
            this.pixelData.data[index + 2], // Blue
            this.pixelData.data[index + 3]  // Alpha
        ];
    }

    _setPixel(x, y, color) {
        const index = (y * this.width + x) * 4;
        this.pixelData.data[index] = color[0];     // Red
        this.pixelData.data[index + 1] = color[1]; // Green
        this.pixelData.data[index + 2] = color[2]; // Blue
        this.pixelData.data[index + 3] = color[3]; // Alpha
    }

    // Returns the canvas element for further use
    getCanvas() {
        return this.canvas;
    }
}
