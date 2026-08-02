function minimax(
  nums: number[],
  left: number,
  right: number,
  getMax: boolean,
  memo: Map<string, number>,
): number {
  if (left > right) {
    return 0;
  }

  const frame: string = `${left},${right},${getMax}`;

  const frameValue: number | undefined = memo.get(frame);
  if (frameValue !== undefined) {
    return frameValue;
  }

  let value: number = 0;
  if (getMax) {
    value = Math.max(
      minimax(nums, left + 1, right, false, memo) + nums[left],
      minimax(nums, left, right - 1, false, memo) + nums[right],
    );
  } else {
    value = Math.min(
      minimax(nums, left + 1, right, true, memo) - nums[left],
      minimax(nums, left, right - 1, true, memo) - nums[right],
    );
  }

  memo.set(frame, value);
  return value;
}

function stoneGame(piles: number[]): boolean {
  let memo = new Map<string, number>();
  return minimax(piles, 0, piles.length - 1, true, memo) >= 0;
}

function main(): void {
  console.log("877. Stone Game");

  let piles: number[] = [3, 5, 3, 4];
  let result: string = stoneGame(piles) ? "Yes" : "No";
  console.log(`Can player win this game ${piles} ? ${result}`);
}

main();
