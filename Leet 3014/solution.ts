/**
 * After remapping a phone's keypad keys return the minimum number of pushes needed to type out word.
 * @param word
 * @returns minimum number of pushes.
 */
function minimumPushes(word: string): number {
  const target: number = 8;

  let value: number = 1;
  let count: number = 0;
  let result: number = 0;

  for (let i = 0; i < word.length; i++) {
    result += value;
    count++;

    if (count == target) {
      count = 0;
      value += 1;
    }
  }

  return result;
}

function main(): void {
  console.log("3014. Minimum Number of Pushes to Type Word I");

  let word: string = "xycdefghij";
  let result: string = minimumPushes(word) === 12 ? "Pass" : "Fail";

  console.log(`Result (${word}) should equal 12 ? ${result}`);
}

main();
