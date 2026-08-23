/**
 * Given a string num of even length consisting of digits and '?',
 * return true if the player can win this game if played optimally.
 *
 * The game works by filling in the ? spliting the result in half and compairing the sums of left and right
 * and making sure they are not equal.
 *
 * @param num
 * @returns can player win this game if played optimally.
 */
function sumGame(num: string): boolean {
  let q1: number = 0;
  let q2: number = 0;
  let left: number = 0;
  let right: number = 0;

  for (let i = 0; i < Math.floor(num.length / 2); i++) {
    if (num[i] === "?") {
      q1++;
    } else {
      left += Number(num[i]);
    }

    if (num[num.length - 1 - i] === "?") {
      q2++;
    } else {
      right += Number(num[num.length - 1 - i]);
    }
  }

  let winCase1: boolean = (q1 + q2) % 2 == 1;
  let winCase2: boolean = left - right != Math.floor(((q2 - q1) * 9) / 2);

  return winCase1 || winCase2;
}

function testCase(num: string, expected: boolean): void {
  let result: boolean = sumGame(num);
  console.log(`Test case: ${num} -> ${result} (expected: ${expected})`);
}

function main(): void {
  console.log("1927. Sum Game");

  testCase("25??", true);
}

main();
