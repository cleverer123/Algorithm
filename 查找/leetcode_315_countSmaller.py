class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.count = 0
        self.left = None
        self.right = None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.reverse()
        print(nums)
        def bst_insert(node, insert_node, count_small):

            if insert_node.val <=  node.val:
                node.count += 1
                if node.left:
                    return bst_insert(node.left, insert_node, count_small)
                else:
                    node.left = insert_node
            else:
                count_small += node.count + 1
                if node.right:
                    return bst_insert(node.right, insert_node, count_small)
                else:
                    node.right = insert_node
            
            return count_small


        if len(nums) == 0 :
            return []
        if len(nums) == 1:
            return [0]   
        
        root = TreeNode(nums.pop(0))
        counts = [0]
        for num in nums:
            
            count_small = bst_insert(root, TreeNode(num), 0)
            counts.append(count_small)

        counts.reverse()
        return counts
import bisect
class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 利用 二分查找来做！
        # 对列表元素倒着挨个插入一个列表构成有序列表，插入时该节点的插入位置即为比该节点小的节点数目
        # 要注意的是，要用bisect_left来找，bisect_left和bisect_right的不同在于对同一数值的元素
        # bisect_left返回左值，bisect_right返回右值
        bssort_res = []
        counts = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            bisect.insort(bssort_res, nums[i])
            counts[i] = bisect.bisect_left(bssort_res, nums[i])
        return counts



if __name__ == "__main__":
    nums = [5,-7,9,1,3,5,-2,1]
    sol = Solution2()
    print(sol.countSmaller(nums))
        


