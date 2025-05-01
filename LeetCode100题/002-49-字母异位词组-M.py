from typing import List
from collections import defaultdict
class Solution:
    # %68
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            hashtable[key].append(word)
        return list(hashtable.values())

    # %99
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in hashtable:
                hashtable[key].append(word)
            else:
                hashtable[key] = [word]
        return list(hashtable.values())
    
    # %18
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            if tuple(counts) in hashtable:
                hashtable[tuple(counts)].append(word)
            else:
                hashtable[tuple(counts)] = [word]
        return list(hashtable.values())
        