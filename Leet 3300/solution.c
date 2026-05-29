//////////////////////////////////////////////////////////
// 3300. Minimum Element After Replacement With Digit Sum

int minI(int a, int b){
    if (a < b) {
        return a;
    }
    return b;
}

int minElement(int* nums, int numsSize) {
    int result = 0x7FFFFFFF;

    for(int i = 0; i < numsSize; i++){
        int num = nums[i];
        int sum = 0;
        
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }

        result = minI(result, sum);
    }
    
    return result;
}
