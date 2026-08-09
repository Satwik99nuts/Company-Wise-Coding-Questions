#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int max_sub_sum(vector<int>&nums){
        int curr_sum = 0;
        int max_sum = INT_MIN;
        int n = nums.size();

        for(int i =0;i<n;i++){
            curr_sum += nums[i];
            max_sum = max(max_sum,curr_sum);

            if(curr_sum<0){
                curr_sum = 0;
            }
        }
        return max_sum;
    }
};