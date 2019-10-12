from collections import defaultdict
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        charmap = defaultdict(lambda: 0)

        for i in range(len(s)):
            charmap[s[i]] += 1

        for i in range(len(s)):
            if charmap[s[i]] == 1:
                return i
            
        return -1