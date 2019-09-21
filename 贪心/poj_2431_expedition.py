class Solution1:
    def expediton(self, L, P, stop_pairs):
        """
        :type L: int
        :type P: int
        :type pairs: List(List(2)) [加油站到终点的距离， 加油站汽油量]
        :rtype: int
        """
        self.maxHeap = []
        stop_pairs.append([0, 0])
        stop_pairs = sorted(stop_pairs, key={lambda x : x[0]}, reverse=True)
        
        add = 0

        for pair in range(len(stop_pairs)):
            d = L - pair[0]
            while len(self.maxHeap) > 0 and P < d :
                P += self.maxHeapPop()
                add += 1
            if len(self.maxHeap) == 0 and P < d:
                return -1
            P -= d

            L = pair[0]
            self.maxHeapAdd(pair[1])

        return add

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        


            






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