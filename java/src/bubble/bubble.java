package bubble;

import java.util.Arrays;

public class bubble{
    public static void bubbleSort(int[] nums){
        boolean hasChanged = true;
        for (int i = 0, n = nums.length; i < n - 1 && hasChanged; i++){
            hasChanged = false;
            for (int j = 0; j < n - i - 1; j++){
                if (nums[j] > nums[j+1]){
                    swap(nums, j, j+1);
                    hasChanged = true;
                }
            }
        }
    }

    public static void swap(int[] nums, int i, int j){
        int tmp = nums[j];
        nums[j] = nums[i];
        nums[i] = tmp;
    }
    public static void main(String[] args) {
        int[] nums = {2, 4, 1, 5, 8, 6};
        bubbleSort(nums);
        System.out.println(Arrays.toString(nums));
    }
}