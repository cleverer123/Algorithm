class Solution:
    def removeKdigits(self, num, k):
        stack = []
        res = ""
        
        for i in range(len(num)):
            
            while len(stack) > 0 and num[i] < stack[-1] and k >0:
                stack.pop()
                k -= 1               
            if len(stack) != 0 or num[i] != "0" :
                stack.append(num[i])
        
        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1

        if len(stack) == 0 :
            return "0"

        return "".join(stack)
        

if __name__ == '__main__':
    S = Solution()
    num = "10200"
    # num = '1432219'
    k = 3
    print(S.removeKdigits(num, k))     