import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> metNumbers = new HashSet<>();

        while(n != 1 && !metNumbers.contains(n)) {
            metNumbers.add(n);
            n = getNextNumber(n);
        }

        return n == 1;
    }

    private int getNextNumber(int n ) {
        int result = 0;

        while (n > 0) {
            int m = n % 10;
            n = n / 10;
            result += m*m;
        }

        return result;
    }
}