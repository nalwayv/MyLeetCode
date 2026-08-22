/**
 * Given a positive integer n, Determin whether n is divisible by the sum of the following two values
 * - The digit sum of n (the sum of its digits).
 * - The digit product of n (the product of its digits).
 * @param n positive integer
 * @returns if n is divisible by the sum of its digit sum and digit product
 */
function checkDivisibility(n: number): boolean {
  let value: number = n;
  let sum: number = 0;
  let product: number = 1;

  while (n > 0) {
    let digit: number = n % 10;

    sum += digit;
    product *= digit;

    n = Math.floor(n / 10);
  }

  return value % (sum + product) === 0;
}
