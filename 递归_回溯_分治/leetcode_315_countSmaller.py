class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.count = {i : 0 for i in range(len(nums))}
        nums = [ [nums[i], i] for i in range(len(nums))]

        self.merge_sort(nums)

        return [self.count[i] for i in range(len(nums))]

    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])        

        return self.merge(left, right)
    
    def merge(self, nums1, nums2):
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] <= nums2[j][0]:
                self.count[nums1[i][1]] += j              
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        for ii in range(i, len(nums1)):
            self.count[nums1[ii][1]] += j
            res.append(nums1[ii])
        for jj in range(j, len(nums2)):
            res.append(nums2[jj])

        return res
 
if __name__ == '__main__':
    print(Solution().countSmaller([5, -7, 9, 1, 3, 5, -2, 1]))