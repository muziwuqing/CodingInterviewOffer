package quick;

import java.util.Arrays;

public class quick{
    public static void quickSort(int []nums, int left, int right){
        if (left >= right){
            return;
        }
        int i = left - 1;
        int j = right + 1;
        int x = nums[left];
        while (i < j) {
            while (nums[++i] < x);
            while (nums[--j] > x);
            if (i < j) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }
        }
        quickSort(nums, left, j);
        quickSort(nums, j+1, right);
    }
    public static void main(String[] args) {
        int []nums = {2, 4, 3, 6, 5};
        quickSort(nums, 0, nums.length-1);
        System.out.println(Arrays.toString(nums));
    }
}