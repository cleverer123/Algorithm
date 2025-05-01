from typing import Optional, List
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visted = [0] * numCourses
        valid = True 

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visted[u] = 1
            for v in edges[u]:
                if visted[v] == 0:
                    dfs(v)
                    if not valid:
                        return 
                elif visted[v] == 1:
                    valid = False
                    return 
            visted[u] = 2
        
        for i in range(numCourses):
            if valid and visted[i] == 0:
                dfs(i)
                if not valid:
                    return False
                
        return valid
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indegree = [0] * numCourses
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indegree[info[0]] += 1

        q = collections.deque([ u for u in range(numCourses) if indegree[u] == 0 ])
        visited = 0
        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        return visited == numCourses