import java.util.HashMap;
import java.util.Map;

class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> records = new HashMap<>();

        for (int a : nums1) {
            for (int b : nums2) {
                records.put(a+b, records.getOrDefault(a+b, 0)+1);
            }
        }

        int result = 0;

        for (int c : nums3) {
            for ( int d : nums4) {
                result += records.getOrDefault(-(c+d), 0);
                
            }
        }

        return result;
        
    }
}