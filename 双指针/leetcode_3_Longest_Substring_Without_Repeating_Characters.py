from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = defaultdict(int)

        start = 0
        res = 0
        for end, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = []
        res = 0
        for c in s:
            while c in seen:
                seen.pop(0)
            seen.append(c)
            res = max(len(seen), res)
        return res



            