function firstStableIndex(nums: number[], k: number): number {
  // store current min at each index
  let mn = nums[nums.length - 1];
  const mnNums = new Array(nums.length);
  for (let i = 0; i < nums.length; i++) {
    mn = Math.min(mn, nums[nums.length - i - 1]);
    mnNums[nums.length - i - 1] = mn;
  }

  let mx = nums[0];
  for (let i = 0; i < nums.length; i++) {
    mx = Math.max(mx, nums[i]);
    if (mx - mnNums[i] <= k) {
      return i;
    }
  }

  return -1;
}

function testCase(nums: number[], k: number, expected: number): void {
  let result = firstStableIndex(nums, k) === expected ? "pass" : "fail";
  console.log(`Test case should equal expected: ${result}`);
}

function main(): void {
  console.log("3903. Smallest Stable Index I");

  testCase([5, 0, 1, 4], 3, 3);
  testCase([1, 3, 2, 4, 0], 2, 0);
}

main();
