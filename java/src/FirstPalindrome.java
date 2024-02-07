// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

public class FirstPalindrome {

    public String findFirstPalindrome(String[] words) {
        for (int i = 0; i < words.length; i++) {
            if (isPalindrome(words[i])) {
                return words[i];
            }
        }
        return "";
    }

    public boolean isPalindrome(String s) {
        StringBuilder reversed = new StringBuilder();
        reversed.append(s).reverse();
        return s.contentEquals(reversed);
    }
}
