#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> findAnagrams(string s, string p)
{
    vector<int> res;
    int lo = 0;
    int hi = p.size();
    int sLength = s.size();
    sort(p.begin(), p.end());
    while (hi <= sLength)
    {
        string window = s.substr(lo, hi - lo);
        sort(window.begin(), window.end());
        if (window == p)
        {
            res.push_back(lo);
        }
        hi++;
        lo++;
    }
    return res;
}
int main()
{
    string s = "cbaebabacd";
    string p = "abc";
    vector<int> res = findAnagrams(s, p);
    for (auto &val : res)
    {
        cout << val;
    }
    return 0;
}