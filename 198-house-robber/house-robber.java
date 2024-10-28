class Solution {
    public int rob(int[] nums) {

        if (nums.length < 2) {
            return nums[0];
        }

        int n = nums.length;

        int[] totalLoot = new int[2];

        totalLoot[0] = nums[0];
        totalLoot[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length ; i++) {
            int max = Math.max(totalLoot[0] + nums[i], totalLoot[1]);
            totalLoot[0] = totalLoot[1];
            totalLoot[1] = max;
        }

        return totalLoot[1];
    }

}