class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = []
        item = []
        
        res.append(item)

        def generate(i, nums, item, res):
            if i >= len(nums):
                return    

            new_item = item.copy()
            new_item.append(nums[i])
            if not new_item in res:
                res.append(new_item)
            generate(i+1, nums, new_item, res)
            
            generate(i+1, nums, item, res)

        generate(0, nums, item, res)
        return res

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = []
        item = []


        def dfs(start, valuelist):
            res.append(valuelist)
            if start >= len(nums):
                return            
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, valuelist + [nums[i]])  

        dfs(0,[])
        return res

if __name__ == "__main__":
    
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))