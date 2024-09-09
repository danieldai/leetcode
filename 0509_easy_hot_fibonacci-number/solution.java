class Solution {

    public int fib2(int n) {
        if (n <= 1)
            return n;
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];

    }

    public int fib(int n) {
        if (n <= 1)
            return n;

        int prePre = 0;
        int pre = 1;
        int result = 0;
        for (int i = 2; i < n + 1; i++) {
            result = prePre + pre;
            prePre = pre;
            pre = result;
        }

        return result;
    }
}