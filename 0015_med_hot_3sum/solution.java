import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        
        // 将数组进行排序
        Arrays.sort(nums);
        
        // 遍历数组
        for (int i = 0; i < nums.length - 2; i++) {
            // 跳过重复的数字
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            int l = i + 1;
            int r = nums.length - 1;
            
            while (l < r) {
                int s = nums[i] + nums[l] + nums[r];
                
                if (s < 0) {
                    l++;
                } else if (s > 0) {
                    r--;
                } else {
                    // 找到一组满足条件的三元组
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    
                    // 跳过重复的左边元素
                    while (l < r && nums[l] == nums[l + 1]) {
                        l++;
                    }
                    
                    // 跳过重复的右边元素
                    while (l < r && nums[r] == nums[r - 1]) {
                        r--;
                    }
                    
                    l++;
                    r--;
                }
            }
        }
        
        return res;
    }
}