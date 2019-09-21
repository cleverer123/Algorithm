class Solution1(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates = sorted(candidates)

        sum = 0

        item = []

        def generate(i, candidates, sum, item, res):
            if i >= len(candidates) or sum > target:
                return
            
            sum += candidates[i]

            new_item = item.copy()
            new_item.append(candidates[i])
            if sum == target and not (new_item  in res):
                res.append(new_item)
            generate(i+1, candidates, sum, new_item, res)

            sum -= candidates[i]
            generate(i+1, candidates, sum, item, res)

        generate(0, candidates, sum, item, res)

        return res 

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates = sorted(candidates)

        def generate(target, start, valuelist):
            if target == 0:
                res.append(valuelist)
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    if target < candidates[i]:
                        break
                    generate(target - candidates[i], i + 1, valuelist + [candidates[i]] )

        generate(target, 0, [])    
        return res            

if __name__ == '__main__':
    nums = [10,1,2,7,6,1,5]
    t = 8
    print(Solution().combinationSum2(nums, t))
