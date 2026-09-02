function findStart(classroom: string[]): { row: number; col: number } {
  for (let i = 0; i < classroom.length; i++) {
    let idx = classroom[i].indexOf("S");
    if (idx !== -1) {
      return { row: i, col: idx };
    }
  }
  return { row: -1, col: -1 };
}

function minMoves(classroom: string[], energy: number): number {
  if (classroom.length === 0 || classroom[0].length === 0) {
    return -1;
  }

  let { row: startX, col: startY } = findStart(classroom);

  if (startX === -1 || startY === -1) {
    return -1;
  }

  // helper functions
  const mapKey = (row: number, col: number) => `${row},${col}`;
  const pickUpLitter = (mask: number, litter: number) => mask |= 1 << litter;

  let rows = classroom.length;
  let cols = classroom[0].length;

  // store classroom litter locations along with id for mask
  let litter = new Map<string, number>();
  let id = 0;
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (classroom[row][col] === "L") {
        litter.set(mapKey(row, col), id++);
      }
    }
  }

  let target = (1 << litter.size) - 1;

  let best: number[][][] = Array.from({ length: target + 1 }, () =>
    Array.from({ length: rows }, () => Array(cols).fill(-1)),
  );


  let directions = [
    { x: 0, y: 1 },
    { x: 0, y: -1 },
    { x: 1, y: 0 },
    { x: -1, y: 0 },
  ];

  let frame = [{ row: startX, col: startY, mask: 0, energy: energy, steps: 0 }];
  while (frame.length > 0) {
    let { row, col, mask, energy: remainingEnergy, steps } = frame.shift()!;

    // reset energy
    if (classroom[row][col] == "R") {
      remainingEnergy = energy;
    }

    let litterID = litter.get(mapKey(row, col));
    if (litterID !== undefined) {
      mask = pickUpLitter(mask, litterID);
    }

    // all litter picked up
    if (mask === target) {
      return steps;
    }

    // already visited
    if (remainingEnergy <= best[mask][row][col]) {
      continue;
    }

    best[mask][row][col] = remainingEnergy;

    // cant proceed any further as energy is needed to move
    if (remainingEnergy === 0) {
      continue;
    }

    // explore all directions
    for (let { x, y } of directions) {
      let nextRow = row + x;
      let nextCol = col + y;

      // out of bounds
      if (nextRow < 0 || nextCol < 0 || nextRow >= rows || nextCol >= cols) {
        continue;
      }

      // blocked
      if (classroom[nextRow][nextCol] === "X") {
        continue;
      }

      frame.push({
        row: nextRow,
        col: nextCol,
        mask,
        energy: remainingEnergy - 1,
        steps: steps + 1,
      });
    }
  }

  // no solution found
  return -1;
}

function main(): void {
  console.log("3568. Minimum Moves to Clean the Classroom");

  let result: number = minMoves(["S.", "XL"], 2);
  console.log(`Test case for [S., XL] should equal 2 ? ${result}`);
}

main();
