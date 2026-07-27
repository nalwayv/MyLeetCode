/**
 * Return the max product value if (nums[i]-1) * (nums[j]-1) from nums.
 * @param nums array of positive numbers.
 * @returns max product of (nums[i]-1) * (nums[j]-1).
 */
function maxProduct(nums: number[]): number {
  // keep track of the two largest numbers in nums.
  let num1: number = -1;
  let num2: number = -1;

  nums.forEach((num) => {
    if (num > num1) {
      num2 = num1;
      num1 = num;
    } else if (num > num2) {
      num2 = num;
    }
  });

  return (num1 - 1) * (num2 - 1);
}


function main(): void {
  console.log("1464. Maximum Product of Two Elements in an Array");

  let nums: number[] = [3, 4, 5, 2];
  let result: string = maxProduct(nums) === 12 ? "Pass" : "Fail";
  console.log(`Result for [3,4,5,2] should equal 12? ${result}`);
}

main();
