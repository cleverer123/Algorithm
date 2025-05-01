from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = Counter(t)
        cnt_subs = Counter()
        ans_left, ans_right = -1, len(s)
        left, right = 0, 0
        while right < len(s):
            cnt_subs[s[right]] += 1
            while cnt_subs >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_right, ans_left = right, left
                cnt_subs[s[left]] -= 1
                left += 1
            right += 1
        return "" if ans_left < 0 else s[left: right + 1]
s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))