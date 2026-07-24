/**
 * Return the most significant bit of n
 * @param {number} n 
 * @returns {number}
 */
function msb(n: number): number {
    let result: number = 0;
    while (1 < n) {
        n = (n >> 1);
        result++;
    }
    return result;
}


/**
 * Return the number of unique XOR triplet values from nums
 * @param {number[]} nums 
 * @returns {number}
 */
function uniqueXorTriplets(nums: number[]): number {
    if (nums.length === 1) {
        return 1;
    }

    let max: number = nums.reduce((num1, num2) => Math.max(num1, num2));
    let bit: number = msb(max);
    let result: number = Math.pow(2, bit + 1) - 1;
    return nums.length <= 2 ? result - 1 : result + 1;
}


function main(): void {
    console.log("3513. Number of Unique XOR Triplets I")

    const nums: number[] = [3,1,2];
    let result: number = uniqueXorTriplets(nums);
    console.log(`Result should equal 4? ${result}`);
}

main();