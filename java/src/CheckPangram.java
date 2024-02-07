import java.util.HashSet;

public class CheckPangram {
    public boolean checkIfPangram(String sentence) {
        char[] charArray = sentence.toCharArray();
        HashSet<Character> alphabetSet = new HashSet<>();
        boolean res;
        for (Character c :
                charArray) {
            alphabetSet.add(c);
        }
        res = alphabetSet.size() == 26;
        return res;
    }
}
