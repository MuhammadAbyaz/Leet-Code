public class ReverseWord {
    public String reversingWord(String s) {
        StringBuilder res = new StringBuilder();
        StringBuilder value = new StringBuilder();
        for (String word : s.split(" ")) {
            value.append(word);
            res.append(value.reverse()).append(" ");
            value = new StringBuilder();
        }
        return res.toString().trim();
    }
}
