class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        arr.sort()
        m = arr[(len(arr) - 1) / 2]
        l, r = 0, len(arr) - 1
        res = []
        while k > 0:
            if abs(arr[l] - m) > abs(arr[r] - m):
                res.append(arr[l])
                l += 1               
            else:
                res.append(arr[r])
                r -= 1
            k -= 1
        return res
                