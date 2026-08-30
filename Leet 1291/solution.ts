function sequentialDigits(low: number, high: number): number[] {
  let lowStr = low.toString();
  let highStr = high.toString();

  let digits = "123456789";
  let result: number[] = [];

  for (let i = lowStr.length; i <= highStr.length; i++) {
    for (let k = 0; k <= 9 - i; k++) {
      let num = Number(digits.slice(k, k + i));

      if (low <= num && num <= high) {
        result.push(num);
      }
    }
  }

  return result;
}

function main(): void {
  console.log("1291. Sequential Digits");

  let result: number[] = sequentialDigits(100, 300);
  for (let r of result) {
    console.log(r);
  }
}

main();
