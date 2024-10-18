export class Differencer {
    constructor(oldArray, newArray) {
        this.old = oldArray;
        this.new = newArray;
    }

    execute() {
        if (this.old === null || this.new === null) {
            return [];
        }

        const lenOld = this.old.length;
        const lenNew = this.new.length;

        // Check if the arrays are of equal length
        if (lenOld !== lenNew) {
            console.error("Arrays must be of the same length.");
            return;
        }

        const diffArray = [];
        // Calculate differences element-wise
        for (let i = 0; i < lenOld; i++) {
            if (this.old[i].length !== this.new[i].length) {
                console.error("Subarrays must have the same length.");
                return;
            }
            if (this.old[i] !== this.new[i]) {
                const diff = this.new[i].map((newVal, j) => newVal - this.old[i][j]);
                diffArray.push(diff);
            }
        }

        const sumArray = [];
        // Round the sum of differences and convert to hexadecimal if non-zero
        for (const diff of diffArray) {
            const roundedDiff = Math.round(diff.reduce((acc, val) => acc + val, 0));
            if (roundedDiff !== 0) {
                const absRoundedDiff = Math.abs(roundedDiff);
                sumArray.push(absRoundedDiff.toString(16).padStart(4, '0'));
            }
        }

        return sumArray;
    }
}