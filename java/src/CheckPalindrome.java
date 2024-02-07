// https://leetcode.com/problems/valid-palindrome/
public class CheckPalindrome {
    public boolean isValidPalindrome(String s) {
        StringBuilder current = new StringBuilder();
        StringBuilder last = new StringBuilder();
        if (s.isEmpty() || s.equals(" ")) return true;
        for (char c : s.toCharArray()) {
            if (Character.isAlphabetic(c) || Character.isDigit(c)) {
                current.append(Character.toLowerCase(c));
            }
        }
        last.append(current);
        return last.toString().contentEquals(current.reverse().toString());
    }
}
