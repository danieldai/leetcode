class Solution {
    public int wiggleMaxLength(int[] nums) {
        int n = nums.length;
        int preDiff = 0;
        int curDiff = 0;
        int result = 1;

        for (int i = 0; i < n - 1; i ++) {
            curDiff = nums[i + 1] - nums[i];
            if ((preDiff <= 0 && curDiff > 0) || (preDiff >= 0 && curDiff < 0)) {
                result ++;
                preDiff = curDiff;
            }
        }

        return result;

    }
}

// DP
class Solution2 {
    public int wiggleMaxLength(int[] nums) {
        // 0 i 作为波峰的最大长度
        // 1 i 作为波谷的最大长度
        int dp[][] = new int[nums.length][2];

        dp[0][0] = dp[0][1] = 1;

        for (int i = 1; i < nums.length; i ++) {
            //i 自己可以成为波峰或者波谷
            dp[i][0] = dp[i][1] = 1;
            
            for (int j = 0; j < i; j++) {
                if(nums[j] > nums[i]) {
                    // i 是波谷
                    dp[i][1] = Math.max(dp[i][1], dp[j][0] + 1);
                }
                if(nums[j] < nums[i]) {
                    // i 是波峰
                    dp[i][0] = Math.max(dp[i][0], dp[j][1] + 1);
                }
            }
        }

        return Math.max(dp[nums.length - 1][0], dp[nums.length - 1][1]);
    }
}