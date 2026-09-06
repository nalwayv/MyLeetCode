/**
 * Given two strings s and t, return the number of distinct subsequences of s which equals t.
 * @param s
 * @param t
 * @returns number of distinct subsequences
 */
function numDistinct(s: string, t: string): number {
  let sLen = s.length;
  let tLen = t.length;

  const dp: number[][] = Array.from({ length: tLen + 1 },
    () => Array(sLen + 1).fill(0));

  for (let i = 0; i <= sLen; i++) {
    dp[0][i] = 1;
  }

  for (let i = 1; i <= tLen; i++) {
    for (let j = 1; j <= sLen; j++) {
      // - If s[j-1] == t[i-1]:
      //     dp[i][j] = dp[i][j-1] (left) + dp[i-1][j-1] (left-up)
      // - Else:
      //     dp[i][j] = dp[i][j-1] (left)
      let v1 = s[j - 1] !== t[i - 1] ? 0 : dp[i - 1][j - 1];
      let v2 = dp[i][j - 1];
      dp[i][j] = v1 + v2;
    }
  }

  return dp[tLen][sLen];
}


function main(): void {
  console.log("115. Distinct Subsequences");

  console.log(numDistinct("rabbbit", "rabbit"));
}

main();
