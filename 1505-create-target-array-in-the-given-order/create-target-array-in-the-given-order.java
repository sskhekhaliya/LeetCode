class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
      List<Integer> ansList = new ArrayList<>();

      for (int i = 0; i < nums.length; i++) {
        ansList.add(index[i], nums[i]);
      }

      int[] ansArray = new int[ansList.size()];
      for (int i = 0; i < ansArray.length; i++) {
        ansArray[i] = ansList.get(i);
      }

      return ansArray;
    }
}