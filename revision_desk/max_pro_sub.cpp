#include<bits/stdc++.h>
using namespace std;

int MaxSubArrPro(vector<int>&nums){
    int currmax = nums[0];
    int currmin = nums[0];
    int ans = nums[0];
    int n = nums.size();
    for(int i = 0;i<=n;i++){
        if(nums[i]<0){
            swap(currmax,currmin);
        }

        currmax = max(currmax,currmax*nums[i]);
        currmin = min(currmin,currmin*nums[i]);
        ans = max(currmax,ans);
    }
    return ans;
};