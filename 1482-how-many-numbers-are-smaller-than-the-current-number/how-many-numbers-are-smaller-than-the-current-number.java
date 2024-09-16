class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++){
            ans[i] = count(nums, nums[i]);
        }

        return ans;
    }
    int count(int[] arr, int num){
        int count = 0;
        for (int i : arr){
            if (num > i) count++;
        }
        return count;
    }
}