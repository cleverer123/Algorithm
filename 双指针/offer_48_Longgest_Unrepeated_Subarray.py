from collections import defaultdict
class Solution(object):
    def findLonggestUnrepeatedSubarray(self, s):
        if len(s) <= 1:
            return len(s)
        counter = defaultdict(int)
        res = 0
        cnt = 0
        left = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            cnt += 1
            while counter[s[right]] > 1:
                cnt -= 1
                counter[s[left]] -= 1 
                left += 1
            res = max(res, cnt)
            
        # if cnt == len(s):
        #     res = cnt
        return res

s = "abcabcbb" 
# s = 'au'
# s = "aab"    
print(Solution().findLonggestUnrepeatedSubarray(s))
        