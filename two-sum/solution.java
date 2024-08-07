import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
                Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[]{map.get(complement), i};
            }
            
            map.put(nums[i], i);
        }
        
        // 如果没有找到符合条件的索引对，这里可以返回一个空数组或者抛出异常
        return new int[]{};
    }
}