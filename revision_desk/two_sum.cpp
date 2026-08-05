#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
    vector<int> twosum(vector<int>&nums,int target){
        unordered_map<int,int> mp;

        for(int i = 0;i<nums.size();i++){
            int need = target - nums[i];
            if (mp.find(need) != mp.end())
            {
                return {mp[need], i};
            }

            mp[nums[i]] = i;
        }
        return {};
    }
};
int main()
{
    Solution s;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> ans = s.twoSum(nums, target);

    cout << ans[0] << " " << ans[1];

    return 0;
}

// This is a **Two Sum** solution using a hash map.

// ```cpp
// #include <bits/stdc++.h>
//     using namespace std;
// ```

// `bits / stdc++.h` includes most common C++ libraries. `using namespace std;
// ` lets you write `vector` instead of `std::vector`.

// ```cpp class Solution
// {
// public:
//     ```

//         This defines a class named `Solution`. `public` means the function below can be called from outside the class.

// ```cpp
//             vector<int>
//             twosum(vector<int> &nums, int target)
// ```

//         This function takes :

// ```cpp
//         nums
// ```

//         a list of numbers,
//         and

// ```cpp
//         target
// ```

//         the sum you want.

//         It returns a `vector<int>` containing the two indices whose values add up to `target`.

// ```cpp
//         unordered_map<int, int> mp;
//     ```

//         This creates a hash map.

//         It stores :

// ```cpp
//             number->index
// ```

//         For example,
//         if `nums[0] = 2`, then later it may store :

// ```cpp mp[2] = 0;
//     ```

//         Now the loop :

// ```cpp for (int i = 0; i < nums.size(); i++)
// ```

//         This checks every element in the array.

// ```cpp int need = target - nums[i];
//     ```

//         This calculates the number needed to complete the sum.

//         Example :

// ```cpp
//             target = 9 nums[i] = 7 need = 9 - 7 = 2
// ```

//                                                       So now we check if `2` appeared earlier.

// ```cpp if (mp.find(need) != mp.end())
// ```

//                                                       This means : “Is `need` already present in the map
//                                                       ?”

//                                                       If yes
//                                                       :

// ```cpp return {mp[need], i};
//     ```

//         Return the earlier index and current index.

//         Example :

// ```cpp
//             nums = {2, 7, 11, 15} target = 9
// ```

//         At `i = 0`,
//             number is `2`.Store `2->0`.

//             At `i = 1`,
//             number is `7`.Need is `2`.

// `2` is already in the map, so return :

// ```cpp{0, 1}
// ```

//         Then :

// ```cpp mp[nums[i]] = i;
//     ```

//         If no pair was found yet,
//         store the current number and its index.

//         Finally :

// ```cpp return {};
//     ```

//         If no answer exists,
//         return an empty vector.

//         Time complexity : `O(n)` Space complexity : `O(n)`