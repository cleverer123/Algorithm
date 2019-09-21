class Solution:
    def calculate(self, s: str) -> int:
        BEGIN = 0
        NUMBER = 1
        OPERATION = 2 
        state = BEGIN

        num = 0
        compute_flag = 0

        num_stack = []
        op_stack = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            
            if  state == BEGIN:
                if s[i] >= '0' and s[i] <= '9':
                    state = NUMBER
                else:
                    state = OPERATION
                i -= 1
                
            elif state == NUMBER:
                if s[i] >= '0' and s[i] <= '9':                    
                    num = num * 10 + int(s[i]) 
                else:
                    num_stack.append(num)
                    if compute_flag == 1:
                        self.compute(num_stack, op_stack)
                    num = 0
                    i -= 1
                    state = OPERATION
                
            elif state == OPERATION:
                if s[i] =='+' or s[i] == '-':
                    op_stack.append(s[i])
                    compute_flag = 1
                elif s[i] == '(':
                    compute_flag = 0
                    state = NUMBER    
                elif s[i] >= '0' and s[i] <= '9':
                    i -= 1
                    state = NUMBER
                elif s[i] == ')':
                    if len(num_stack) > 1 :
                        self.compute(num_stack, op_stack)
            i += 1
                        
        if num != 0:
            num_stack.append(num)
            if len(num_stack) > 1 :
                self.compute(num_stack, op_stack)
        
        if num == 0 and len(num_stack) == 0:
            return 0

        return num_stack[0]

    def compute(self, num_stack, op_stack):
        n2 = num_stack.pop()
        n1 = num_stack.pop()
        op = op_stack.pop()
        if op == '+':
            num_stack.append(n1 + n2)
        else:
            num_stack.append(n1 - n2)

if __name__ == '__main__':
    S = Solution()
    s = "1"
    print(S.calculate(s))