
/*
ID: imehedi2
LANG: C++
TASK: milk2
*/

#include <bits/stdc++.h>

using namespace std;

void solve(){
    int n;
    cin>>n;
    vector<vector<int>> v;
    while(n--){
        int m,n;
        cin>>m>>n;
        v.push_back({m,n});
    }
    cout << v[0][0] << endl;
}

int main(){
   // freopen("milk2.in", "r", stdin);
   // freopen("milk2.out", "w", stdout);
    solve(); 
    return 0;
}

