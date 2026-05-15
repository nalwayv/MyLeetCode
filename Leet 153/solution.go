
func findMin(nums []int) int {
    result := nums[0]
    for i:= 0; i < len(nums) - 1; i++ {
        if nums[i+1] - nums[i] < 0 {
            result = min(result, nums[i + 1])
        }
    }
    return result
}