function stoneGameIX(stones: number[]): boolean {
  let remainders: number[] = [0, 0, 0];
  for (let s of stones) {
    remainders[s % 3]++;
  }

  if (remainders[0] % 2 == 0) {
    return remainders[1] > 0 && 0 < remainders[2];
  }

  return Math.abs(remainders[1] - remainders[2]) > 2;
}

function main(): void {
  console.log("2029. Stone Game IX");
  let result = stoneGameIX([5, 1, 2, 4, 3]) === false ? "Pass" : "Fail";
  console.log(`Test case for [5,1,2,4,3] should return false ? ${result}`);
}

main();
