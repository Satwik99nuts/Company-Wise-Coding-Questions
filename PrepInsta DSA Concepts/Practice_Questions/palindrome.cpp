#include<bits/stdc++.h>
using namespace std;

// normal methods- two pointers
int bool_pal(string c){
    int left = 0;
    int right = c.size() - 1;

    while(left<right){
        if(c[left]!=c[right]){
            return false;
        }
        left++;
        right--;
    }
    return true;
}

// ---------------using recursion------------------
bool isPalOrNot(string &s,int left , int right){
    if(left<=right){
        return true;
    }
    if(s[left]!=s[right]){
        return false;
    }
    return isPalOrNot(s,left+1,right-1);
}
bool isPalOrNot(string s){
    return isPalOrNot(s,0,s.length()-1);
}
// -------------------------------------------------
int main(){
    string x; 
    cout<<"Write the string to check = "<<endl;
    cin>>x;
    cout<<bool_pal(x);
    return 0;
}