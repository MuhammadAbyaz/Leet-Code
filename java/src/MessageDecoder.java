// https://leetcode.com/problems/decode-the-message/

import java.util.HashMap;

public class MessageDecoder {

    public String decodeTheMessage(String key, String message) {
        HashMap<Character, Character> messageMap = new HashMap<>();
        StringBuilder res = new StringBuilder();
        Character value = 'a';
        for (int i = 0; i < key.length(); i++) {
            if (key.charAt(i) != ' ' && !messageMap.containsKey(key.charAt(i))) {
                messageMap.put(key.charAt(i), value);
                value++;
            }
        }
        for (Character c : message.toCharArray()) {
            if (c != ' ') {
                res.append(messageMap.get(c));
            } else res.append(' ');
        }
        return res.toString();
    }
}
