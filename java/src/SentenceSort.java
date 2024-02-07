public class SentenceSort {
    public String sortSentence(String s) {
        String[] strArray = s.split(" ");
        Character c;
        String[] resArray = new String[strArray.length];
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < strArray.length; i++) {
            c = strArray[i].charAt(strArray[i].length() - 1);
            resArray[Integer.parseInt(Character.toString(c)) - 1] = strArray[i];
        }
        for (String word : resArray) {
            c = word.charAt(word.length() - 1);
            word = word.replace(c.toString(), "");
            res.append(word).append(" ");
        }

        return res.toString().trim();
    }
}
