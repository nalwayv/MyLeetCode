function dp(i: number, j: number, memo: number[][]): number {
  if (i === 0 && j === 0) {
    return 1;
  }

  if (i < 0 || j < 0) {
    return 0;
  }

  if (memo[i][j] !== -1) {
    return memo[i][j];
  }

  let result = dp(i - 1, j, memo) + dp(i, j - 1, memo);
  memo[i][j] = result;

  return result;
}


/**
 * Return the count of all unique paths taken by only moving right or down
 * @param m grid rows
 * @param n grid columns
 * @returns count from starting at [0][0] and moving to [m-1][n-1]
 */
function uniquePaths(m: number, n: number): number {
  let memo: number[][] = Array.from({ length: m }, () => Array(n).fill(-1));
  return dp(m - 1, n - 1, memo);
}


function main(): void {
  console.log("62. Unique Paths")
  console.log(`Result for (3,2): ${uniquePaths(3, 2)}`);
}

main();
