package offerthirteen;

public class offerthirteen{
    public static int movingCount(int m, int n, int k){
        boolean [][] visited = new boolean[m][n];
        return dfs(m, n, k, visited, 0, 0);
    }

    public static int getDigitSum(int num){
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    public static int dfs(int m, int n, int k, boolean [][] visited, int i, int j){
        int res = 0;
        if (0<=i && i<m && 0<=j && j<n && !visited[i][j] && getDigitSum(i) + getDigitSum(j) <= k) {
            visited[i][j] = true;
            res = 1 + dfs(m, n, k, visited, i+1, j) + dfs(m, n, k, visited, i, j+1);
        }
        return res;
    }

    public static void main(String[] args) {
        int m = 3, n = 2, k = 1;
        int res = movingCount(m, n, k);
        System.out.println(res);
    }
}