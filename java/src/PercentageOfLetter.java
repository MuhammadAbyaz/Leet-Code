// https://leetcode.com/problems/percentage-of-letter-in-string/
public class PercentageOfLetter {
    public int percentage(String s, char letter) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == letter) {
                count++;
            }
        }
        return (count * 100) / s.length();
    }
}
