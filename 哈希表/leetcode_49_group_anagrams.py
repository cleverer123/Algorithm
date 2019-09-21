class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        word_map = {}
        for s in strs:
            k = ''.join(sorted(s))
            word_map[k] = word_map.get(k, []) + [s]
        res = []
        for v in word_map.values():
            res.append(v)

        return res

if __name__ == '__main__':
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(s))
