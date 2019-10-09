class Solution:
    def GetNumberOfK(self, data, k):
        # write code here

        left = self.find_left(data, k)
        right = self.find_right(data, k)
        if left == -1:
            return 0
        return right - left + 1

    def find_left(self, data, k):
        i = 0
        j = len(data) - 1
        while i <= j:
            mid = (i + j) // 2
            if k == data[mid]:
                if mid == 0 or k > data[mid-1]:
                    return mid 
                else:
                    j = mid -1
            elif k < data[mid] :
                j = mid - 1 
            else: 
                i = mid + 1
        
        return -1
       
    def find_right(self, data, k):
        i = 0
        j = len(data) - 1
        while i <= j:
            mid = (i + j) // 2
            if k == data[mid]:
                if mid == len(data) - 1  or k < data[mid+1]:
                    return mid 
                else:
                    i = mid + 1
            elif k < data[mid] :
                j = mid - 1 
            else: 
                i = mid + 1
            
        return -1


if __name__ == "__main__":
    nums = [1,2,3,4,4,4,5,6]
    print(Solution().GetNumberOfK(nums, 4))