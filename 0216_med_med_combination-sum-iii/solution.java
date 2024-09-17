import java.util.*;


class Solution {
    List<List<Integer>> result = new ArrayList<>();
    LinkedList<Integer> path = new LinkedList<>();
    int sum = 0;

    public List<List<Integer>> combinationSum3(int k, int n) {
        backTracking(k, n, 1);
        return result;
    }

    private void backTracking(int k, int n, int startIndex) {
        if (path.size() == k) {
            if (sum == n) {
                result.add(new ArrayList<>(path));
            }
            return;
        }

        for (int i = startIndex; i <= 9 - (k - path.size()) + 1; i++) {
            path.add(i);
            sum += i;
            backTracking(k, n, i + 1);
            path.removeLast();
            sum -= i;
        }
    }
}