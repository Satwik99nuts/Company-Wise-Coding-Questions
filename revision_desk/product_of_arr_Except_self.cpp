#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> productofarr(vector<int>&nums){
        int n = nums.size();
        vector<int> ans(n,1);
        for(int i = 0; i < n; i++){
            ans[i] = ans[i-1]*nums[i-1];
        }

        int suffix = 1;
        for(int i = n-2;i>=0;i--){
            suffix = nums[i+1]*suffix;
            ans[i] = ans[i]*suffix;
        }
        return ans;
    }
};