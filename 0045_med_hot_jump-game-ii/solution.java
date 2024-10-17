class Solution {
    public int jump(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return 0;
        }

        int curDistance = 0;
        int ans = 0;
        int nextDistance = 0;

        for (int i = 0; i < nums.length; i++) {
            nextDistance = Math.max(nextDistance, i + nums[i]);
            if (i == curDistance) {
                ans += 1;
                curDistance = nextDistance;
                if (nextDistance >= nums.length - 1) {
                    break;
                }
            }
        }

        return ans;

    }
}