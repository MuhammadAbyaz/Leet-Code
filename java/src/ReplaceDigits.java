// https://leetcode.com/problems/replace-all-digits-with-characters/

public class ReplaceDigits {
    public String replaceDigits(String s) {
        int charValue = 0;
        StringBuilder res = new StringBuilder();
        res.append(s);
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0) {
                charValue = s.charAt(i);
            }
            if (i % 2 != 0) {
                charValue += Character.getNumericValue(s.charAt(i));
                res.setCharAt(i, (char) charValue);
            }
        }
        return res.toString();
    }
}
