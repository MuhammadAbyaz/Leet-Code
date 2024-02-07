public class JewelsInStones {
    public int numberOfJewels(String jewels, String stones) {
        int count = 0;
        StringBuilder str = new StringBuilder();
        str.append(jewels);
        for (Character stone : stones.toCharArray()) {
            if (str.toString().contains(String.valueOf(stone))) count++;
        }
        return count;
    }
}
