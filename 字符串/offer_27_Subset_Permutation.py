class Solution:
    def Permutation(self, ss):
        # write code here
        if ss == '':
            return []
        res = []
        def pem( s, sub):
            if s == '':
                res.append(sub)
                return
            for i in range(len(s)):
                pem( s[:i]+s[i+1:] , sub + s[i])
            
        pem( ss, '')

        return sorted(list(set(res)))

if __name__ == "__main__":
    s = 'abc'
    print(Solution().Permutation(s))

