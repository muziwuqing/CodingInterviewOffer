package insert;

import java.util.Arrays;

public class insert {
    public static void insertSort(int []nums){
        for (int i=1; i < nums.length; i++){
            int j = i-1;
            int num = nums[i];
            for (; j>=0 && nums[j]>num; j--){
                nums[j+1] = nums[j];
            }
            nums[j+1] = num;
        }
    }
    public static void main(String[] args) {
        int []nums = {2, 4, 6, 1, 5, 3};
        insertSort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
