import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private static final Map<Character, String> chars = new HashMap<>();
    
    static {
        chars.put('2', "abc");
        chars.put('3', "def");
        chars.put('4', "ghi");
        chars.put('5', "jkl");
        chars.put('6', "mno");
        chars.put('7', "pqrs");
        chars.put('8', "tuv");
        chars.put('9', "wxyz");
    }

    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.length() == 0) {
            return new ArrayList<>();
        }
        
        if (digits.length() == 1) {
            String letters = chars.get(digits.charAt(0));
            List<String> result = new ArrayList<>();
            for (char c : letters.toCharArray()) {
                result.add(String.valueOf(c));
            }
            return result;
        }
        
        List<String> res = new ArrayList<>();
        String firstCharLetters = chars.get(digits.charAt(0));
        for (char a : firstCharLetters.toCharArray()) {
            for (String s : letterCombinations(digits.substring(1))) {
                res.add(a + s);
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String digits = "23";
        List<String> result = sol.letterCombinations(digits);
        System.out.println(result);  // 输出: [ad, ae, af, bd, be, bf, cd, ce, cf]
    }
}
