/**
 * Return the length of the longest subarray with at most k frequency.
 * @param nums array or positive integers.
 * @param k max frequency of any element in the subarray.
 * @returns subarray length.
 */
function maxSubarrayLength(nums: number[], k: number): number {
  const fr = new Map<number, number>();
  for (const num of nums) {
    fr.set(num, 0);
  }

  let p1: number = 0;
  let maxLen: number = 0;
  for (let p2 = 0; p2 < nums.length; p2++) {
    fr.set(nums[p2], (fr.get(nums[p2]) ?? 0) + 1);

    while (p1 < p2 && (fr.get(nums[p2]) ?? 0) > k) {
      fr.set(nums[p1], (fr.get(nums[p1]) ?? 0) - 1);
      p1++;
    }

    maxLen = Math.max(maxLen, p2 - p1 + 1);
  }

  return maxLen;
}

function main(): void {
  console.log("2958. Length of Longest Subarray With at Most K Frequency");

  let nums: number[] = [1, 2, 3, 1, 2, 3, 1, 2];
  let result: string = maxSubarrayLength(nums, 2) === 6 ? "Pass" : "Fail";
  console.log(`Test case should pass ? ${result}`);
}

main();
