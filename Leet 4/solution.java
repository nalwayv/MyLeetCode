class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] combine = new int[nums1.length + nums2.length];
        int idx1 = 0;
        int idx2 = 0;
        int idx = 0;
        while(idx1 < nums1.length && idx2 < nums2.length)
        {
            if(nums1[idx1] < nums2[idx2])
            {
                combine[idx++] = nums1[idx1++];
            }
            else
            {
                combine[idx++] = nums2[idx2++];
            }
        }
        
        while(idx1 < nums1.length)
        {
            combine[idx++] = nums1[idx1++];
        }
        
        while(idx2 < nums2.length)
        {
            combine[idx++] = nums2[idx2++];
        }
        
        if(combine.length % 2  == 0)
        {
            int at = combine.length / 2;
            return (combine[at - 1] + combine[at]) / 2.0f;
        }
        
        return combine[combine.length / 2];
    }
}