class Solution(object):
    def wordPattern(self, pattern, ss):
        """
        :type pattern: str
        :type ss: str
        :rtype: bool
        """
        ss += ' '
        word_map = {}
        word = ''
        pos = 0
        used = {}
        for s in ss:
            if s == ' ':
                if pos == len(pattern):
                    return False
                
                if word in word_map:
                    if word_map[word] != pattern[pos]:
                        return False
                else:
                    if used.get(pattern[pos], 0) == 1:
                        return False 
                    word_map[word] = pattern[pos]
                    used[pattern[pos]] = 1
                
                pos += 1
                word = ''

            else:
                word += s    

        if pos != len(pattern):
            return False
        
        return True

if __name__ == "__main__":
    pattern = "abba"
    ss = "dog cat cat dog"
    print(Solution().wordPattern(pattern, ss))
        

