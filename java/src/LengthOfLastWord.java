public class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        String[] stringArray = s.trim().split(" ");
        String lastWord = stringArray[stringArray.length - 1];
        return lastWord.length();

//        String newString = s.trim();
//        StringBuilder lastWord = new StringBuilder();

//        for (int i = newString.length() - 1; i >= 0; i--) {
//            if (newString.charAt(i) == ' ') {
//                break;
//            } else {
////                lastWord.append(newString.charAt(i));
//            }
//        }
//        return lastWord.length();
    }
}
