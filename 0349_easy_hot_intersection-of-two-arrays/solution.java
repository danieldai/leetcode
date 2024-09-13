import java.util.Set;
import java.util.HashSet;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> numsSet = new HashSet<>();

        for(int num : nums1) {
            numsSet.add(num);
        }

        Set<Integer> resultList = new HashSet<>();

        for(int num : nums2) {
            if(numsSet.contains(num)) {
                resultList.add(num);
            }
        }

        return resultList.stream().mapToInt(x -> x).toArray();
    }
}