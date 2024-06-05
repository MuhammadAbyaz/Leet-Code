#include <iostream>
#include <set>
#include <vector>
// bool containsDuplicate(vector<int> &nums)
// {
//     unordered_set<int> numsSet;
//     for (int i = 0; i < nums.size(); i++)
//     {
//         numsSet.insert(nums[i]);
//     }
//     return !(nums.size() == numsSet.size());
// }
bool containsDuplicate(vector<int> &nums)
{
    std::set<int> s(nums.begin(), nums.end());
    return !(s.size() == nums.size());
}