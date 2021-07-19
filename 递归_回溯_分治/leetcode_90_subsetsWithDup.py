# 递归
class Solution0(object):
    def subsetsWithDup(self, nums):
        res = []
        if not nums:
            return [[]]
        res = self.subsetsWithDup(nums[1:])
        return res + [[nums[0]] + s for s in res if [nums[0]] + s not in res]

# 回溯
class Solution1(object):
    def subsetsWithDup(self, nums):
        res = []
        self._subsetsWithDup(nums, 0, list(), res)
        return res

    def _subsetsWithDup(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if index < i and nums[i] == nums[i-1]:
                continue
            self._subsetsWithDup(nums, i + 1, path + [nums[i]], res)
        
# 回溯
class Solution3(object):
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

# 深度优先
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        res = []

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
    print(Solution0().subsetsWithDup(nums))