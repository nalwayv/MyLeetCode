#include <stdlib.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) 
{
	// merge both sorted arrays

	int totalSize = nums1Size + nums2Size;
	int* merged = malloc(totalSize * sizeof(int));
	
	int p1 = 0;
	int p2 = 0;
	int p3 = 0;
	
	while (p1 < nums1Size && p2 < nums2Size) 
	{
		if (nums1[p1] < nums2[p2])
		{
			merged[p3++] = nums1[p1++] 
		}
		else
		{
			merged[p3++] = nums2[p2++]
		}
	}
	
	while (p1 < nums1Size)
	{
		merged[p3++] = nums1[p1++];
	}

	while (p2 < nums2Size)
	{
		merged[p3++] = nums2[p2++];
	}
	
	// get median

	int middle = totalSize / 2;
	double median;
	if (totalSize % 2 == 0)
	{
		median = (merged[middle] + merged[middle - 1]) / 2.0;
	}
	else
	{
		median = merged[middle];
	}

	free(merged);

	return median;
}
