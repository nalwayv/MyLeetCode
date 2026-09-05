function firstStableIndex(nums: number[], k: number): number {
  if (nums.length === 0) {
    return -1;
  }

  const suffixMin: number[] = new Array(nums.length);
  suffixMin[nums.length - 1] = nums[nums.length - 1];

  for (let i = nums.length - 2; i >= 0; i--) {
    suffixMin[i] = Math.min(suffixMin[i + 1], nums[i]);
  }

  let prefixMan = nums[0];
  for (let i = 0; i < nums.length; i++) {
    prefixMan = Math.max(prefixMan, nums[i]);

    if (prefixMan - suffixMin[i] <= k) {
      return i;
    }
  }

  return -1;
}

function testCase(nums: number[], k: number, expected: number): void {
  let strNums = nums.join(", ");
  let actual = firstStableIndex(nums, k);
  let result = actual === expected ? "Pass" : "Fail";
  console.log(
    `${result} firstStableIndex([${strNums}], ${k}) -> expected ${expected} got ${actual}`,
  );
}

function main(): void {
  console.log("3904. Smallest Stable Index II");

  testCase([5, 0, 1, 4], 3, 3);
  testCase([1, 3, 2, 4, 0], 2, 0);
  testCase([], 2, -1);
}

main();
