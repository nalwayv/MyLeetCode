static int detect_capital_use(const char* word) {
    int count = 0;
    int length = 0;
    
    while (word[length] != '\0') {
        if (word[length] - 'A' >= 0 && word[length] - 'A' < 26) {
            count++;
        }

        length++;
    }

    // all capitals
    // only one capital
    // only first letter is capital
    if (count == length ||
        count == 0 ||
        count == 1 && (word[0] - 'A' >= 0 && word[0] - 'A' < 26)) {
        return 1;
    }

    return 0;
}