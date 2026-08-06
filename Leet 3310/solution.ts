/**
 * Return array containing all remaining methods after removing all suspicious ones.
 * @param n positive number that is >= 1
 * @param k positive number between 0 and n - 1
 * @param invocations describe how nodes from n are connect to one another in a directed graph.
 * @returns array of numbers remaining after removing suspicious.
 */
function remainingMethods(
  n: number,
  k: number,
  invocations: number[][],
): number[] {
  let adjacency: number[][] = Array.from({ length: n }, () => []);
  for (const [u, v] of invocations) {
    adjacency[u].push(v);
  }

  // mark all nodes that can be reached by k as suspicious
  let suspicious: boolean[] = Array(n).fill(false);
  suspicious[k] = true;

  let stack: number[] = [k];
  while (stack.length > 0) {
    const node: number = stack.pop()!;
    for (const neighbour of adjacency[node]) {
      if (!suspicious[neighbour]) {
        suspicious[neighbour] = true;
        stack.push(neighbour);
      }
    }
  }

  let result: number[] = Array.from({ length: n }, (_, i) => i);

  for (const [u, v] of invocations) {
    if (!suspicious[u] && suspicious[v]) {
      return result;
    }
  }

  return result.filter((_, i) => !suspicious[i]);
}

/**
 * Return true if arr1 equals arr2 else false.
 * @param arr1 array of numbers
 * @param arr2 array of numbers
 * @returns true is arr1 equals arr2
 */
function equalityBetweenArrays(arr1: number[], arr2: number[]): boolean {
  if (arr1.length !== arr2.length) {
    return false;
  }

  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }

  return true;
}

function testCase(
  n: number,
  k: number,
  invocations: number[][],
  expected: number[],
): void {
  const arr: number[] = remainingMethods(n, k, invocations);
  console.log(arr);
  const testResult = equalityBetweenArrays(arr, expected) ? "Pass" : "Fail";
  console.log(`Test Result: ${testResult}`);
}

function main(): void {
  console.log("3310. Remove Methods From Project");

  const invocations1: number[][] = [
    [1, 2],
    [0, 1],
    [3, 2],
  ];
  const expected1: number[] = [0, 1, 2, 3];
  testCase(4, 1, invocations1, expected1);

  const invocations2: number[][] = [
    [1, 2],
    [0, 2],
    [0, 1],
    [3, 4],
  ];
  const expected2: number[] = [3, 4];
  testCase(5, 0, invocations2, expected2);
}

main();
