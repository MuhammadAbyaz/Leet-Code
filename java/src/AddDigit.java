public class AddDigit {
    public int addingDigit(int num) {
        int res = 0;
        if (num >= 10) {
            res += num % 10;
            res += num / 10;
            num = res;
        }
        return res;
    }
}
