from collections import Counter, defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        start, end = 0, 0
        res = []
        while end <= len(s):
            while len(s[start : end]) >= len(p):
                if Counter(s[start : end]) ==  Counter(p):
                    res.append(start)
                start += 1
            end += 1
        return res

    def findAnagrams2(self, s, p):
        if len(s) < len(p):
            return []
        counter_p = Counter(p)
        res = []
        left, right = 0, 0
        for left in range(len(s) - len(p) + 1):
            while right < left + len(p) and counter_p[s[right]] >= 1:
                counter_p[s[right]] -= 1
                right += 1
            
            if right == left + len(p):
                res.append(left)

            counter_p[s[left]] += 1
        return res

    def findAnagrams3(self, s, p):
        if len(s) < len(p):
            return []
        counter_p = [0] * 26
        for c in p:
            counter_p[ord(c) - ord('a')] += 1
        res = []
        left, right = 0, 0

        for left in range(len(s) - len(p) + 1):
            while right < left + len(p) and counter_p[ord(s[right]) - ord('a')] >= 1:
                counter_p[ord(s[right]) - ord('a')] -= 1
                right += 1
            
            if right == left + len(p):
                res.append(left)

            counter_p[ord(s[left]) - ord('a')] += 1
        return res

    def findAnagrams4(self, s, p):
        if len(s) < len(p):
            return []
        dic_1 = [0] * 26
        dic_2 = [0] * 26
        res = []
        for i in range(len(p)):
            dic_1[ord(p[i]) - ord('a')] += 1
            dic_2[ord(s[i]) - ord('a')] += 1

        if dic_1 == dic_2:
                res.append(i - len(p) + 1)
        for i in range(len(p), len(s)):
            
            dic_2[ord(s[i - len(p)]) - ord('a')] -= 1
            dic_2[ord(s[i]) - ord('a')] += 1
        
            if dic_1 == dic_2:
                    res.append(i - len(p) + 1)
        return res
        

    def findAnagrams5(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counts = defaultdict(int)
        for letter in p:
            counts[letter] += 1
        
        res = []
        start = 0
        for end, char in enumerate(s):
            counts[char] -= 1
            while counts[char] < 0:
                counts[s[start]] += 1
                start += 1
            if end - start + 1 == len(p):
                res.append(start) 
        return res        

    def findAnagrams6(self, s, p):
        if len(s) < len(p):
            return []
        counter_p = [0] * 26
        for c in p:
            counter_p[ord(c) - ord('a')] += 1
        res = []
        left, right = 0, 0

        for right in range(len(s)):
            counter_p[ord(s[right]) - ord('a')] -= 1
            while counter_p[ord(s[right]) - ord('a')] < 0:
                counter_p[ord(s[left]) - ord('a')] += 1
                left += 1
            
            if right - left + 1 == len(p):
                res.append(left)

        return res

s = "cbaebabacd"
p = "abc"

s = "abcab"
p = "ab"

print(Solution().findAnagrams6(s, p))