import java.util.Arrays;

public class CheckingArray {
    public boolean checkIfArrayEqual(String[] word1, String[] word2) {
        boolean res = false;
        if (Arrays.equals(word1, word2)) {
            res = true;
        }
        return res;
    }
}

