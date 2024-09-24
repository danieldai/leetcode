https://leetcode.com/problems/binary-search/description/


视频讲解

https://www.bilibili.com/video/BV1eg411w7gn/?p=43&vd_source=dead283aa3efb297fb9f9c1d2b8e9fe8

过去3个月
字节跳动
3
过去6个月
Meta
2
微软Microsoft
2
6个月前
亚马逊
6
谷歌Google



注意左右边界索引的初始话的值，以及循环的终止条件

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # 初始化为最右边的索引
        mid = left + (right - left) // 2

        while left <= right: # 注意这个循环终止条件
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1 
            elif nums [mid] < target:
                left = mid + 1
            mid = left + (right - left) // 2

        return -1
```