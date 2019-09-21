from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        begin = 0

        char_map_s = defaultdict(lambda : 0)
        char_map_t = defaultdict(lambda : 0)
        for tt in t:
            char_map_t[tt] += 1        

        word = ''

        def window_ok():
            for tt in char_map_t.keys():
                if char_map_s[tt] < char_map_t[tt]:
                    return False
            return True

        for i in range(len(s)):
            char_map_s[s[i]] += 1

            while begin < i:
                if char_map_t[s[begin]] == 0: # not s[begin]  in t
                    begin += 1

                elif char_map_s[s[begin]] > char_map_t[s[begin]]:
                        char_map_s[s[begin]] -= 1
                        begin += 1
                else:
                    break

            if window_ok():
                if len(word)==0 or (i - begin + 1 < len(word)):
                    word = s[begin: i+1]
        return word


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    
    print(Solution().minWindow(S, T))            
            


