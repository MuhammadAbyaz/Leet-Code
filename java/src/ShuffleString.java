public class ShuffleString {
    public String shuffleString(String sentence, int [] indices){
        StringBuilder string=new StringBuilder(sentence);
        for(int i=0;i<sentence.length();i++){
            string.setCharAt(indices[i],sentence.charAt(i));
        }
        return String.valueOf(string);
    }
}
