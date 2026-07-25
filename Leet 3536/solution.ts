/**
 * Return the max product of the two larges digits within n.
 * @param n positive number.
 * @returns max product of the two largest digits.
 */
function maxProduct(n: number): number {
  let mx1: number = Number.MIN_SAFE_INTEGER;
  let mx2: number = Number.MIN_SAFE_INTEGER;

  while( n > 0) {

    let current: number = n % 10;

    if (current > mx1) {
      mx2 = mx1;
      mx1 = current;
    } else if (current > mx2) {
      mx2 = current;
    }

    n = Math.floor(n / 10);
  }

  return mx1 * mx2;
}


function main(): void {
  console.log("3536. Maximum Product of Two Digits");

  let result: number = maxProduct(31);
  console.log(`Result 31 should equal 3? ${result === 3 ? "Pass" : "Fail"}`);
}


main();
