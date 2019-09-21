class Solution:
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
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        res += nums1[i:]
        res += nums2[j:]

        return res



if __name__ == '__main__':
    nums = [5, -7, 9, 8, 1]
    # # m = [(nums[i] , i) for i in range(len(nums)) ]
    # # print(m)
    # nums = [(nums[i] , i) for i in range(len(nums))]
    # print(nums)
    # # m[7] = 2
    # # print(m)
    print(Solution().merge_sort(nums))