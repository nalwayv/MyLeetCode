/**
 * Given two strings s and t, return the number of distinct subsequences of s which equals t.
 * @param s
 * @param t
 * @returns number of distinct subsequences
 */
function numDistinct(s: string, t: string): number {
  let sLen = s.length;
  let tLen = t.length;

  const dp: number[][] = Array.from({ length: tLen + 1 }, () => Array(sLen + 1).fill(0));

  for (let i = 0; i <= sLen; i++) {
    dp[0][i] = 1;
  }

  for (let i = 1; i <= tLen; i++) {
    for (let j = 1; j <= sLen; j++) {

      let topLeft = (s[j - 1] === t[i - 1]) ? dp[i - 1][j - 1] : 0;
      let left = dp[i][j - 1];

      dp[i][j] = left + topLeft;
    }
  }

  return dp[tLen][sLen];
}


function main(): void {
  console.log("115. Distinct Subsequences");

  console.log(numDistinct("rabbbit", "rabbit"));
}

main();
