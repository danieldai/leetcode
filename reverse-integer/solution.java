class Solution {
    public int reverse(int x) {
        int low = -(int)Math.pow(2, 31) - 1; // Integer.MIN_VALUE in Java is -2147483648
        int high = (int)Math.pow(2, 31);     // Integer.MAX_VALUE in Java is 2147483647
        
        try {
            if (x < 0) {
                int s = -Integer.parseInt(new StringBuilder(String.valueOf(-x)).reverse().toString());
                return s >= low ? s : 0;
            } else {
                int s = Integer.parseInt(new StringBuilder(String.valueOf(x)).reverse().toString());
                return s <= high ? s : 0;
            }
        } catch(Exception e) {
            return 0;
        }
    }
}

class Solution2 {
    public int reverse(int x) {
        int low = -(int)Math.pow(2, 31) - 1; // 下界: Integer.MIN_VALUE - 1
        int high = (int)Math.pow(2, 31);     // 上界: Integer.MAX_VALUE
        
        int result = 0;
        int sign = 1;
        
        if (x < 0) {
            sign = -1;
            x = -x;
        }

        while (x > 0) {
            int digit = x % 10;

            if ((result * 10 + digit) / 10 != result) {
                return 0;
            }

            result = result * 10 + digit;
            x = x / 10;
        }

        result = sign * result;

        if (low <= result && result <= high) {
            return result;
        } else {
            return 0;
        }
    }
}