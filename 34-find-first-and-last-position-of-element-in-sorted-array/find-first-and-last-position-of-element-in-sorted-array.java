class Solution {
    public int[] searchRange(int[] nums, int target) {
        int firstValue = search(nums, target, true);
        int lastValue = search(nums, target, false);
        return new int[] {firstValue, lastValue};
    }

    int search(int[] nums, int target, boolean fIndex) {
        int ans = -1;
        int start = 0;
        int end = nums.length - 1;

        while (start <= end){
            int mid = start + (end - start)/2;

            if (target < nums[mid]) {
                end = mid - 1;
            } else if (target > nums[mid]) {
                start = mid + 1;
            } else {
                ans = mid;
                if (fIndex){
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }
        }
        return ans;
    }
    
}