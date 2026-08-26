function shortestBeautifulSubstring(s: string, k: number): string {
    let counter = new Map<string, number>([
        ["0", 0],
        ["1", 0],
    ]);

    let resultStr: string = "";

    let p1: number = 0;
    for (let p2 = 0; p2 < s.length; p2++) {
        let p2Value = counter.get(s[p2]) ?? 0;
        counter.set(s[p2], p2Value + 1);

        while (counter.get("1")! > k) {
            let p1Value = counter.get(s[p1])!;
            counter.set(s[p1], p1Value - 1);
            p1++;
        }

        if (counter.get("1")! === k) {
            // strip leading zero's from beautiful.
            let beautifulStr: string = s.slice(p1, p2 + 1).replace(/^0+/, "");

            if (
                resultStr === "" ||
                beautifulStr.length < resultStr.length ||
                (beautifulStr.length === resultStr.length && beautifulStr < resultStr)
            ) {
                resultStr = beautifulStr;
            }
        }
    }

    return resultStr;
}

function main(): void {
    console.log("2904. Shortest and Lexicographically Smallest Beautiful String")

    console.log(shortestBeautifulSubstring("100011001", 3), "11001");
    console.log(shortestBeautifulSubstring("1011", 2), "11");
    console.log(shortestBeautifulSubstring("01011101000111110", 5), "11111");
}

main();