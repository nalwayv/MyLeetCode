/**
 * Return the minimum number of pushes needed to type word on a phone keypad after remapping the keys.
 * @param word word comprised of lowercase English letters.
 * @returns minimum number of pushes.
 */
function minimumPushes(word: string): number {
  let frequency: number[] = Array(26).fill(0);
  for (let ch of word) {
    frequency[ch.charCodeAt(0) - 97]++;
  }

  // sort in descending order
  frequency.sort((a, b) => b - a);

  const target: number = 8;

  let result: number = 0;
  let count: number = 0;
  let value: number = 1;

  for (let i = 0; i < 26; i++) {
    result += (frequency[i] * value);
    count++;

    if (count === target) {
      count = 0;
      value++;
    }
  }

  return result;
}


function main(): void {
  console.log("3016. Minimum Number of Pushes to Type Word II");

  let word: string = "aabbccddeeffgghhiiiiii";
  let result = minimumPushes(word) === 24 ? "Pass" : "Fail";
  console.log(`${word} should equal 24 ? ${result}`);
}

main();
