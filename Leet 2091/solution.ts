/**
 * Return the minimum number of deletions it would take to remove
 * both the minimum and maximum element from nums.
 * @param nums
 * @returns minimum number of deletions.
 */
function minimumDeletions(nums: number[]): number {
  // get indices of min and max
  let iMin = nums.indexOf(Math.min(...nums));
  let iMax = nums.indexOf(Math.max(...nums));

  // get left most and right most indices
  let left = Math.min(iMax, iMin);
  let right = Math.max(iMax, iMin);

  // is it best to delete from the front, back, or both?
  // - front
  // - back
  // - both
  return Math.min(
    Math.max(left, right) + 1,
    nums.length - Math.min(left, right),
    left + 1 + (nums.length - right)
  );
}

function testCase(nums: number[], expected: number): void {
  let result = minimumDeletions(nums) === expected ? "pass" : "fail";
  console.log(`Test case should equal expected: ${result}`);
}

function main(): void {
  console.log("2091. Removing Minimum and Maximum From Array");
  let nums = [2, 10, 7, 5, 4, 1, 8, 6]
  testCase(nums, 5);
}

main()
