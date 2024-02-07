// https://leetcode.com/problems/unique-morse-code-words/

// improve memory

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class MorseCode {
    public int uniqueMorseCode(String[] words) {
        String[] stringArray = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};
        Set<String> stringSet = new HashSet<>();
        StringBuilder value;
        HashMap<Character, String> hashMap = new HashMap<>();
        char c = 'a';

        for (int i = 0; i < stringArray.length; i++) {
            hashMap.put(c, stringArray[i]);
            c++;
        }

        for (String word : words) {
            value = new StringBuilder();
            for (Character character : word.toCharArray()) {
                value.append(hashMap.get(character));
            }
            stringSet.add(value.toString());
        }

        return stringSet.size();
    }
}
