/**
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
function twoEditWords(queries, dictionary) {
    let result = [];

    for (let q of queries) {
        for (let d of dictionary) {
            let diff = 0;

            for (let i = 0; i < q.length; i++) {
                if (diff > 2) {
                    break;
                }

                if (q[i] !== d[i]) {
                    diff++;
                }
            }

            if (diff <= 2) {
                result.push(q);
                break
            }
        }
    }

    return result;
}