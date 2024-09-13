class Solution {
    public String reverseStr(String s, int k) {
        StringBuilder sb = new StringBuilder();

        int n = s.length();

        for(int i = 0; i < n; i += 2 * k) {
            sb.append(reverseStr(s.substring(i, Math.min(i + k, n))));

            if (n > i + k) {
                sb.append(s.substring(i + k, Math.min(i + 2 * k, n)));
            }
        }

        return sb.toString();
    }

    private String reverseStr(String s) {
        return new StringBuilder(s).reverse().toString();
    }
}