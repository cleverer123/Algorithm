from collections import Counter 
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = [0, float('inf')]
        t_counter = Counter(t)
        valid_cnt = len(t)

        left = 0
        for right in range(len(s)):
            if t_counter[s[right]] > 0:
                valid_cnt -= 1
            t_counter[s[right]] -= 1

            while not valid_cnt:
                if right - left + 1 < res[1] - res[0] + 1:
                    res = (left, right)
                if t_counter[s[left]] == 0:
                    valid_cnt += 1
                t_counter[s[left]] += 1
                left += 1

        return "" if res[1] == float('inf') else s[res[0] : res[1] + 1]

    def minWindow2(self, s, t):
        res = [0, float('inf')]
        counter = [0]*128
        left, right = 0, 0
        valid_cnt = 0
        for c in t:
            counter[ord(c) - ord('a')] += 1
        for right in range(len(s)):
            if counter[ord(s[right]) - ord('a')] > 0 :
                valid_cnt += 1
            counter[ord(s[right]) - ord('a')] -= 1

            while valid_cnt == len(t):
                if right - left < res[1] - res[0]:
                    res = (left, right)
                if counter[ord(s[left]) - ord('a')] == 0:
                    valid_cnt -= 1
                counter[ord(s[left]) - ord('a')] += 1
                left += 1
        return "" if res[1] == float('inf') else s[res[0] : res[1] + 1]   
                




S="DOABECODEBANC"
T="ABC"

print(Solution().minWindow2(S, T))




       