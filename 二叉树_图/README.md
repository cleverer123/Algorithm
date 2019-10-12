# 二叉树&图

---

## 二叉树的深度遍历
1. 前序遍历：**node**->node.left->node.right
2. 中序遍历：node.left->**node**->node.right
3. 后续遍历：node.left->node.right->**node**

### 1、路径之和
 - 难度： Medium
 - 来源： ***LeetCode 113. Path Sum II***
 - 思路： 前序遍历二叉树，增加路径和，节点入路径栈，当满足路径节点之和与目标相等，且当且节点为叶节点时，即找到一条路径。回溯，路径和减小，路径栈栈顶弹出。

### 2、最近的公共祖先
 - 难度： Medium
 - 来源： ***LeetCode 236. Lowest Common Ancestor of a Binary Tree***
 - 思路： 
    - 1. 找到路径。
    - 2. 在遍历过程中寻找，当p、q，不在同一子树中，比如，p在left左子树，那么右为空，返回左子树的根节点，同样q返回其所在子树的根节点，此时，两子树根节点的父节点即为最近公共祖先。

### 3、二叉树转链表
 - 难度： Medium
 - 来源： ***LeetCode 114. Flatten Binary Tree to Linked List***
 - 思路： 

## 二叉树的层次遍历

   采用队列对所遍历的节点进行存储，每次遍历，弹出队头节点，并将该节点左右子节点加入队列，循环访问。

### 4、侧面观察二叉树
 - 难度： Medium
 - 来源： ***LeetCode 199. Binary Tree Right Side View***
 - 思路： 求层次遍历二叉树时，每一层最后一个节点。

## 图

邻接矩阵；邻接表。

### 5、课程安排

 - 难度： Medium
 - 来源： ***LeetCode 207. Course Schedule***
 - 思路： 检测图中是否有环。深搜法：未访问、正在访问、完成访问。广搜法：入度，入度为0，代表学完了。

 

