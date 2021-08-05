package offerfour;

public class offerfour{
    public static boolean findNumberIn2DArrays(int [][]matrix, int target){
        if (matrix.length == 0) return false;
        int m = matrix.length, n = matrix[0].length;
        int i = 0, j = n - 1;
        while (i < m && j >= 0) {
            if (matrix[i][j] == target) return true;
            if (matrix[i][j] < target) i++;
            else j--;
        }
        return false;
    }
    public static void main(String[] args) {
        int [][]matrix = {{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
        int target = 13;
        boolean res = findNumberIn2DArrays(matrix, target);
        System.out.println(res);
    }
}