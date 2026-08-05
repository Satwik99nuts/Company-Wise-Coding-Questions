#include<bits/stdc++.h>
using namespace std;

int maxprofit(vector<int>&prices){
    int max_pro = 0;
    int min_pri = INT_MAX;

    for(int i = 0;i <= prices.size();i++){
        min_pri = min(min_pri,prices[i]);
        max_pro = max(max_pro,prices[i]-min_pri);
    }
    return max_pro;
};