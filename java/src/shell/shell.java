package shell;

import java.util.Arrays;

public class shell {
    public static void shellSort(int []nums){
        int n = nums.length;
        for (int gap = n / 2; gap>0; gap/=2){
            for (int i=gap; i<n; i++){
                int j = i-gap;
                int num = nums[i];
                for (; j >= 0 && nums[j] > num; j-=gap){
                    nums[j+gap] = nums[j];
                }
                nums[j+gap] = num;
            }
        }
    }
    public static void main(String[] args) {
        int []nums = {2, 5, 6 ,3, 1, 4};
        shellSort(nums);
        System.out.println(Arrays.toString(nums));
    }
    
}
