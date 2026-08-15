function longestSubsequence(nums: number[]): number {
  let allZero: number = 0;
  let xsum: number = 0;

  for (let num of nums) {
    if (num === 0) {
      allZero++;
    }

    xsum ^= num;
  }

  if (allZero === nums.length) {
    return 0;
  }

  if (xsum === 0) {
    return nums.length - 1;
  }

  return nums.length;
}

function testCase(nums: number[], expected: number): void {
  let result: string = longestSubsequence(nums) === expected ? "Pass" : "Fail";
  console.log(`Test case should equal ${expected} ? ${result}`);
}

function main(): void {
  console.log("3702. Longest Subsequence With Non-Zero Bitwise XOR");

  testCase([1, 2, 3], 2);
  testCase([2, 3, 4], 3);
  testCase([0, 0, 0], 0);
}

main();
