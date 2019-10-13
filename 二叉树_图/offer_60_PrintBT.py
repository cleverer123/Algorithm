class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot :
            return[]
        queue = [pRoot]
        next_queue = []
        res = []
        layer = []
        while len(queue) > 0 or len(next_queue) > 0:
            if len(queue) > 0:
                while len(queue) > 0:
                    node = queue.pop(0)
                    layer.append(node.val)
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)
                res.append(layer)
                layer = []
            if len(next_queue) > 0:
                while len(next_queue) > 0:
                    node = next_queue.pop(0)
                    layer.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(layer)
                layer = []
        
        return res

                
        

