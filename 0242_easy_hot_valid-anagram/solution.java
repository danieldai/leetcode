class Solution {
    public boolean isAnagram(String s, String t) {

        int[] records = new int[26];

        for(char c : s.toCharArray()) {
            records[c - 'a']++;
        }

        for(char c : t.toCharArray()) {
            records[c - 'a']--;
        }

        for(int r : records) {
            if(r != 0) {
                return false;
            }
        }

        return true;
        
    }
}