/**
 * Return the maximum length of a substring that contains at most 2 occurrences of each character.
 * @param s String to check
 * @returns Length of maximum substring.
 */
function maximumLengthSubstring(s: string): number {
  const fr = new Map<string, number>();

  let maxLen: number = 0;
  let left: number = 0;

  for (let right: number = 0; right < s.length; right++) {

    fr.set(s[right], (fr.get(s[right]) ?? 0) + 1);

    while (fr.get(s[right])! > 2) {
      fr.set(s[left], fr.get(s[left])! - 1);
      left++;
    }

    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}

function testCase(s: string, expected: number): void {
  const result: string =
    maximumLengthSubstring(s) === expected ? "Pass" : "Fail";
  console.log(`Test case should equal expected ${expected} ? ${result}`);
}

function main(): void {
  console.log("3090. Maximum Length Substring With Two Occurrences");

  testCase("bcbbbcba", 4);
  testCase("aaaa", 2);
}

main();
