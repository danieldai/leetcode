package main

import "fmt"

func twoSum(nums []int, target int) []int {
    d := make(map[int]int)
    
    for i, num := range nums {
        complement := target - num
        if val, ok := d[complement]; ok && val != i {
            return []int{i, val}
        }
        d[num] = i
    }
    
    return nil
}

func main() {
    nums := []int{2, 7, 11, 15}
    target := 9
    result := twoSum(nums, target)
    fmt.Println(result) // 输出: [1, 0]
}