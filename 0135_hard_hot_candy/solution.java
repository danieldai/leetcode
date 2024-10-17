import java.util.stream.IntStream;

class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;

        int[] result = new int[n];

        result[0] = 1;

        for (int i = 1; i < n ; i++) {
            result[i] = ratings[i] > ratings[i - 1] ? result[i - 1] + 1 : 1;
        }

        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                result[i] = Math.max(result[i], result[i + 1] + 1);
            }
        }

        return IntStream.of(result).sum();

    }
}