from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        len_word = len(words[0])
        counter_words = Counter(words)
        res = []
        for i in range(len_word):
            counter_tmp = Counter()
            start = i
            for j in range(i, len(s), len_word):
                word = s[j : j + len_word]
                if word in counter_words:
                    counter_tmp[word] += 1
                    
                    while counter_tmp[word] > counter_words[word]:
                        counter_tmp[s[start : start + len_word]] -= 1
                        start += len_word
                    
                    if (j - start) == (len(words) - 1) * len_word:
                        res.append(start)
                else:
                    counter_tmp.clear()
                    start = j + len_word

        return res

s = "barfoothefoobarman"
words = ["foo","bar"]
print(Solution().findSubstring(s, words))

