class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_map = {}

        begin = 0
        res = 0
        for i in range(len(s)):
            char_map[s[i]] = char_map.get(s[i], 0) + 1
            if char_map[s[i]] == 1:               
                res = max(i - begin + 1, res)               
            else:
                while char_map[s[i]] > 1:
                    char_map[s[begin]] -= 1
                    begin += 1    
        return res
            

if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))

                

