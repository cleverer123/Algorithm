class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxHeap) == 0:
            self.maxHeapAdd(num)
            return

        if len(self.maxHeap) > len(self.minHeap):
            if num < self.maxHeap[0]:
                self.minHeapAdd(self.maxHeap[0])
                self.maxHeap[0] = num
                self.maxHeapShiftDown(0, len(self.maxHeap))
            else:
                self.minHeapAdd(num)
        elif len(self.maxHeap) == len(self.minHeap):
            if num < self.minHeap[0]:
                self.maxHeapAdd(num)
            else:
                self.minHeapAdd(num)

        else:
            if num > self.minHeap[0]:
                self.maxHeapAdd(self.minHeap[0])
                self.minHeap[0] = num
                self.minHeapShiftDown(0, len(self.minHeap))
            else:
                self.maxHeapAdd(num)
                          
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0]


    def maxHeapAdd(self, num):
        self.maxHeap.append(num)
        self.maxHeapShiftUp(len(self.maxHeap) - 1)

    def maxHeapShiftUp(self, i):        
        while i > 0 and self.maxHeap[i] > self.maxHeap[( i - 1 ) // 2] :
            self.maxHeap[i], self.maxHeap[(i - 1) // 2] = self.maxHeap[(i - 1) // 2], self.maxHeap[i]
            i = ( i - 1 ) // 2
    
    def maxHeapShiftDown(self, i, heapSize):
        left = 2 * i + 1
        while left < heapSize:
            if left + 1 < heapSize and self.maxHeap[left+1] > self.maxHeap[left]:
                maxidx = left + 1  
            else:
                maxidx = left

            if self.maxHeap[i] > self.maxHeap[maxidx]:
                break

            self.maxHeap[i], self.maxHeap[maxidx] = self.maxHeap[maxidx], self.maxHeap[i]
            i = maxidx
            left = 2 * i + 1

    def minHeapAdd(self, num):
        self.minHeap.append(num)
        self.minHeapShiftUp(len(self.minHeap) - 1)

    def minHeapShiftUp(self, i):
        while i > 0 and self.minHeap[i] < self.minHeap[( i - 1 ) // 2] :
            self.minHeap[i], self.minHeap[(i - 1) // 2] = self.minHeap[(i - 1) // 2], self.minHeap[i]
            i = ( i - 1 ) // 2
   
    def minHeapShiftDown(self, i, heapSize):  
        left = 2 * i + 1
        while left < heapSize:
            
            if left + 1 < heapSize and self.minHeap[left + 1] < self.minHeap[left] :     
                minidx = left + 1
            else:
                minidx = left
            
            if self.minHeap[i] < self.minHeap[minidx]:
                break
            
            self.minHeap[i], self.minHeap[minidx] = self.minHeap[minidx], self.minHeap[i]

            i = minidx
            left = 2 * i + 1

if __name__ == '__main__' :
    obj = MedianFinder()
    obj.addNum(3)
    obj.addNum(2)
    obj.addNum(1)
    obj.addNum(5)
    obj.addNum(6)
    obj.addNum(4)
    print(obj.maxHeap)
    print(obj.minHeap)
    print(obj.findMedian())