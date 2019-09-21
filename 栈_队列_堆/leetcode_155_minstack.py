class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.mins) == 0 :
            self.mins.append(x)
        else:            
            self.mins.append(min(x, self.mins[-1]))

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()
        
    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]

if __name__ == '__main__':
    data = [3,4,5,6,7]
    