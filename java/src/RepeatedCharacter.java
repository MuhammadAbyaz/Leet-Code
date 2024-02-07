import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/first-letter-to-appear-twice/description/
public class RepeatedCharacter {
    public char findRepeatedCharacter(String s) {
        char res = ' ';
        Set<Character> set = new HashSet<>();
        for (char c : s.toCharArray()) {
            if (set.contains(c)) {
                res = c;
                break;
            } else {
                set.add(c);
            }
        }
        return res;
    }
}
