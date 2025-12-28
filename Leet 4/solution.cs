// NOTE - left and right must be sorted
int[] MergeSortedLists(int[] nums1, int[] nums2)
{
    int[] result = new int[nums1.Length + nums2.Length];
    int nums1Idx = 0;
    int nums2Idx = 0;
    int idx = 0;

    while (nums1Idx < nums1.Length && nums2Idx < nums2.Length)
    {
        if (nums1[nums1Idx] < nums2[nums2Idx])
        {
            result[idx++] = nums1[nums1Idx++];
        }
        else
        {
            result[idx++] = nums2[nums2Idx++];
        }
    }

    while (nums1Idx < nums1.Length)
    {
        result[idx++] = nums1[nums1Idx++];
    }

    while (nums2Idx < nums2.Length)
    {
        result[idx++] = nums2[nums2Idx++];
    }

    return result;
}


float FindMedianSortedArrays(int[] nums1, int[] nums2)
{
    int[] merged = MergeSortedLists(nums1, nums2);
    int mid = merged.Length / 2;

    float result;
    if (merged.Length % 2 == 0)
    {
        result = (merged[mid] + merged[mid - 1]) / 2.0f;
    }
    else
    {
        result = merged[mid];
    }

    return result;
}


Console.WriteLine("4. Median of Two Sorted Arrays");

int[] nums1 = [1, 3];
int[] nums2 = [2];
Console.WriteLine($"Case1: {FindMedianSortedArrays(nums1, nums2)}");