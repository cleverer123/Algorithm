# 递归&回溯&分治
---
### 1-a、求子集
 - 难度： Medium
 - 来源： ***Leetcode 78. Subsets***
 - 思路：
    - 1. 回溯。对于每个元素，都有试探**放入**或**不放入**集合中的两个选择：选择**放入**该元素，递归地进行后续元素的选择，完成放入该元素后续所有元素的试探；之后将其拿出，即再进行一次选择**不放入**，递归地进行后续元素的选择，完成不放入该元素后续所有元素的试探。（本来选择放入，再选择一次不放入的这个过程，称为回溯试探法）

### 1-b、求子集
 - 难度： Medium
 - 来源： ***LeetCode 90. Subsets II***
 - 思路：
    - 1. 同样采用回溯思想，首先对输入序列排序，在加入结果中时，判断是否存在（Set去重）
    - 2. 首先对输入序列排序，以小数作为起始，依次选择后续大的数加入子集，如果数字与前一个相同，则跳过。

### 1-c、组合数之和
 - 难度： Medium
 - 来源： ***LeetCode 40. Combination Sum II***
 - 思路：
    - 1. 回溯 + 剪枝
    - 2. 首先对输入序列排序，以小数作为起始，依次选择后续大的数加入子集（如果数字与前一个相同，则跳过），同时target减去加入的元素。如果当前待加入元素大于target，则跳出循环（后续元素均无需试探）。
 - 相关题：
        - ***LeetCode 39. Combination Sum***
        - ***LeetCode 40. Combination Sum II***
        - ***LeetCode 216. Combination Sum III***

### 2、生成括号
 - 难度： Medium
 - 来源： ***LeetCode 22. Generate Parentheses***
 - 思路：在所有可能中，有些是合法的，有些不合法。递归限制条件：左右括号均最多个放n个；当左括号的个数大于右括号的个数，才进行放置右括号的递归。

### 3、N皇后
 - 难度： Hard
 - 来源： ***LeetCode 51. N-Queens***
 - 思路： 
    - 1.采用一个矩阵mark来标记地图上皇后可达的位置。第一个皇后在第一行第j列放置，扫描第二个皇后在第二行放置的位置，直到第N个皇后。如果不成功，需要回溯mark和location。
    - 2.在二维坐标系中观察可知，若x1 + y1 = x2 + y2, 则两点处在对角线上；若x1 - y1 = x2 - y2，则两点处在副对角线上。递归的条件，判断该列是否被占据，同时x1-y1是否存在；x1+y1是否存在。

## 分治思想

> 将一个难以直接解决的大问题，分割成一些规模较小的相同问题，以便各个击破，分而治之。
 - step1. 分解：将原问题分解为若干个规模较小，相互独立，与原问题形式相同的子问题；
 - step2. 解决：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题
 - step3. 合并：将各个子问题的解合并为原问题的解。    

依据分治法设计程序时的思维过程，实际上就是类似于数学归纳法，找到解决本问题的求解方程公式，然后根据方程公式设计递归程序。
1. 一定是先找到最小问题规模时的求解方法
2. 然后考虑随着问题规模增大时的求解方法
3. 找到求解的递归函数式后（各种规模或因子），设计递归程序即可

### 归并排序
1. 当列表中只有一个元素时就是最小规模。
2. 将规模扩大
3. 将列表递归地分解为两个列表，直到到达最小规模，对已经排序好的规模进行合并。

### 4、逆序数
 - 难度： Hard
 - 来源： ***LeetCode 315. Count of Smaller Numbers After Self ***
 - 思路： 采用归并排序的思想，在归并排序时，当右序列的数小于左序列，则右序列数加入结果序列，同时右序列下标右移；当左序列数小于等于左序列数，左序列数加入结果序列，此时右序列下标索引即为小于当前加入左序列的数的个数，左序列的下标索引右移。左序列剩余的数均为大于右序列的数，尚未更新小于这些左序列剩余的数的个数，需加上小于当前加入左序列的数的个数，也就是当前右序列下标索引（其实是末尾+1）。

## 剑指Offer（九）：变态跳台阶
 - f[0] = 1, f[1] = 1, f[n] = f[0] + ... + f[n-1]

## 剑指Offer（十）：矩形覆盖
 - 当前2*n的矩形，可以由，2*(n-1)的矩形加一条2*1的矩形组合，或者由2*(n-2)和两条横着的2*1矩形组合（如果是竖的，包含在前一种情况中）。因此 f[n] = f[n-1] +f[n-2]. f[1]=1, f[2]=2。同斐波那契数列。

 
