
class Solution:
    def checkvalidorder(self, stack, order):
        tmpstack = []
        while len(order) and len(stack):
            tmpstack.append(stack.pop())

            while len(tmpstack) and order[0] == tmpstack[-1] :
                order.pop(0)
                tmpstack.pop()
        if len(tmpstack) > 0 :
            return False
        return True

if __name__ == '__main__':
    stack = [5,4,3,2,1]
    order = [3,1,5,4,2]
    print(Solution().checkvalidorder(stack, order))            
            

