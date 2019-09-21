class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def left_bound(nums):
            begin = 0
            end = len(nums) - 1
            while begin <= end :
                mid = (begin + end) // 2
                if target == nums[mid]:
                    if mid == 0 or target > nums[mid - 1]:
                        return mid
                    else:
                        end = mid - 1
                elif target < nums[mid]:
                    end = mid - 1
                else: 
                    begin = mid + 1 
            return -1

        def right_bound(nums):
            begin = 0
            end = len(nums) - 1
            while begin <= end :
                mid = (begin + end) // 2
                if target == nums[mid]:
                    if mid == len(nums) - 1 or target < nums[mid + 1]:
                        return mid
                    else:
                        begin = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else: 
                    begin = mid + 1   
            return -1    
        res = []
        res.append(left_bound(nums))
        res.append(right_bound(nums))
        return res

if __name__ == '__main__':
    test = [5,7,7,8,8,8,10]
    sol = Solution()

    for i in range(11):
        print(sol.searchRange(test, i))





