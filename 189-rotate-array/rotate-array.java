class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        int index = n - k;
        // reversing part 1: 0 to index - 1
        reverse(nums, 0, index - 1);

        // reversing part 2: index to nums.length - 1
        reverse(nums, index, n - 1);

        // reversing the new whole array
        reverse(nums, 0, n - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}