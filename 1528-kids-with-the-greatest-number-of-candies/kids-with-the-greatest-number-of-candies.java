class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> ans = new ArrayList<>();
        
        int maxCandies = 0;
        for (int candy : candies){
            if (candy > maxCandies) maxCandies = candy;
        }

        for (int candy : candies) {
            ans.add(candy + extraCandies >= maxCandies);
        }

        return ans;
    }
}
