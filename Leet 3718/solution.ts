/**
 * Given an array of positive integers and a positive integer k,
 * return the smallest positive multiple of k
 * that is missing from nums.
 *
 * @param nums array of positive integers
 * @param k positive integer
 * @returns smallest positive multiple of k that is missing from nums
 */
function missingMultiple(nums: number[], k: number): number {
  // Using set
  // let set = new Set<number>(nums);
  // let result: number = k;
  // while (set.has(result)) {
  //   result += k;
  // }
  // return result;

  // Using sorted
  let snums: number[] = nums.toSorted((a, b) => a - b);
  let result: number = -1;
  let current: number = k;

  for (let v of snums) {
    if (v < current) {
      continue;
    }

    if (v % k == 0) {
      if (v !== current) {
        result = result === -1 ? current : Math.min(result, current);
      }
      current += k;
    }
  }

  if (result === -1) {
    result = current;
  }

  return result;
}

function testCase(nums: number[], k: number, expected: number): void {
  let result: string = missingMultiple(nums, k) === expected ? "Pass" : "Fail";
  console.log(`Test case should equal ${expected}? ${result}`);
}

function main(): void {
  console.log("3718. Smallest Missing Multiple of K");

  testCase([8, 2, 3, 4, 6], 2, 10);
  testCase([1, 4, 7, 10, 15], 5, 5);
}

main();
