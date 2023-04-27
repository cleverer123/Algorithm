RED = 1
GREEN = 2
class Solution(object):

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [-1] * n

        for i in range(0, n):
            if colors[i] == -1 and not self.dfs(graph, i, RED, colors):
                return False
        
        return True

    def dfs(self, graph, node, color, colors):
        if colors[node] != -1:
            return colors[node] == color

        colors[node] = color

        for j in graph[node]:
            if self.dfs(graph, j, GREEN if color == RED else RED, colors) == False:
                return False

        return True

import collections
class Solution2(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n, colored = len(graph), {}
        for i in range(n):
            if i not in colored and graph[i]:
                colored[i] = 1
                q = collections.deque([i])
                while q:
                    cur = q.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            q.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True

if __name__== '__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    # graph = [[1,3],[0,2],[1,3],[0,2]]
    print(Solution2().isBipartite(graph))