#include <stdlib.h>

/**
 * 1385. Find the Distance Value Between Two Arrays.
 */
int findTheDistanceValue(int* arr1, int arr1Size, int* arr2, int arr2Size, int d) {
    int result = arr1Size;

    for (int i = 0; i < arr1Size; i++) {
        for (int j = 0; j < arr2Size; j++) {
            if (abs(arr1[i] - arr2[j]) <= d) {
                result -= 1;
                break;
            }
        }
    }

    return result;
}
