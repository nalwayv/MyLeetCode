/**
 * Return the product of n's digits.
 * @param n positive number
 * @returns product sum
 */
function getProductOf(n: number): number {
  let result: number = 1;
  while (n > 0) {
    result *= (n % 10);
    n = Math.floor(n / 10);
  }
  return result;
}

/**
 * Return the smallest number greater then or equal to n shuch that the product of n's digits is divisible by t.
 * @param n positive number
 * @param t positive number
 * @returns smallest number greater then or equal to n were the product of its digits is divisible by t.
 */
function smallestNumber(n: number, t: number): number {
  while (getProductOf(n) % t !== 0) {
    n++;
  }
  return n;
}

function testCase(n: number, t: number, expected: number): void {
  let testResult: string = smallestNumber(n, t) === expected ? "Pass" : "Fail";
  console.log(`Smallest Divisible Digit Product of (${n}, ${t}) should equal ${expected} ?  ${testResult}`);
}

function main(): void {
  console.log("3345. Smallest Divisible Digit Product I");

  testCase(10, 2, 10);
  testCase(15, 3, 16);
}

main();
