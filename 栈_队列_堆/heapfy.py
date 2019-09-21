class MaxHeap(object):
    def __init__(self ):
        self.maxHeap = []

    def maxHeapAdd(self, num):
        self.maxHeap.append(num)
        self.maxHeapShiftUp(len(self.maxHeap) - 1)
    
    def maxHeapPop(self):
        top = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[-1]
        self.maxHeap.remove[-1]
        self.maxHeapShiftDown(0, len(self.maxHeap))
        return top

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