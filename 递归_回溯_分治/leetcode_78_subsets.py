class Solution(object):
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

        

class Solution2:
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

if __name__ == '__main__':
    s = Solution2()
    input = [1,2,3]
    print(s.subsets(input)) 