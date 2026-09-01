class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next: ListNode | null = null) {
    this.val = val ?? 0;
    this.next = next;
  }
}

function isMinima(a: number, b: number, c: number): boolean {
  return a > b && b < c;
}

function isMaxima(a: number, b: number, c: number): boolean {
  return a < b && b > c;
}

function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
  if (head === null || head.next === null) {
    return [-1, -1];
  }

  let criticalPts: number[] = []
  let idx = 0;
  let pre: ListNode|null = head;
  let curr: ListNode | null = head.next;
  while (curr !== null && curr.next !== null) {
    if (
      isMinima(pre.val, curr.val, curr.next.val) ||
      isMaxima(pre.val, curr.val, curr.next.val)) {
      criticalPts.push(idx);
    }

    pre = curr;
    curr = curr.next;
    idx++;
  }

  if (criticalPts.length < 2) {
    return [-1, -1];
  }

  // get min and max distances
  criticalPts.sort((a, b) => a - b);
  let maxDistance = criticalPts[criticalPts.length - 1] - criticalPts[0];
  let minDistance = Infinity;
  for (let i = 1; i < criticalPts.length; i++) {
    minDistance = Math.min(minDistance, criticalPts[i] - criticalPts[i - 1]);
  }

  return [minDistance, maxDistance];
}

function createList(values: number[]): ListNode | null {
  if (values.length === 0) {
    return null;
  }

  let head = new ListNode(values[0]);
  let curr = head;
  for (let i = 1; i < values.length; i++) {
    curr.next = new ListNode(values[i]);
    curr = curr.next;
  }

  return head;
}

function testCase(nums: number[], expectedMin: number, expectedMax: number): void {
  let head = createList(nums);
  let [resultMin, resultMax] = nodesBetweenCriticalPoints(head);
  let result = (resultMin === expectedMin && resultMax === expectedMax) ? "pass" : "fail";
  console.log(`Test case should pass ? ${result}`);
}

function main(): void {
  console.log("2058. Find the Minimum and Maximum Number of Nodes Between Critical Points");

  testCase([3, 1], -1, -1);
  testCase([5, 3, 1, 2, 5, 1, 2], 1, 3);
  testCase([1, 3, 2, 2, 3, 2, 2, 2, 7], 3, 3);
}

main();
