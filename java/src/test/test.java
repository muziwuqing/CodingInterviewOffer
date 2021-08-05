package test;

public class test {
    public static void main(String[] args) {
        int m = 4, n = 3;
        boolean [][] a = new boolean[m][n];
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.println(a[i][j]);
            }
        }
    }
}
