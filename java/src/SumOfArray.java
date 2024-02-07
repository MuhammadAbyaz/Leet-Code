public class SumOfArray {
    public void addingArray() {
        int[] num = {1, 2, 3, 4};

        int[] result = new int[4];
        int value = num[0];
        result[0] = value;
        for (int i = 1; i < num.length; i++) {
            value += num[i];
            result[i] = value;
        }

        for (int j : result) {
            System.out.println(j);
        }
    }
}
