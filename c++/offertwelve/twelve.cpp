#include <iostream>
#include <vector>
using namespace std;

int m, n;
bool bfs(vector<vector<char>> &board, string &word, int cur, int i, int j){
    if (i<0 || i>=m || j<0 || j>=n || board[i][j] != word[cur]) return false;
    if (cur == word.size()-1) return true;
    board[i][j] = '\0';
    bool res = bfs(board, word, cur+1, i+1, j) || 
        bfs(board, word, cur+1, i-1, j) || 
        bfs(board, word, cur+1, i, j+1) || 
        bfs(board, word, cur+1, i, j-1);
    board[i][j] = word[cur];
    return res;
}

bool exist(vector<vector<char>> &board, string &word){
    if (board.size() == 0) return false;
    m = board.size(), n = board[0].size();  
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if (board[i][j] == word[0] && bfs(board, word, 0, i, j)) return true;
        }
    }
    return false;
}

int main(){
    vector<vector<char>> board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    string word = "ABCCED";
    bool res = exist(board, word);
    cout<<res<<endl;
    system("pause");
    return 0;
}