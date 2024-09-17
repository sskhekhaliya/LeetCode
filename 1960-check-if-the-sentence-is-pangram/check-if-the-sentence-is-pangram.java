class Solution {
    public boolean checkIfPangram(String sentence) {
        String alph = "abcdefghijklmnopqrstuvwxyz";
        for (char ch : alph.toCharArray()) {
            if (!sentence.contains(String.valueOf(ch))) {
                return false;
            }
        }
        return true;
    }
}
