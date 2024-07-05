#include <bits/stdc++.h>
#define DEBUG 1

using namespace std;

void solve(){
    string id;
    cin>>id;

    for(char ch in id) {
        cout << ch << endl;
    }

}


int main(){
    ifstream fileSource("dict.txt");
    if(!fileSource){
        cerr << "Error" << endl;
        exit(-1);

    }
    string buff;
    vector<string> vs; 
    while(fileSource >> buff ){
        vs.push_back(buff);    
    }

    return 0;
}

