function create2D<T>(rows: number, cols: number, fill: T): T[][] {
    return Array.from({length: rows}, () => new Array<T>(cols).fill(fill));
}


function rangeSum(presum: number[], i: number, j: number): number {
    return presum[j + 1] - presum[i];
}

function stoneGameV(stoneValue: number[]):number {
    const length = stoneValue.length;

    let presum: number[] = new Array(length + 1).fill(0);
    for(let i = 0; i < length; i++) {
        presum[i + 1] = presum[i] + stoneValue[i];
    }

    let dp: number[][] = create2D(length, length, 0);
    
    for(let l = 2; l <= length; l++) {
        for(let i = 0; i <= length - l; i++) {

            let j = i + l - 1;
            let result: number = 0;

            for (let k = i; k < j; k++) {
                let left = rangeSum(presum, i, k);
                let right = rangeSum(presum, k + 1, j);

                if (left < right) {
                    result = Math.max(result, left + dp[i][k]);
                } else if (left > right) {
                    result = Math.max(result, right + dp[k + 1][j]);
                } else {
                    result = Math.max(result, left + dp[i][k], right + dp[k + 1][j]);
                }
            }

            dp[i][j] = result;
        }
    }
    
    return dp[0][length - 1];
}

function main(): void {
    console.log("1563. Stone Game V");

    let result: number = stoneGameV([6,2,3,4,5,5]);
    console.log(result);
}

main();
