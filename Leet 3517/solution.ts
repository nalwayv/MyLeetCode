/**
 * Return the lexicographically smallest palindromic permutation of s
 * @param s A palindromic string
 * @returns Smallest palindromic permutation of s.
 */
function smallestPalindrome(s: string): string {
  let frequency = new Map<string, number>();
  for (let char of s) {
    frequency.set(char, (frequency.get(char) ?? 0) + 1);
  }

  let front: string = "";
  let middle: string = "";
  let end: string = "";

  let lowercase: string = "abcdefghijklmnopqrstuvwxyz";
  for (let char of lowercase) {
    if (!frequency.has(char)) {
      continue;
    }

    let count = frequency.get(char) ?? 0;
    if (count === 0) {
      continue;
    }

    front += char.repeat(count / 2);
    middle += char.repeat(count % 2);
    end = char.repeat(count / 2) + end;
  }

  return front + middle + end;
}

function main(): void {
  console.log("3517. Smallest Palindromic Rearrangement I");

  let result: string = smallestPalindrome("babab");
  console.log(`Result: ${result}`);
}

main();
