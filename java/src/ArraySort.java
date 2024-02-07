public class ArraySort {

    public int[] sortArrayByParity(int[] nums) {
        int value = 0;
        int[] sortedArray = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                sortedArray[i] = nums[i];
                value = i;
            }
        }
        for (int i = value + 1; i < nums.length; i++) {
            if (nums[i] % 2 != 0) {
                sortedArray[i] = nums[i];
            }
        }
        return sortedArray;
    }
}
