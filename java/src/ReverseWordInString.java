public class ReverseWordInString {
    public String wordReversing(String s) {
        StringBuilder reversedString = new StringBuilder();
        String[] stringArray = s.split(" ");
        for (int i = stringArray.length - 1; i >= 0; i--) {
            if (!stringArray[i].isEmpty()) {
                reversedString.append(stringArray[i]).append(" ");
            }
        }
        return reversedString.toString().trim();
    }
}
