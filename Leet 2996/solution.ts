/**
 * Given an array of intergers return the smallest integer x missing from nums such that
 * x is greater than or equal to the sum of the largest sequential preset.
 * @param nums array of positive integers that can contain duplicates
 * @returns smallest missing integer greater than or equal to the sum of the largest sequential prefix
 */
function missingInteger(nums: number[]): number {
  // starting from 0 get largest sequential prefix sum
  let i: number = 1;
  let pre: number = nums[0];
  while (i < nums.length && nums[i] - nums[i - 1] === 1) {
    pre += nums[i];
    i++;
  }

  // increase pre until it is not present in nums
  const present: Set<number> = new Set(nums);
  while (present.has(pre)) {
    pre++;
  }

  return pre;
}

function testCase(nums: number[], expected: number): void {
  const result: string = missingInteger(nums) === expected ? "Pass" : "Fail";
  console.log(`Test case should equal expected: ${result}`);
}

function main(): void {
  console.log("2996. Smallest Missing Integer Greater Than Sequential Prefix Sum");

  let nums1: number[] = [1, 2, 3, 2, 5];
  testCase(nums1, 6);

  let nums2: number[] = [3, 4, 5, 1, 12, 14, 13];
  testCase(nums2, 15);
}

main();
