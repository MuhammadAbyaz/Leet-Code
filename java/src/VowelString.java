// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

public class VowelString {
    boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    public int countVowel(String[] words, int left, int right) {
        int count = 0;
        for (int i = left; i <= right; i++) {
            count += isVowel(words[i].charAt(0)) && isVowel(words[i].charAt(words[i].length() - 1)) ? 1 : 0;
        }
        return count;
    }
//    public int vowelStrings(String[] words, int left, int right) {
//        int count = 0;
//        char[] vowelArray = {'a', 'e', 'i', 'o', 'u'};
//        for (int i = left; i <= right; i++) {
//            for (Character c : vowelArray) {
//                if (words[i].charAt(0) == c) {
//                    for (Character character : vowelArray) {
//                        if (words[i].charAt(words[i].length() - 1) == character) {
//                            count++;
//                        }
//                    }
//                }
//            }
//        }
//        return count;
//    }

/*    String vowels = "aeiou";
    int count = 0;

        for (int i = left; i <= right; i++) {
        if (vowels.contains(Character.toString(words[i].charAt(0))) && vowels.contains(Character.toString(words[i].charAt(words[i].length() - 1)))) {
            count++;
        }
    }
        return count;*/
}
