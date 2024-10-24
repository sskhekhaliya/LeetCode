class Solution {
    public int[][] generateMatrix(int n) {
        int[][] ans = new int[n][n];
        int left = 0, right = n-1;
        int top = 0, bottom = n-1;

        int i = 1;
        while (left <= right && top <= bottom){
            for (int j = left; j <= right; j++) {
                ans[top][j] = i;
                i++;
            }
            top++;

            for (int j = top; j <= bottom ; j++) {
                ans[j][right] = i;
                i++;
            }
            right--;

            if (top <= bottom){
                for (int j = right; j >= left ; j--) {
                    ans[bottom][j] = i;
                    i++;
                }
                bottom--;
            }

            if (left <= right) {
                for (int j = bottom; j >= top ; j--) {
                    ans[j][left] = i;
                    i++;
                }
                left++;
            }
            
        }
        return ans;
    }
}