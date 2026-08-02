function minimax(
  nums: number[],
  left: number,
  right: number,
  player: boolean,
): number {
  if (left > right) {
    return 0;
  }

  if (player) {
    return Math.max(
      minimax(nums, left + 1, right, false) + nums[left],
      minimax(nums, left, right - 1, false) + nums[right],
    );
  }

  return Math.min(
    minimax(nums, left + 1, right, true) - nums[left],
    minimax(nums, left, right - 1, true) - nums[right],
  );
}

function predictTheWinner(nums: number[]): boolean {
  return minimax(nums, 0, nums.length - 1, true) >= 0;
}

function main(): void {
  console.log("486. Predict the Winner");

  let nums: number[] = [1, 5, 233, 7];
  let result: string = predictTheWinner(nums) ? "Yes" : "No";
  console.log(`Can player win this game [${nums}] ? ${result}`);
}

main();
