import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        nums = IntStream.of(nums).boxed().sorted((o1, o2) -> Math.abs(o2) - Math.abs(o1)).mapToInt(Integer::intValue).toArray();

        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (nums[i] < 0 && k > 0) {
                nums[i] *= -1;
                k--;
            }
        }

        if(k % 2 == 1) {
            nums[n - 1] *= -1;
        }

        return Arrays.stream(nums).sum();
    }
}