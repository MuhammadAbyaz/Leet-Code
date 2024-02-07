import java.util.Arrays;
import java.util.List;

public class FizzBuzz {
    public List<String> fizzBuzz(int n) {
//        List<String> res = new ArrayList<>();
//        res.add(String.format("%s", 1));
//        for (int i = 2; i <= n; i++) {
//            if (i % 3 == 0 && i % 5 == 0) {
//                res.add("FizzBuzz");
//            } else if (i % 3 == 0) {
//                res.add("Fizz");
//            } else if (i % 5 == 0) {
//                res.add("Buzz");
//            } else {
//                res.add(String.format("%s", i));
//            }
//        }
        String[] res = new String[n];
//        for (int i = 0; i < res.length; i++) {
//            if (i + 1 == 1) {
//                res[i] = "1";
//            } else if ((i + 1) % 3 == 0 && (i + 1) % 5 == 0) {
//                res[i] = "FizzBuzz";
//            } else if ((i + 1) % 3 == 0) {
//                res[i] = "Fizz";
//            } else if ((i + 1) % 5 == 0) {
//                res[i] = "Buzz";
//            } else {
//                res[i] = String.format("%s", (i + 1));
//            }
//        }
        return Arrays.stream(res).toList();

    }
}
