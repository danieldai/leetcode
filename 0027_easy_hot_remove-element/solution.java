class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums == null || nums.length == 0) {
            return 0;
        }

        int n = nums.length;
        int i = n - 1;

        while (i >= 0 && nums[i] == val) {
            i--;
        }

        for (int j = i-1; j > -1; j--) {
            if (nums[j] == val) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i--;
            }
        }

        return i + 1; 
    }
}