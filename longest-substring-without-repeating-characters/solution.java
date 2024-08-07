import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
                int length = s.length();
        if (length < 2) {
            return length;
        }

        int result = 0;
        Set<Character> charSet = new HashSet<>();

        int i = 0, j = 0;
        while (i < length && j < length) {
            if (!charSet.contains(s.charAt(j))) {
                charSet.add(s.charAt(j));
                result = Math.max(result, charSet.size());
                j++;
            } else {
                while (s.charAt(i) != s.charAt(j)) {
                    charSet.remove(s.charAt(i));
                    i++;
                }
                charSet.remove(s.charAt(i));
                i++;
            }
        }
        return result;
    }
}