#include <iostream>
#include <vector>
using namespace std;

int dfs(int m, int n, int k, vector<vector<bool>> &visited, int i, int j);
int getDigitSum(int num);
int movingCount(int m, int n, int k);
bool check(int m, int n, int k, vector<vector<bool>> &visited, int i, int j);

int main() {
    int m = 2, n = 3, k = 1;
    int res = movingCount(m, n, k);
    cout<<res<<endl;
    system("pause");
    return 0;
}

int movingCount(int m, int n, int k) {
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    return dfs(m, n, k, visited, 0, 0);
}

int dfs(int m, int n, int k, vector<vector<bool>> &visited, int i, int j) {
    int res = 0;
    if(check(m, n, k, visited, i, j)){
        visited[i][j] = true;
        res = 1 + dfs(m, n, k, visited, i+1, j) + dfs(m, n, k, visited, i, j+1);
    }
    return res;
}

bool check(int m, int n, int k, vector<vector<bool>> &visited, int i, int j){
    if(0<=i && i<m && 0<=j && j<n && !visited[i][j] && getDigitSum(i) + getDigitSum(j)<=k){
        return true;
    }   
    return false;
}

int getDigitSum(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}