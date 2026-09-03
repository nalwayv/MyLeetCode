/**
 * Return true if it is possible to construct a uniform parity array from nums1.
 * @param nums1
 * @returns if a 
 */
function uniformArray(nums1: number[]): boolean {
    // array can ever be all even or all odd

    // get smallest of odd number
    let minOdd = -1;
    for(let num of nums1) {
        if (num % 2 === 1) {
            if (minOdd === -1 || num < minOdd) {
                minOdd = num;
            }
        }
    }

    // convert all even nums into odd 
    // Rules
    //  . even - odd = odd
    //  . nums[i] - nums[j] >= 1
    for(let num of nums1) {
        // if all nums are even then num - -1 becomes num + 1
        if (num % 2 === 0 && num - minOdd < 1) {
            return false;
        }
    }

    return true;
}

function testCase(nums1: number[], expected: boolean): void {
    let result = uniformArray(nums1) === expected ? "pass" : "fail";
    console.log(`uniformArray(nums1) should equal expected ? ${result}`);
}

function main(): void {
    console.log("3876. Construct Uniform Parity Array II");

    testCase([1,4,7], true);
    testCase([2,3], false);
}

main();