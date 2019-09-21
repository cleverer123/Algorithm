class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.help = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.help.append(x)

        while len(self.data) :
            self.help.append(self.data.pop(0))

        while len(self.help) :
            self.data.append(self.help.pop(0))

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        return self.data.pop(-1)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.data[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if len(self.data) else True


if __name__ == '__main__':
    s = MyQueue()
    s.push(0)
    s.push(1)
    s.push(2)
    print(s.data)
    print(s.pop())