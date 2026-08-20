function resultArray(nums: number[]): number[] {
    let a: number[] = [nums[0]];
    let b: number[] = [nums[1]];

    for(let i = 2; i < nums.length; i++) {
        if (a[a.length - 1] > b[b.length - 1]) {
            a.push(nums[i]);
        } else {
            b.push(nums[i]);
        }
    }
    
    return a.concat(b);
}

function arraysEqual(a: number[], b: number[]): boolean {
    if (a.length !== b.length) {
        return false;
    }

    for(let i = 0; i < a.length; i++) {
        if(a[i] !== b[i]) {
            return false;
        }
    }

    return true;
}

function testCase(nums: number[], expected: number[]): void {
    let result: string = arraysEqual(resultArray(nums), expected) ? "Pass" : "Fail"
    console.log(`Test case should equal expected ? ${result}`);
}

function main(): void {
    console.log("3069. Distribute Elements Into Two Arrays I");

    let expected: number[] = [5,3,4,8];
    let nums: number[] = [5,4,3,8];
    
    testCase(nums, expected);
}

main();