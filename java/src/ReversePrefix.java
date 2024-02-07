// https://leetcode.com/problems/reverse-prefix-of-word/description/

public class ReversePrefix {
    public String reversePrefix(String word, char ch) {
        StringBuilder res = new StringBuilder();
        char[] charArray = word.toCharArray();

        for (int i = word.indexOf(ch); i >= 0; i--) {
            res.append(charArray[i]);
        }
        for (int i = word.indexOf(ch) + 1; i < charArray.length; i++) {
            res.append(charArray[i]);
        }
        return res.toString();
    }
}
