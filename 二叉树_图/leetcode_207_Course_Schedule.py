class GraphNode(object):
    def __init__(self, x):
        self.val = x
        self.neighbors = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        vist = [-1 for i in range(numCourses)] #-1:未被访问。 0：正在访问 1：已访问完成
        graph = [GraphNode(i) for i in range(numCourses)]

        for preq in prerequisites:
            graph[preq[1]].neighbors.append(graph[preq[0]])

        def dfs(node):

            vist[node.val] = 0

            for neigh in node.neighbors:
                if vist[neigh.val] == -1:
                    if not dfs(neigh):
                        return False 
                elif vist[neigh.val] == 0:
                    return False

            vist[node.val] = 1
            return True
        
        for i in range(numCourses):
            
            if vist[i] == -1 and not dfs(graph[i]):
                return False

        return True


class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        degree = [0 for i in range(numCourses)]
        graph = [GraphNode(i) for i in range(numCourses)]

        for preq in prerequisites:
            graph[preq[1]].neighbors.append(graph[preq[0]])
            degree[preq[0]] += 1 # 入度加1
        
        queue = []
        for i in range(numCourses):
            if not degree[i]:
                queue.append(graph[i]) 
        

        while len(queue) > 0:
            node = queue.pop(0)
            for neigh in node.neighbors:
                degree[neigh.val] -= 1
                if degree[neigh.val] == 0: 
                    queue.append(neigh)

        for d in degree:
            if d > 0:
                return False
        
        return True

# 2023-04-27
class Solution3(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        解体思路：首先遍历prerequisites得到每个课程的入度（有前驱课程<第一个元素>加1），以及每个课程的所有后继（第一个元素是第二个元素的后继），
        通过维护一个入度为零的课程栈实现图的遍历：
            遍历入度表，将其中为0的课程id入栈。
            如果栈不为空，弹出栈（模拟学完该课程），这时候记录count+1，该课程的所有后继的入度-1，同时判断这些后继课程的入度是否变为0，若为零则入栈。
        """

        inDegrees = [0] * numCourses
        next = [ [] for _ in range(numCourses) ]
        # next = {}
        for pres in prerequisites:
            inDegrees[ pres[0] ] += 1 
            next[ pres[1] ].append( pres[0] )
            
        
        stack = []

        for i in range(numCourses):
            if inDegrees[i] == 0:
                stack.append(i)
        
        count = 0

        while len(stack):
            i = stack.pop()
            count += 1

            for post in next[i]:
                inDegrees[post] -= 1
                if inDegrees[post] == 0:
                    stack.append(post)
        
        return count == numCourses

if __name__ == '__main__':       
    num = 3
    # l = [[1,2],[0,1],[2,0]]
    l = [[0,1], [0,2], [1,2]]
    print(Solution3().canFinish(num, l))






            
