// https://leetcode.com/problems/counting-words-with-a-given-prefix/

public class PrefixCount {
    public int countPrefix(String[] words, String pref) {
        int count = 0;
        for (String word : words) {
            if (startsWith(word, pref)) {
                count++;
            }
        }
        return count;
    }

    public boolean startsWith(String word, String pref) {
        boolean res = true;
        if (word.length() < pref.length()) return false;
        for (int i = 0; i < pref.length(); i++) {
            if (word.charAt(i) != pref.charAt(i)) {
                res = false;
            }
        }
        return res;
    }
}
