class GraphNode(object):
    def __init__(self, x):
        self.val = x
        self.neighbors = []

class Solution:
    def graph(self):
        nodes = [GraphNode(i) for i in range(5)]
        nodes[0].neighbors.append(nodes[4])
        nodes[0].neighbors.append(nodes[2])
        nodes[1].neighbors.append(nodes[2])
        nodes[2].neighbors.append(nodes[3])
        nodes[3].neighbors.append(nodes[4])
        nodes[4].neighbors.append(nodes[3])

        for node in nodes:
            print('node', node.val, end=': ')
            for neigh in node.neighbors:
                print(neigh.val, end=' ')
            print('')
        return nodes

    def dfs_graph(self, nodes):

        def dfs(node):

            vist[node.val] = 1
            print(node.val, end='')
            
            for neigh in node.neighbors:
                if vist[neigh.val] == 0:
                    dfs(neigh)

        vist = [0 for i in range(len(nodes)) ]
        for i, node in enumerate(nodes):
            if vist[i] == 0 :
                print('vist node', node.val, end=' : ')
                dfs(node)
                print('')
    
    def bfs_graph(self, nodes):

        vist = [0 for i in range(len(nodes)) ]

        def bfs(root):
            queue = [root]
            while len(queue) > 0:
                node = queue.pop(0)
                print(node.val, end=' ')
                for neigh in node.neighbors:
                    if vist[neigh.val] == 0:
                        queue.append(neigh)
                        vist[neigh.val] =1
                
        
        for i, node in enumerate(nodes):
            if vist[i] == 0 :
                print('vist node', node.val, end=' : ')
                bfs(node)

                print('')

if __name__ == '__main__':
    nodes = Solution().graph()
    Solution().bfs_graph(nodes)
