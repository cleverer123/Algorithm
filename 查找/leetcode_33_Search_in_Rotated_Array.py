class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
    
        while begin <= end:
            mid = (begin + end) // 2
            if target == nums[mid] :
                return mid
            
            if target < nums[mid]:  
                if nums[begin] < nums[mid]:
                    if target >= nums[begin]:
                        end = mid - 1
                    else:
                        begin = mid +1
                elif nums[begin] > nums[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1

            elif target > nums[mid]:
                if nums[begin] < nums[mid] :
                    begin = mid + 1
                elif nums[begin] > nums[mid]:
                    if target >= nums[begin]:
                        end = mid -1
                    else:
                        begin = mid + 1
                else:
                    begin = mid + 1
        
        return -1


        

if __name__ == '__main__':
    # test = [7,9,12,15,20,1,3,6]
    test = [5,1,3]
    sol = Solution()

    for i in range(6):
        print(sol.search(test, i))

            
                    