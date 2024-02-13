public class Solution {
    public static boolean isPalindrome(String s) {
        StringBuilder st = new StringBuilder(s);
        return s.equals(st.reverse().toString());
    }

    public String firstPalindrome(String[] words) {
        String ans = "";
        for (int i = 0; i < words.length; i++) {
            if (isPalindrome(words[i])) {
                ans = words[i];
                break;
            }
        }
        return ans;
    }
}
