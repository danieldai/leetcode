import java.util.List;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        
        if (strs.length == 1) {
            return strs[0];
        }

        String prefix = "";

        while (true) {
            // 如果当前前缀长度大于等于第一个字符串的长度，则返回当前前缀
            if (prefix.length() >= strs[0].length()) {
                return prefix;
            }

            // 更新前缀
            prefix = strs[0].substring(0, prefix.length() + 1);

            // 检查前缀是否是所有字符串的前缀
            for (int i = 1; i < strs.length; i++) {
                if (!strs[i].startsWith(prefix)) {
                    return prefix.length() > 0 ? prefix.substring(0, prefix.length() - 1) : "";
                }
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] strs = {"flower", "flow", "flight"};
        System.out.println(sol.longestCommonPrefix(strs));  // 输出: "fl"
    }
}