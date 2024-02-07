public class TwoSum {
    public int [] twoSum(int[] nums, int target){
        int [] pos = null;
        int i = 0;
        while (i <= (nums.length + 1)) {
            for (int k = i+1; k < nums.length; k++) {
                if (nums[i] + nums[k] == target) {
                    pos = new int[]{i, k};
                    break;
                }
            }
            if (pos == null){
                i++;
            }
            else break;
        }
        return pos;
    }

}
