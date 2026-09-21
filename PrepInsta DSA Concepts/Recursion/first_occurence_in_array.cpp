#include<bits/stdc++.h>
using namespace std;

int first_find(vector<int> arr,int target, int idx=0){
    if(idx == size(arr)){
        return -1;
    }
    if(arr[idx] == target){
        return idx;
    }
    return first_find(arr,target,idx+1);
}



int main(){
    vector<int> arr = {1,2,3,4,5,4,3,4,5,56,7,8,6,5,4};
    int target = 56;
    cout<<"The first and formost index of the element "<< target <<" is "<<first_find(arr,target);
    return 0;
}