import java.util.HashMap;
import java.util.Map;

class Solution {
    public int romanToInt(String s) {
        // 创建一个映射罗马数字到对应的整数值
        Map<Character, Integer> digits = new HashMap<>();
        digits.put('I', 1);
        digits.put('V', 5);
        digits.put('X', 10);
        digits.put('L', 50);
        digits.put('C', 100);
        digits.put('D', 500);
        digits.put('M', 1000);

        // 获取字符串s的最后一个字符的整数值作为初始值
        int num = digits.get(s.charAt(s.length() - 1));
        int last = num;

        // 从倒数第二个字符开始，向前遍历字符串
        for (int i = s.length() - 2; i >= 0; i--) {
            int current = digits.get(s.charAt(i));
            if (current < last) {
                num -= current;  // 如果当前字符代表的值小于前一个字符的值，则减去当前值
            } else {
                num += current;  // 否则加上当前值
            }
            last = current;  // 更新last为当前字符的值
        }

        return num;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.romanToInt("MCMXCIV"));  // 输出: 1994
    }
}
