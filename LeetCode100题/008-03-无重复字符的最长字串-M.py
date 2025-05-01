class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        subs = {}
        res = 0
        while right < len(s):
            if s[right] not in subs:
                subs[s[right]] = 0
            subs[s[right]] += 1
            while left < right and subs[s[right]] > 1:
                subs[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
s = "abcabcbb"
s = " "
print(Solution().lengthOfLongestSubstring(s))   
