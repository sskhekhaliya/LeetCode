class Solution {
    public int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];

        for (int i = 0; i < nums.length; i++){
            int sum = 0;
            for (int y = 0; y <= i; y++){
                sum = sum + nums[y];
            }
            ans[i] = sum;
        }

        return ans;
    }
}