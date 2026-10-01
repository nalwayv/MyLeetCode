/**
 * 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
 *
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxDepthAfterSplit(char* seq, int* returnSize) {

    int n = 0;
    while (seq[n] != '\0') {
        n++;
    }

    int depth = 0;
    int* result = malloc(sizeof(*result) * n);

    for(int i = 0; i  < n; i++) {
        if (seq[i] == '(') {
            result[i] = depth % 2;
            depth++;
        } else {
            depth--;
            result[i] = depth % 2;
        }
    }

    *returnSize = n;
    return result;
}