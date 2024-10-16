class Solution {
    public int largestAltitude(int[] gain) {
        int[] altitude = new int[gain.length + 1];
        altitude[0] = 0;

        int temp = 0;
        int highest = 0;
        
        for(int i = 0; i < altitude.length-1; i++) {
            temp = temp + gain[i];
            altitude[i+1] = temp;
            if (temp > highest) {
                highest = temp;
            }
        } 

        return highest;
    }
}