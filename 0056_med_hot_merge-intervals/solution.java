import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> result = new LinkedList<>();

        result.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            if (result.getLast()[1] >= intervals[i][0]) {
                result.getLast()[1] = Math.max(result.getLast()[1], intervals[i][1]);
            } else {
                result.add(intervals[i]);
            }
        }

        return result.toArray(new int[result.size()][]);

    }
}