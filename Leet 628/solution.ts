/**
 * Return the max product of three numbers
 * @param nums array of positive and nevative numbers
 * @returns max product of three numbers
 */
function maximumProduct(nums: number[]): number {
  let max1: number = Number.MIN_SAFE_INTEGER;
  let max2: number = Number.MIN_SAFE_INTEGER;
  let max3: number = Number.MIN_SAFE_INTEGER;

  let min1: number = Number.MAX_SAFE_INTEGER;
  let min2: number = Number.MAX_SAFE_INTEGER;

  // get top 3 positive numbers and top 2 negative numbers
  nums.forEach((num) => {
    if (num > max1) {
      max3 = max2;
      max2 = max1;
      max1 = num;
    } else if (num > max2) {
      max3 = max2;
      max2 = num;
    } else if (num > max3) {
      max3 = num;
    }

    if (num < min1) {
      min2 = min1;
      min1 = num;
    } else if (num < min2) {
      min2 = num;
    }
  });

  return Math.max(max1 * max2 * max3, max1 * min1 * min2);
};


function main(): void {
  console.log("628. Maximum Product of Three Numbers");

  let nums: number[] = [-1, -2, -3];
  let result: number = maximumProduct(nums);

  console.log(`Result: ${result}`);
}


main();
