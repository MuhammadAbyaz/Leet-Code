public class ToLowerCase {
    public String toLower(String s) {
        char character;
        int charValue;
        StringBuilder res = new StringBuilder();
        for (char c: s.toCharArray()) {
            charValue = c;
            if (charValue>=65 && charValue<=90){
                charValue+=32;
                character = (char) charValue;
                res.append(character);
            }
            else {
                res.append(c);
            }
        }
        return res.toString();
    }
}
