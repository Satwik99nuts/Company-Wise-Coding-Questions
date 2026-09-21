#include<bits/stdc++.h>
using namespace std;

int last_find(vector<int>&arr, int target; int index=0){
    // base case
    if(index == size(arr)){
        return -1;
    }
    int rest = last_find(arr,target,index+1);

    if(rest!=-1){
        return rest;
    }

    if(arr[index]==target){
        return index;
    }
    return -1;
}



int main(){
    return 0;
}