from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        counter_s1 = Counter(s1)
        left, right = 0, 0
        for left in range(len(s2) - len(s1) + 1):
            

            while right < left + len(s1) and counter_s1[s2[right]] >=  1:
                counter_s1[s2[right]] -= 1
                right += 1

            if right == left + len(s1):
                return True
            
            counter_s1[s2[left]] += 1
        
        return False

    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        dic1 = [0] * 26
        dic2 = [0] * 26

        for i in range(len(s1)):
            dic1[ord(s1[i]) - ord('a')] += 1
            dic2[ord(s2[i]) - ord('a')] += 1
        
        if dic1 == dic2:
            return True
        
        for i in range(len(s1), len(s2)):
            dic2[ord(s2[i - len(s1)]) - ord('a')] -= 1
            dic2[ord(s2[i]) - ord('a')] += 1
            if dic1 == dic2:
                return True
        return False


    # 此写法超时不通过，应是line 65 占用时间。此写法简洁便于理解。
    def checkInclusion3(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        start, end = 0, 0
        while end <= len(s2):
            while len(s2[start: end]) >= len(s1):
                if Counter(s2[start: end]) == Counter(s1):
                    return True
                start += 1
            end += 1
        return False



s1 = "ab"
s2 = "eidbaooo"
# s1 = "ab"
# s2 = "a"
s1 = "adc"
s2 = "dcda"


print(Solution().checkInclusion(s1, s2))