#include <bits/stdc++.h>
using namespace std;
int getPowerA(int a){
    return a*a;
}

//void solve(){
int gerPowerB(int b){
    return b*b;
}



int main(){
    //solve();
    int a,b;
    cin>>a>>b;
    int res = getPowerA(a)+getPowerB(b);
    cout<<res;
}