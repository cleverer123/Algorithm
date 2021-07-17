# [LeetCode - 215. Kth Largest Element in an Array(6种写法(包括BFPRT算法))](https://blog.csdn.net/zxzxzx0119/article/details/81509018)
# 最大堆
class Solution1:
    def findKthLargest(self, nums, k):
        if len(nums) == 0:
            return None
        self.maxheap = []

        for i in range(len(nums)):
            self.maxheap.append(nums[i])
            self.shiftUp(nums[i], i)

        heapSize = len(nums) - 1
        
        for _ in range(k-1):
            self.maxheap[0] = self.maxheap[heapSize]
            heapSize -= 1
            self.shiftDown(0, heapSize)

        return self.maxheap[0]

        
    def shiftUp(self, num, i):        
        while i > 0 and self.maxheap[i] > self.maxheap[( i - 1 ) // 2] :
            self.maxheap[i], self.maxheap[(i - 1) // 2] = self.maxheap[(i - 1) // 2], self.maxheap[i]
            i = ( i - 1 ) // 2
    
    def shiftDown(self, i, heapSize):
        left = 2 * i + 1
        while left < heapSize:
            if (left + 1) < heapSize and self.maxheap[left+1] > self.maxheap[left]:
                maxidx = left + 1  
            else:
                maxidx = left

            if self.maxheap[i] > self.maxheap[maxidx]:
                break

            self.maxheap[i], self.maxheap[maxidx] = self.maxheap[maxidx], self.maxheap[i]
            i = maxidx
            left = 2 * i + 1

    # def maxHeapPop(self):
    #     self.maxHeap[0] = self.maxHeap[-1]
    #     self.maxHeap.remove[-1]
    #     self.maxHeapShiftDown(0, len(self.maxHeap))

# k最小堆
class Solution2:
    def findKthLargest(self, nums, k):
        if len(nums) == 0:
            return None

        self.kHeap = []
        for i in range(k):

            self.kHeap.append(nums[i])
            self.shiftUp(i)

        for i in range(k, len(nums)):
            if nums[i] > self.kHeap[0] :
                self.kHeap[0] = nums[i]
                self.shiftDown(0, k)
            
        return self.kHeap[0]

    def shiftUp(self, i):
        while i > 0 and self.kHeap[i] < self.kHeap[( i - 1 ) // 2] :
            self.kHeap[i], self.kHeap[(i - 1) // 2] = self.kHeap[(i - 1) // 2], self.kHeap[i]
            i = ( i - 1 ) // 2
   
    def shiftDown(self, i, heapSize):  
        left = 2 * i + 1
        while left < heapSize:
            
            if left + 1 < heapSize and self.kHeap[left + 1] < self.kHeap[left] :     
                minidx = left + 1
            else:
                minidx = left
            
            if self.kHeap[i] < self.kHeap[minidx]:
                break
            
            self.kHeap[i], self.kHeap[minidx] = self.kHeap[minidx], self.kHeap[i]

            i = minidx
            left = 2 * i + 1

    # def minHeapPop(self):
    #     self.minHeap[0] = self.minHeap[-1]
    #     self.minHeap.remove[-1]
    #     self.minHeapShiftDown(0, len(self.minHeap))
 
from heapq import *
    


if __name__ == '__main__':
    S = Solution2()

    nums = [3,2,1,5,6,4]
    k = 2
    print(S.findKthLargest(nums, k))