/**
 * Check if Alice can win the stone game against Bob if both players play optimally.
 * On each turn a player can remove any non zero square number of stones from the pile.
 * @param n number of stones in the pile
 * @returns True if Alice can win the game.
 */
function winnerSquareGame(n: number): boolean {
  const dp: boolean[] = new Array(n + 1).fill(false);

  for (let i: number = 1; i <= n; i++) {
    let j: number = 1;

    // iterate through square numbers up to i and check if dp[i - j * j] is false
    // if it is, set dp[i] to true and break the loop
    while (j * j <= i) {
      if (!dp[i - j * j]) {
        dp[i] = true;
        break;
      }

      j++;
    }
  }

  return dp[n];
}

function testCase(n: number, expected: boolean): void {
  const result: boolean = winnerSquareGame(n)
  const testResult: string = result === expected ? "PASS" : "FAIL";
  console.log(`Test case ${n}: ${testResult}`);
}

function main(): void {
  console.log("1510. Stone Game IV");
  // testCase(1, true);
  // testCase(2, false);
  testCase(10, false);
}

main();
