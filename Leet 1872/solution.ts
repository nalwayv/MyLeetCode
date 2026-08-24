function stoneGameVIII(stones: number[]): number {
  let pre: number[] = new Array(stones.length + 1).fill(0);
  for (let i = 0; i < stones.length; i++) {
    pre[i + 1] = pre[i] + stones[i];
  }

  let mx: number = pre[pre.length - 1];
  for (let i = stones.length - 2; i > 0; i--) {
    mx = Math.max(mx, pre[i + 1] - mx);
  }

  return mx;
}

function main(): void {
  console.log("1872. Stone Game VIII");

  console.log(stoneGameVIII([-1, 2, -3, 4, -5]) === 5 ? "Pass" : "Fail");
  console.log(stoneGameVIII([7,-6,5,10,5,-2,-6]) === 13 ? "Pass" : "Fail");
  console.log(stoneGameVIII([-10,-12]) === -22 ? "Pass" : "Fail");
}

main();
