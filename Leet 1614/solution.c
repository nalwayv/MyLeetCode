/** Return the max depth of nested parentheses
*/
int maxDepth(char* s) {
    int depth = 0 ;
    int max_depth = 0;

    for(int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            depth++;
        }

        if (s[i] == ')') {
            depth--;
        }
        
        if (depth > max_depth) {
            max_depth = depth;
        }
    }

    return max_depth;
}
