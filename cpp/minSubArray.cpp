#include <iostream>
#include <math.h>
#include <vector>
using namespace std;
int minSubArrayLen(int target, vector<int> &nums)
{
    int res = INT_MAX;
    int total = 0;
    int lo = 0;
    for (int hi = 0; hi < nums.size(); hi++)
    {
        total += nums[hi];
        while (total >= target)
        {
            res = min(res, hi - lo + 1);
            total -= nums[lo++];
        }
    }
    return res == INT_MAX ? 0 : res;
}
int main()
{
    vector<int> v = {2, 3, 1, 2, 4, 3};
    std::cout << minSubArrayLen(7, v);
    return 0;
}