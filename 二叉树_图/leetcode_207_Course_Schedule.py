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


class Solution(object):
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


if __name__ == '__main__':       
    num = 3
    # l = [[1,2],[0,1],[2,0]]
    l = [[0,1], [0,2], [1,2]]
    print(Solution().canFinish(num, l))




