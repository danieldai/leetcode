class Solution {
    public int[] sortArray(int[] nums) {
        int n = nums.length;

        for( int i = n / 2 - 1; i > -1; i--) {
            heapify(nums, n , i);
        }

        for( int i = n-1; i > 0; i--) {
            swap(nums, i, 0);
            heapify(nums, i, 0);
        }

        return nums;
    }

    private void heapify(int[] nums, int n, int i) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int largest = i;

        if(left < n && nums[left] > nums[largest]) {
            largest = left;
        }

        if (right < n && nums[right] > nums[largest]) {
            largest = right;
        }

        if (largest != i) {
            swap(nums, i, largest);
            heapify(nums, n, largest);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}