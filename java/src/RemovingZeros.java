public class RemovingZeros {
    public String removingTrailingZeros(String num) {
        char[] charArray = num.toCharArray();
        StringBuilder res = new StringBuilder();
        res.append(num);
        for (int i = charArray.length - 1; i >= 0; i--) {
            if (charArray[i] != '0') {
                break;
            } else if (charArray[i] == '0') {
                res.setCharAt(i, ' ');
            }
        }
        return res.toString().trim();
    }
}
