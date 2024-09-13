class Solution {
    public int strStr(String haystack, String needle) {
        int n1 = needle.length();
        int n2 = haystack.length();

        for(int i = 0; i < n2 - n1 + 1; i++) {
            if(haystack.substring(i, i+n1).equals(needle)) {
                return i;
            }
        }

        return -1;
    }
}