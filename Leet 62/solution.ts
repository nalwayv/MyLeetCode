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


// function uniquePaths(m: number, n: number): number {
//   type Frame = {
//     x: number;
//     y: number;
//     processed: boolean;
//   }

//   let memo = Array.from({ length: m }, () => Array(n).fill(-1));

//   let stk: Frame[] = [{
//     x: m - 1,
//     y: n - 1,
//     processed: false
//   }];

//   while (stk.length > 0) {
//     const { x, y, processed } = stk.pop() as Frame;

//     if (x < 0 || y < 0) {
//       continue;
//     }

//     if (x === 0 && y === 0) {
//       memo[0][0] = 1;
//       continue;
//     }

//     if (memo[x][y] !== -1) {
//       continue;
//     }

//     if (processed) {
//       let up = x > 0 ? memo[x - 1][y] : 0;
//       let left = y > 0 ? memo[x][y - 1] : 0;
//       memo[x][y] = up + left;
//     } else {
//       stk.push({ x: x, y: y, processed: true });
//       stk.push({ x: x - 1, y: y, processed: false });
//       stk.push({ x: x, y: y - 1, processed: false });
//     }
//   }

//   return memo[m - 1][n - 1];
// }


function main(): void {
  console.log("62. Unique Paths")
  console.log(`Result for (3,7): ${uniquePaths(3, 7)}`);
  console.log(`Result for (3,7): ${foo(3, 7)}`);
}

main();
