class Solution {
    public int[] countBits(int n) {
        int[] bits = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            bits[i] = bits[i & (i - 1)] + 1;
        }
        return bits;
    }

    // 如果一个数是奇数，那么它的1的个数为 n-1 的 1的个数加1
    // 如果一个数是偶数，那么它的1的个数为 为 n/2 的 1的个数相同
    public int[] countBits2(int num) {
        int[] bits = new int[num + 1];
        bits[0] = 0;
        for (int i = 1; i <= num; i++)
            bits[i] = ((i & 1) == 1 ? bits[i - 1] + 1 : bits[i >> 1]);
        return bits;

    }

}