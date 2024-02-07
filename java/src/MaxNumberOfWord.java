public class MaxNumberOfWord {

    public int maxNumberOfWord(String [] sentence){
        int res = 0;
        int numberOfWords = 0;
        for (String s : sentence) {
            for (String words: s.split(" ")) {
                numberOfWords++;
            }
            res = Math.max(res, numberOfWords);
            numberOfWords = 0;
        }
        return res;
    }
}
