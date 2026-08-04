function findMissingElements(nums: number[]): number[] {
  const snums: number[] = nums.toSorted((a, b) => a - b);
  const result: number[] = [];

  let start: number = snums[0];
  let end: number = snums[snums.length - 1];
  let j: number = 0;

  for (let i = start; i <= end; i++) {
    if (snums[j] !== i) {
      result.push(i);
    } else {
      j++;
    }
  }

  return result;
}

function arraysAreEqual(arr1: number[], arr2: number[]) {
  if (arr1.length !== arr2.length) {
    return false;
  }

  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }

  return true;
}

function testCase(nums: number[], expected: number[]): void {
  let missing: number[] = findMissingElements(nums);
  let result: string = arraysAreEqual(missing, expected) ? "Pass" : "Fail";

  console.log(`Result from findMissingElements(nums) should equal expected ? ${result}`);
}

function main(): void {
  console.log("3731. Find Missing Elements");

  const nums: number[] = [1, 3, 5, 6];
  const expected: number[] = [2, 4];
  testCase(nums, expected);
}

main();
