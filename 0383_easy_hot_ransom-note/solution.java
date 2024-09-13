class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int [] counter = new int[26];

        for (int i = 0; i < magazine.length(); i++) {
            counter[magazine.charAt(i) - 'a']++;
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            counter[ransomNote.charAt(i) - 'a']--;

            if (counter[ransomNote.charAt(i) - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
}


class Solution2 {
    public boolean canConstruct(String ransomNote, String magazine) {
        int [] counterA = new int[26];
        int [] counterB = new int[26];

        for (int i = 0; i < ransomNote.length(); i++) {
            counterA[ransomNote.charAt(i) - 'a']++;
        }

        for (int i = 0; i < magazine.length(); i++) {
            counterB[magazine.charAt(i) - 'a']++;
        }

        for(int i = 0; i < 26; i++) {
            if(counterA[i] > counterB[i]) {
                return false;
            }
        }

        return true;

    }
}