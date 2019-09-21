from collections import defaultdict
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 4:
            return False

        c = sum(nums) 

        if c % 4 :
            return False

        nums = sorted(nums, reverse = True)

        target = c // 4

        edges = defaultdict(lambda:0)


        def back_track(i):
            if i >= len(nums):
                return edges[0] == target and edges[1] == target and edges[2] == target and edges[3] == target

            for j in range(4):
                if edges[j] + nums[i] > target:
                    continue
                edges[j] += nums[i]
                if back_track(i+1):
                    return True
                edges[j] -= nums[i]
            
            return False

        return back_track(0)

if __name__ == "__main__":
    nums =[1,1,2,2,2]
    nums2 = [3,3,3,3,4]
    print(Solution().makesquare(nums2))

            


        
            