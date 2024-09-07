import java.util.Arrays;

public class Solution {
    public int arrayPairSum(int[] nums) {
        // 对数组进行排序
        Arrays.sort(nums);
        
        int sum = 0;
        
        // 每隔两个元素相加
        for (int i = 0; i < nums.length; i += 2) {
            sum += nums[i];
        }
        
        return sum;
    }
}