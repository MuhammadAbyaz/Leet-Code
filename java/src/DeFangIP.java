import java.util.Arrays;

public class DeFangIP {
    public String defangIPaddr(){
        String input = "1.1.1.1";
        String[] inputArray = input.split("\\.");
        String res = null;
        for (String s: inputArray) {
            if (res == null) {
                res = s;
            } else {
                res += "[.]" + s;
            }
        }
        return res;
    }
}
