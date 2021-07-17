# 链表

---

## 反转链表 

### 1 Reverse
 - 难度： Easy
 - 来源： **LeetCode 206. Reverse Linked List**
 - 思路： 首先，备份原表头的后继节点，原表头指向新表头（空节点），新链表的表头更新为现原表头，更新原链表表头。
 
### 2 ReverseBetween
 - 难度： Medium
 - 来源： **LeetCode 92. Reverse Linked List II**
 - 思路： 首先记录原表头作为新链表的头部，然后找到开始逆置的节点，保存该节点的前驱，开始逆置的节点即是逆置部分的尾结点，按*LeetCode206*逆序，表头指针位于逆置部分的后继节点处，即逆置部分的尾结点的后继即为当前表头指针所处的节点。最后需要将逆置段前部与逆置段链接，如果逆置段起始节点的前驱为空即逆置段前部为空，那么逆置段新表头就是新链表表头，如果不为空，就需要将逆置段起始节点的前驱指向逆置段新表头。

 ## 链表相交

 ### 1 getIntersectionNode
 - 难度： Easy
 - 来源： ***LeetCode 160. Intersection of Two Linked Lists*

 ## 链表求环

 ### 1 hasCycle
 - 难度： Easy
 - 来源： ***LeetCode 141. Linked List Cycle***
 - 思路： 见 2。

 ### 2 detectCycle
 - 难度： Medium
 - 来源： ***LeetCode 142. Linked List Cycle II***
 - 思路：
    - 1. 使用集合Set，依次添加到集合中，如果已存在，则为环起点
    - 2. 使用快慢指针，快指针步长为2，慢指针步长为1。如果有环，快慢指针会相遇。当他们相遇时，快指针路程是慢指针两倍，可以证明头指针与相遇指针距离环起点的距离相等，从而可以找到起点。

## 链表划分

### 1 partition
 - 难度： Medium
 - 来源： ***LeetCode 86. Partition List***
 - 思路： 临时节点，小于部分节点和指针、大于部分节点和指针。

 ## 深度拷贝

 ### 1 copyRandomList
 - 难度： Medium
 - 来源： ***LeetCode 138. Copy List with Random Pointer***
 - 思路： 采用map，将原链表节点与新链表对应节点一一映射。

## 排序链表合并

### 1 mergeTwoLists
 - 难度： Easy
 - 来源： ***LeetCode 21. Merge Two Sorted Lists*** 

### 2 mergeKLists
 - 难度： Hard
 - 来源： ***LeetCode 23. Merge k Sorted Lists***
 - 思路： 分治。划分成两个子 lists 。

## 剑指Offer（三）：从尾到头打印链表
 - 入栈

## 剑指Offer（十四）：链表中倒数第k个结点
 - 两个指针，第一个指针先走K步，然后同时走，停止时，第二个指针指向的就是倒数第K个节点。

## 剑指Offer（十五）：反转链表
 - 新临时节点作为新头节点，首先保存原头结点的next，原头结点指向新头结点，然后更新新头结点为原头结点，原头结点更新为next。