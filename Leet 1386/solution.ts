/**
 * Check whether one or two four-person groups can be seated together
 * in a row of 10 seats, using one (or both) of these seat blocks:
 *
 * - [2,3,4,5]
 * - [4,5,6,7]
 * - [6,7,8,9]
 * @param reservedMask a bit mask representing a row of seats from 1 to 10 that are reserved
 * - 00000001110 shows seats [1,2,3] taken
 * the zero seat should never be set
 * @returns
 * - 2 if both outer seat blocks ([2,3,4,5] and [6,7,8,9]) are free
 * - 1 if at least one of the three blocks if free
 * - 0 if no block if fully free
 */
function maxAllowedSeatAllocations(reservedMask: number): number {
  let seatMasks: number[] = [1020, 960, 240, 60];

  if ((reservedMask & seatMasks[0]) === 0) {
    return 2;
  }

  for (let i = 1; i <= 3; i++) {
    if ((reservedMask & seatMasks[i]) === 0) {
      return 1;
    }
  }

  return 0;
}

/**
 * Return an number denoting the maximum number of four-person groups that can be assigned.
 * @param n number of rows
 * @param reservedSeats [row, col] seats that have been reserved.
 * @returns maximum number of four-person groups that can be assigned.
 */
function maxNumberOfFamilies(n: number, reservedSeats: number[][]): number {
  let reservedSeatMasks = new Map<number, number>();
  for (let [row, seat] of reservedSeats) {
    reservedSeatMasks.set(row, (reservedSeatMasks.get(row) ?? 0) | (1 << seat));
  }

  let count: number = 2 * (n - reservedSeatMasks.size);
  reservedSeatMasks.forEach((value: number) => {
    count += maxAllowedSeatAllocations(value);
  });

  return count;
}

function testCase(n: number, reserved: number[][], expected: number): void {
  let result: string =
    maxNumberOfFamilies(n, reserved) === expected ? "Pass" : "Fail";
  console.log(`Test case for ${n} should equal expected ? ${result}`);
}

function main(): void {
  console.log("1386. Cinema Seat Allocation");

  testCase(
    3,
    [
      [1, 2],
      [1, 3],
      [1, 8],
      [2, 6],
      [3, 1],
      [3, 10],
    ],
    4,
  );
  testCase(
    2,
    [
      [2, 1],
      [1, 8],
      [2, 6],
    ],
    2,
  );
  testCase(
    4,
    [
      [4, 3],
      [1, 4],
      [4, 6],
      [1, 7],
    ],
    4,
  );
}

main();
