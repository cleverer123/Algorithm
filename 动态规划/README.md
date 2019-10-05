# 动态规划

1. 确认**原问题**和**子问题**
2. 确认状态
3. 确认边界状态值
4. 确定状态转移方程

---

> 动态规划两套题目整理：
> [动态规划经典题目总结](https://blog.csdn.net/program_developer/article/details/85274825)
> [动态规划总结与题目分类](https://blog.csdn.net/eagle_or_snail/article/details/50987044)

## 1、爬楼梯

 - 难度： Easy
 - 来源： ***LeetCode 70. Climbing Stairs***
 - 思路：

## 2、打家劫舍

 - 难度： Easy
 - 来源： ***LeetCode 198. House Robber***
 - 思路： dp[i]表示到第i家的最优情况，dp[i] 可能有两种选择，其一，选第i家，那么此时最优情况就是dp[i-2] + nums[i]；其二，不选第i家，那么最优解就是dp[i-1]

## 2、最大子段和 最大连续子序列和

 - 难度： Easy
 - 来源： ***LeetCode 53. Maximum Subarray*** 
 - 思路： dp[i]表示以nums[i]结尾的子段的最大值。

## 3、找零钱

 - 难度： Medium
 - 来源： ***LeetCode 322. Coin Change***
 - 思路： dp[i]，代表金额i的最优解（即最小使用张数）。dp[i] 可以由状态(i-面值)状态转移得到.

## 5、三角形

 - 难度： Medium
 - 来源： ***LeetCode 120. Triangle***
 - 思路： 从底向上处理，dp[i]代表，第i层的最优解.

## 6、最长上升子序列

 - 难度： Medium
 - 来源： ***LeetCode 300. Longest Increasing Subsequence***
 - 思路： 
    - 1. dp[i] 代表以第i个数字结尾的最长子序列，初始化为1。d[i]的计算，需要拿当前数字nums[i]，与前i-1个数字比较，0 <= j <= i-1，如果nums[i] > nums[j]， 说明nums[i]可以放在以nums[j] 结尾的最长子序列后面，作为新的最长子序列，长度为dp[j] + 1。如果dp[j] + 1 大于 dp[i]， 更新dp[i]。
    - 2. 采用一个栈，stack[i]表示，长度为i+1的上升子序列的最小可能取值。最终栈的长度就是最长公上升子序列。

## 7、最小路径和
 - 难度： Medium
 - 来源： ***LeetCode 300. Longest Increasing Subsequence***
 - 思路： 

## 8、地牢游戏
 - 难度： Medium
 - 来源： ***LeetCode 300. Longest Increasing Subsequence***
 - 思路： 

## 9、最长公共子序列
 - 难度： Medium
 - 来源： ***LeetCode 1143. Longest Common Subsequence***
 - 思路：

## 10、最短公共超序列
 - 难度： Hard
 - 来源： ***LeetCode 1092. Shortest Common Supersequence***
 - 思路： dp[i][j]用来标记公共部分的长度。dp回溯时，如果dp[i][j] == dp[i-1][j]，说明str1[i-1]和str2[j-1]两字符不相等，将str1[i-1]放入结果中，并将i指针前移；如果dp[i][j] == dp[i][j-1]，说明str1[i-1]和str2[j-1]两字符不相等，将str2[j-1]放入结果头部，并将j指针前移；否则，说明str1[i-1]和str2[j-1]两字符相等，将该字符放入结果头部，并将i，j指针前移。回溯结束时，str1或str2剩余的部分即为不同的部分，放入结果头部。

## 牛客：矩形覆盖
 - 题目描述
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
 - 思路：同斐波那契数列。

## LeetCode 343. Integer Break
 - 思路： mem[i] = max(mem[i], j * (i-j), j * mem[i-j]) 

## LeetCode 91. Decode Ways
 - 思路：

## LeetCode 62. Unique Paths
 - 思路：

## LeetCode 63. Unique Paths II
 - 思路： 有障碍物，边界dp及后续变为0，非边界dp变为0。

## LeetCode 213. House Robber II
 - 思路： 抢劫第一个房子，则不能抢劫最后一个房子。抢劫最后一个房子，则不能抢劫第一个房子。分解为两个House Robber问题。

## LeetCode 337. House Robber III
 - 思路： 二叉树深度优先遍历，后序遍历，维护一对值,res[0] 代表不抢当前节点所能得到的最大值，其等于左右子节点最大值之和，res[1]代表抢劫当前节点所得的最大值，其值应等于，节点值及上左右子节点不抢所得的最大值之和。

## LeetCode 121. Best Time to Buy and Sell Stock
 - 思路： 
    - 动态规划1 维护 截止到当日的最小值，当日股价减去最小值，即为截止至当日可获得的最大收益。
    - 动态规划2 维护 在当天卖出的最佳交易 和 到目前为止最好的交易。

## LeetCode 123. Best Time to Buy and Sell Stock III
 - 思路：动态规划，开辟两个数组dp1和dp2，dp1[i]表示在price[i]之前进行一次交易所获得的最大利润，dp2[i]表示在price[i]之后进行一次交易所获得的最大利润。则dp1[i]+dp2[i]的最大值就是所要求的最大值（代码中则是从后往前寻找降幅最大）。

## LeetCode 309. Best Time to Buy and Sell Stock with Cooldown
 - 思路： 有限状态机，三种状态，rest，hold，sold状态。
 - 参考：
    - https://v.youku.com/v_show/id_XMzgzOTA2Mzc2OA==.html 
    - https://blog.csdn.net/program_developer/article/details/86245536



## 0-1 背包问题
 - F(n, C) 表示将n个物品放进容器为C的背包，使得价值最大。
 - 初始状态，放置第1个物品到容器为c的背包中，F(0,c)，当容量大于第一个物品的重量w[0]时，最大值为v[0]，否则为0（容量不足）
 - 状态转移方程：F(i, c) = max(F(i-1, c), v[i] + F(i-1, c - w[i]))，即，是保持上一状态，还是放入当前物品能够使得价值最大。放入当前物品，需要保证容量足够，及c>=w[i]，由状态F(i-1, c-w[i])转移得到，即刨除当前物品重量的前一个容量。
 

    
## LeetCode 416. Partition Equal Subset Sum
 - 思路：背包，n个物品，sum(nums)/2 容量
