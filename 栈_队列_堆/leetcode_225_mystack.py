from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.help = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.help.append(x)
        while len(self.data) :
            self.help.append(self.data.pop(0))
        
        while len(self.help) :
            self.data.append(self.help.pop(0))
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """       
        return self.data[0]    

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """

        return False if len(self.data) else True



if __name__ == '__main__':
    s = MyStack()
    s.push(0)
    s.push(1)
    s.push(2)
    print(s.pop())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()