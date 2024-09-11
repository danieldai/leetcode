class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        final int L = nums.length;
        int left = 0;
        int right = 0;
        int sum = 0;
        int minLen = Integer.MAX_VALUE;

        while(right < L) {
            sum += nums[right];

            while(sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left];
                left++;
            }
            right++;
        }

        return minLen != Integer.MAX_VALUE ? minLen : 0;

    }
}