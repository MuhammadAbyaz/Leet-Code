public class FaultyKeyBoard {
    public String faultyKeyboard(String s) {
        StringBuilder newString = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == 'i') {
                newString.reverse();
            } else newString.append(c);
        }
        return newString.toString();
    }
}
