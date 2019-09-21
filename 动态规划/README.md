# 动态规划

1. 确认**原问题**和**子问题**
2. 确认状态
3. 确认边界状态值
4. 确定状态转移方程

---

## 1、爬楼梯

 - 难度： Easy
 - 来源： ***LeetCode 70. Climbing Stairs***
 - 思路：

## 2、打家劫舍

 - 难度： Easy
 - 来源： ***LeetCode 198. House Robber***
 - 思路：  

## 2、最大子段和

 - 难度： Easy
 - 来源： ***LeetCode 53. Maximum Subarray***
 - 思路：  

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


