class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int y = 0;
        int xx = x;

        while( x > 0) {
            y = y * 10 + x % 10;
            x = x / 10;
        }

        return xx == y;
    }
}