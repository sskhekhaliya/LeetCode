class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans = 0;
        for (int i = 0; i < accounts.length; i++){
            int sumAccount = sum(accounts[i]);
            if (sumAccount > ans) ans = sumAccount;
        }
        return ans;
    }

    static int sum(int[] arr){
        int sum = 0;
        for (int i : arr){
            sum = sum + i;
        }
        return sum;
    }
}