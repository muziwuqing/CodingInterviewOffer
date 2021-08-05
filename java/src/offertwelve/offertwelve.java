package offertwelve;

public class offertwelve{
    private static boolean[][] visited;
    public static boolean exist(char[][] board, String word){
        int m = board.length, n = board[0].length;
        visited = new boolean[m][n];
        char[] words = word.toCharArray();
        boolean res = false;
        int cur = 0;
        for (int i = 0; i<m; i++){
            for (int j = 0; j<n;j++){
                res = helper(board, words, cur, i, j);
                if (res == true) return true;
            }
        }
        return false;
    }

    public static boolean helper(char[][] board, char[] word, int cur, int i, int j){
        if (cur == word.length) return true;
        if (i<0 || i>board.length-1 || j<0 || j>board[0].length-1 || visited[i][j] || board[i][j] != word[cur]) return false;
        visited[i][j] = true;
        cur++;
        boolean res = helper(board, word, cur, i+1, j) || 
                    helper(board, word, cur, i-1, j) || 
                    helper(board, word, cur, i, j+1) ||
                    helper(board, word, cur, i, j-1);
        visited[i][j] = false;
        return res;
    }
    public static void main(String[] args) {
        char[][] board = new char[][] {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        String word = "ABCCED";
        boolean res = exist(board, word);
        System.out.println(res);
    }
}