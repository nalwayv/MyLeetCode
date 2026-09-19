static void populate_seen(int* seen, int* digits, int digitsSize, int k) {
    if (k == 3 && digits[0] != 0) {
        // build 3 digit number
        int number = 0;
        number = number * 10 + digits[0];
        number = number * 10 + digits[1];
        number = number * 10 + digits[2];

        const int in_range = number >= 100 && number <= 999 ? 1 : 0;
        const int is_even = number % 2 == 0;

        if (in_range && is_even) {
            if (!seen[number]) {
                seen[number] = 1;
            }
        }
    } else {
        for (int i = k; i < digitsSize; i++) {
            int tmp = digits[i]; digits[i] = digits[k]; digits[k] = tmp;
            populate_seen(seen, digits, digitsSize, k + 1);
            tmp = digits[i]; digits[i] = digits[k]; digits[k] = tmp;
        }
    }
}

int total_numbers(int* digits, int digitsSize) {
    int seen[1000] = {0};
    
    populate_seen(seen, digits, digitsSize, 0);
    
    int count = 0;
    for(int i = 0; i < 1000; i++) {
        if(seen[i]) {
            count++;
        }
    }

    return count;
}