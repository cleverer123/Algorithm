from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = [0] * 26

        left = 0
        maxseen = 0
        for right, c in enumerate(s):
            counter[ord(c) - ord('A')] += 1

            maxseen = max(maxseen, counter[ord(c) - ord('A')])

            while right - left + 1 - maxseen > k:
                
                counter[ord(s[left]) - ord('A')] -= 1
                left += 1
            
        return right - left + 1

s = "ABAB"
k = 2
print(Solution().characterReplacement(s,k))