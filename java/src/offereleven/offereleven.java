package offereleven;

public class offereleven {
    public static int minArray(int[] numbers){
        int l = 0, r = numbers.length-1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (numbers[mid] > numbers[r]) {
                l = mid+1;
            } else if (numbers[mid] < numbers[l]) {
                r = mid;
            } else {
                r--;
            }
        }
        return numbers[l];
    }
    public static void main(String[] args) {
        int [] numbers = new int[]{4, 5, 1, 2, 3};
        System.out.println(minArray(numbers));
    }
}
