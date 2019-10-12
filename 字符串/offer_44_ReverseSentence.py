class Solution:
    def ReverseSentence(self, s):
        # write code here
        i = 0
        sentence = []
        word = ''
        while i < len(s):
            if s[i] == ' ':
                sentence.insert(0, word)
                word = ''

            else:
                word += s[i]
            i += 1               
        sentence.insert(0, word)
        
        return ' '.join(sentence)

if __name__ == "__main__":
    s = 'student. a am I'
    print(Solution().ReverseSentence(s))

            
