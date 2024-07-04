
/*
ID: imehedi2
LANG: C++
TASK: milk2
*/


#include <bits/stdc++.h>
using namespace std;

const int debug = 0;

void solve(){
    int n;
    cin>>n;
    vector<vector<int>> v;
    while(n--){
        int m,n;
        cin>>m>>n;
        v.push_back({m,n});
    }
    sort(v.begin(), v.end());
    vector<vector<int>> v2;  
    vector<int> first = v[0];
    for(int i=1; i<v.size(); i++){
        if(v[i][0] <= first[1]){
            if(v[i][1]>first[1]) {
                first[1] = v[i][1];
            }     
        }else{
            v2.push_back(first);
            first = v[i];
        }
    }
    v2.push_back(first);
    if(debug) {
        cout << "Debug" << endl;
        for(auto it: v2){
            cout <<it[0] << " " << it[1] << endl;
        }

        cout << "end Debug" << endl;
    }

    int mx = 0;
    int mn = 0;
    for(auto it: v2){
        mx = max(it[1] - it[0], mx);
    }
    cout << mx << " ";
    if(v2.size() == 0){
        cout << 0 << endl;
        return;
    }
    int last = v2[0][1];
    for(int i=1; i<v2.size(); i++){
        int d = v2[i][0] - last;
        mn = max(d, mn);
        last = v2[i][1];
    }
    cout << mn << endl;
}

int main(){
    freopen("milk2.in", "r", stdin);
    freopen("milk2.out", "w", stdout);
    solve(); 
    return 0;
}
