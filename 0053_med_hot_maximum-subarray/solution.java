class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;

        if (n == 0) {
            return 0;
        }

        int f = 0;
        int result = Integer.MIN_VALUE;

        for (int num : nums) {
            if (f > 0) {
                f += num;
            } else {
                f = num;
            }
            result = Math.max(f, result);
        }

        return result;
    }
}