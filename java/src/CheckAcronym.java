import java.util.List;

public class CheckAcronym {

    public boolean isAcronym(List<String> words, String s) {
        StringBuilder isAcronym = new StringBuilder();
        for (String word : words) {
            isAcronym.append(word.charAt(0));
        }
        return s.contentEquals(isAcronym);
    }
}
