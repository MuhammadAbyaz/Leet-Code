import java.util.Arrays;

public class ReverseString {
    public void reverseString(char[] s) {
        char temp;
        for (int i = 1; i <= s.length / 2; i++) {
            temp = s[i - 1];
            s[i - 1] = s[s.length - i];
            s[s.length - i] = temp;
        }
        System.out.println(Arrays.toString(s));
    }
}
