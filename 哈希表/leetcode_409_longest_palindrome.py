class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        flag = 0
        char_map = {} 
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        for c in char_map.keys():
            if char_map[c] % 2 == 0:
                count += char_map[c]
            else:
                count += char_map[c] - 1 
                flag = 1
        return count + flag

if __name__ == '__main__':
    sol = Solution()
    s = 'ccd'
    print(sol.longestPalindrome(s))

