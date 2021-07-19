# 递归 
class Solution0(object):
    def subsets(self, nums):
        res = []
        if not nums:
            return [[]]
        res = self.subsets(nums[1:])
        return res + [[nums[0]] + s for s in res]

# 回溯
class Solution1(object):
    def subsets(self, nums):
        res = list()
        self._subsets(nums, 0, list(), res)
        return res

    def _subsets(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self._subsets(nums, i + 1, path + [nums[i]], res)

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        item = []
        res.append(item)

        def generate(i, nums, item, res):
            if i >= len(nums):
                return    

            new_item = item.copy()
            new_item.append(nums[i])
            res.append(new_item)
            generate(i+1, nums, new_item, res)
            
            generate(i+1, nums, item, res)

        generate(0, nums, item, res)
        return res

        

class Solution3:
    def subsets(self, nums):
        res = []
        all_set = 1 << len(nums)
        for i in range(all_set):
            item = []
            for j in range(len(nums)):
                if 1 << j & i:
                    item.append(nums[j])
                
            res.append(item)
        return res

# 迭代
class Solution4(object):
    def subsets(self, nums):
        res = [[]]

        for num in nums:
            res += [s + [num]  for s in res]    
               
        return res

class Solution5(object):
    def subsets(self, nums):
        
        res = []

        def dfs(index, path):
            res.append(path)
            if index > len(nums):
                return 
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])                

        dfs(0, [])
        
        return res



    
if __name__ == '__main__':
    s = Solution5()
    input = [1,2,3]
    print(s.subsets(input)) 