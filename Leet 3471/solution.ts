function largestInteger(nums: number[], k: number): number {
  let frequency = new Map<number, number>();
  for (let num of nums) {
    frequency.set(num, 0);
  }

  for (let i = 0; i < nums.length - k + 1; i++) {
    let set = new Set(nums.slice(i, i + k));
    for (let num of set) {
      frequency.set(num, (frequency.get(num) || 0) + 1);
    }
  }

  let result: number = -1;
  for (let num of nums) {
    if ((frequency.get(num) ?? 0) === 1) {
      result = Math.max(result, num);
    }
  }

  return result;
}

function main(): void {
  console.log("3471. Find the Largest Almost Missing Integer");

  let result: string = largestInteger([3, 9, 2, 1, 7], 3) === 7 ? "Pass" : "Fail";
  console.log(`Result for [3,9,2,1,7] should equal 7 ? ${result}`);
}

main();
