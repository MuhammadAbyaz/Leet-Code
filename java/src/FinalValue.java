public class FinalValue {
    public int finalValueAfterOperation(String[] operations) {
        int x = 0;
        for (String s : operations) {
            if (s.equals("++X") || s.equals("X++")) {
                x++;
            } else {
                x--;
            }
        }
        return x;
    }
}
