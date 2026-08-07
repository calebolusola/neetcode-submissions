func twoSum(nums []int, target int) []int {
    encountered := make(map[int]int)

    for idx, num := range nums {
        diff := target - num
        
        if _, exists := encountered[diff]; !exists {
            encountered[num] = idx
        } else {
			return []int{encountered[diff], idx}
        }
    }

    return []int{0}
}
