class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;

        for (int i : nums){
            if (countDigit(i) % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    public int countDigit(int num){
        int count = 0;
        int i = num;
        while (i > 0) {
            i = i / 10;
            count++;
        }
        return count;
    }
}