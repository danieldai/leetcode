from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = dict()
        for i, n in enumerate(numbers):
            dic[n] = i
            
        for i, n in enumerate(numbers):
            complement = target - n
            if complement in dic:
                return sorted([i+1, dic[complement]+1])


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            c = target - numbers[i]

            left = i + 1
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == c:
                    return [i+1, mid+1]
                if numbers[mid] > c:
                    right = mid - 1
                else:
                    left = mid + 1