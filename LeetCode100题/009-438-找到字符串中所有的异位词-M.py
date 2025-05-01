class Solution:
    # 定宽滑动窗口
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        p_cnt, subs_cnt = [0] * 26, [0] * 26
        res = []
        for i in range(len(p)):
            p_cnt[ord(p[i]) - ord('a')] += 1
            subs_cnt[ord(s[i]) - ord('a')] += 1
        
        if subs_cnt == p_cnt:
            res.append(0)
    
        for i in range(0, len(s) - len(p)):
            subs_cnt[ord(s[i]) - ord('a')] -= 1
            subs_cnt[ord(s[i + len(p)]) - ord('a')] += 1
            if subs_cnt == p_cnt:
                res.append(i + 1)

        return res

    # 优化：统计窗口中各字母与p中字母的数量差，
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        res = []
        cnt = [0] * 26
        for i in range(len(p)):
            cnt[ord(s[i]) - 97] += 1
            cnt[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in cnt].count(True)

        if differ == 0:
            res.append(0)
        
        for i in range(len(s) - len(p)):
            if cnt[ord(s[i]) -97] == 1:
                differ -= 1
            elif cnt[ord(s[i]) - 97] == 0:
                differ += 1
            cnt[ord(s[i]) - 97] -= 1

            if cnt[ord(s[i + len(p)]) -97] == -1:
                differ -= 1
            elif cnt[ord(s[i + len(p)]) - 97] == 0:
                differ += 1
            cnt[ord(s[i + len(p)]) - 97] += 1

            if differ == 0:
                res.append(i + 1)
                
        return res

s = "cbaebabacd"
p = "abc"
s = "aa"
p = "bb"
print(Solution().findAnagrams(s, p))
    