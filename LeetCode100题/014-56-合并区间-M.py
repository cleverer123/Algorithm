class Solution:
    def merge(self, intervals) :
        intervals.sort(key=lambda p: p[0])
        ans = []
        for p in intervals:
            if ans and ans[-1][1] >= p[0]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else:
                ans.append(p)
        return ans
    