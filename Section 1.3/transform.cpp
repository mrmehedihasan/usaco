
/*
ID: imehedi2
LANG: C++
TASK: transform
*/

#include <bits/stdc++.h>
#define DEBUG 0
using namespace std;

vector<vector<int>> rotate(vector<vector<int>> matrix){
    int N = matrix.size();
    vector<vector<int>> matrix_rotate;
    for(int i=0; i<N; i++){
        vector<int> new_matrix;
        for(int j=N-1; j>=0; j--){
            new_matrix.push_back(matrix[j][i]);
        }
        matrix_rotate.push_back(new_matrix);
    }
    return matrix_rotate;
}

vector<vector<int>> mirror(vector<vector<int>> matrix){
    int N = matrix.size();
    vector<vector<int>> matrix_rotate;
    for(int i=0; i<N; i++){
        vector<int> new_matrix;
        for(int j=N-1; j>=0; j--){
            new_matrix.push_back(matrix[i][j]);
        }
        matrix_rotate.push_back(new_matrix);
    }
    return matrix_rotate;
}

int check(vector<vector<int>> b_mat, vector<vector<int>> a_mat){
    if(rotate(b_mat) == a_mat) {
        return 1;
    }else if(rotate(rotate(b_mat)) == a_mat){
        return 2;
    }else if(rotate(rotate(rotate(b_mat))) == a_mat){
        return 3;
    }else{
        return 0;
    }
}
void solve(){
    //input
    int n;
    cin>>n;
    vector<vector<int>> b_mat;
    for(int i=0; i<n; i++){
        vector<int>tmp;
        for(int j=0; j<n; j++){
            char x;
            cin>>x;
            if(x=='@'){
                tmp.push_back(1); 
            }else{
                tmp.push_back(0);
            }
        }
        b_mat.push_back(tmp);

    }
    vector<vector<int>> a_mat;
    for(int i=0; i<n; i++){
        vector<int>tmp;
        for(int j=0; j<n; j++){
            char x;
            cin>>x;
            if(x=='@'){
                tmp.push_back(1); 
            }else{
                tmp.push_back(0);
            }
        }
        a_mat.push_back(tmp);

    }
    //end input
    
    if(DEBUG){
        for(auto it: a_mat){
            for(auto i: it) {
                cout << i << " "; 
            }
            cout << endl;
        }

        for(auto it: a_mat){
            for(auto i: it) {
                cout << i << " "; 
            }
            cout << endl;
        }

    }
    // check for rotation
    if(check(b_mat, a_mat)) {
        cout << check(b_mat, a_mat) << endl;
        return;
    }
    else if(mirror(b_mat) == a_mat){
        cout << 4 << endl;
        return;
    }else if(check(mirror(b_mat), a_mat) > 0){
        cout << 5 << endl;
        return;
    }else if(a_mat == b_mat){
        cout << 6 << endl;
    }
    else{
        cout << 7 << endl;
        return;
    }

}

int main(){
    freopen("transform.in", "r", stdin);
    freopen("transform.out", "w", stdout);
    solve();
    return 0; 
}

