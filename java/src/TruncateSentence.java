public class TruncateSentence {
    public String truncateSentence(String s, int k) {
        StringBuilder res = new StringBuilder();
        String[] stringArray = s.split(" ");
        for (int i = 0; i < k; i++) {
            res.append(stringArray[i]).append(" ");
        }
        return res.toString().trim();
    }
}
