#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool search(vector<int> &nums, int target)
{
    sort(nums.begin(), nums.end());
    int lo = 0;
    int hi = nums.size() - 1;
    while (lo < hi)
    {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == target)
            return true;
        else if (nums[mid] < target)
            lo = mid + 1;
        else
            hi = mid - 1;
    }
    return false;
}
int main()
{
    vector<int> s = {4, 5, 6, 7, 0, 1, 2};
    cout << search(s, 8);
    return 0;
}