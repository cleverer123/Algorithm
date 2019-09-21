class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        left = 0
        right = 0
        def back_track(item, left, right):
            if left == n and right == n:
                res.append(item)
                return 

            if left < n:
                back_track(item + '(', left + 1, right)
                
            if left > right:
                back_track(item + ')', left, right + 1)
            

        back_track('', left, right)
        return res
    

        

if __name__ == '__main__':
    print(Solution().generateParenthesis(2))