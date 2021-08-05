#include <iostream>
using namespace std;

string replaceSpace(string s){
    int count = 0;
    int sOldSize = s.size();
    for (int i=0; i<sOldSize; i++) {
        if (s[i] == ' ') count++;
    }
    s.resize(sOldSize + count * 2);
    int sNewSize = s.size();
    for (int i = sNewSize - 1, j = sOldSize - 1; j < i; i--, j--) {
        if (s[j] != ' ') {
            s[i] = s[j];
        } else {
            s[i] = '0';
            s[i - 1] = '2';
            s[i - 2] = '%';
            i -= 2;
        }
    }
    return s;
}

int main(){
    string s = "we are happy";
    string res = replaceSpace(s);
    cout<<res<<endl;
    system("pause");
    return 0;
}