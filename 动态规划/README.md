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
 - 题意： n阶台阶，每次可爬1或2阶台阶。共有多少种不同的方式爬到顶？
 - 思路： dp[i]表示爬到i共有的不同方式，第i阶台阶可以从第i-1爬一步或者第i-2爬两步到达，那么爬到第i阶共有不同的方式即为爬到第i-1阶的方式总数和爬到第i-2阶的方式总数之和，即dp[i] = dp[i-1] + dp[i-2]。dp[1] = 1, dp[2] = 2。
 
## 2、打家劫舍

 - 难度： Easy
 - 来源： ***LeetCode 198. House Robber***
 - 题意： 一条街上有若干人家，每家有一定的现金，你打算在不被警察发现的情况偷最多的钱，但是相邻两家同时被偷就会触发警报，你最多能偷多少。
 - 思路： dp[i]表示到第i家的最优情况，dp[i] 可能有两种选择，其一，选第i家，那么此时最优情况就是dp[i-2] + nums[i]；其二，不选第i家，那么最优解就是dp[i-1]。即dp[i] = max(dp[i-2] + nums[i], dp[i-1])。dp[0] = nums[0]，dp[1] = max(nums[0], nums[1])。

## 3、最大子段和 最大连续子序列和

 - 难度： Easy
 - 来源： ***LeetCode 53. Maximum Subarray*** 
 - 题意： 给定一个整形数组，找到其中最大连续子段和。
 - 思路： dp[i]表示以nums[i]结尾的子段的最大值。那么dp[i]由dp[i-1]转移得到，如果dp[i-1] + nums[i] > nums[i]，那么以nums[i]结尾的最大子段和的子段由以nums[i-1]结尾的最大子段和的子段与nums[i]组成；如果dp[i-1] + nums[i] < nums[i]， 那么以nums[i]结尾的最大子段和的子段只由nums[i]组成。即dp[i] = max(dp[i-1] + nums[i], nums[i])。dp[0] = nums[0]。最终最大连续子段和为dp中的最大值。

## 4、找零钱

 - 难度： Medium
 - 来源： ***LeetCode 322. Coin Change***
 - 题意： 给定整形数组coins代表不同面额硬币和整数amount代表总金额，返回组成该金额需要的最少硬币数。如果任意组合都无法组成该面额，返回-1。假定每一面额的硬币你可以拥有无数个。
 - 思路： dp[i]，代表金额i的最优解（组成金额i需要的最少硬币数）。dp[i] 可以由状态(i-面值)状态转移得到。遍历coins中的coin，如果coin > i，该硬币无法放到组合中；如果dp[i-coin] == -1, 也无法组合；那么对于 i >= coin and dp[i-coin] != -1，如果 dp[i] == -1 or dp[i-coin] + 1 < dp[i], 更新dp[i] = dp[i-coin] + 1。

## 5、三角形

 - 难度： Medium
 - 来源： ***LeetCode 120. Triangle***
 - 题意： 给定一个三角形数组，返回从上到下的最小路径和。
 - 思路： 从底向上处理。dp = [0] * (len(triangle) + 1)，dp[i] = line[i] + min(dp[i], dp[i+1])。

## 6、最长上升子序列

 - 难度： Medium
 - 来源： ***LeetCode 300. Longest Increasing Subsequence***
 - 题意： 返回最长上升子序列的长度。
 - 思路： 
    - 1. dp[i] 代表以第i个数字结尾的最长子序列，初始化为1。d[i]的计算，需要拿当前数字nums[i]，与前i-1个数字比较，0 <= j <= i-1，如果nums[i] > nums[j]， 说明nums[i]可以放在以nums[j] 结尾的最长子序列后面，作为新的最长子序列，长度为dp[j] + 1。如果dp[j] + 1 大于 dp[i]， 更新dp[i]。
    - 2. 采用一个栈，stack[i]表示，长度为i+1的上升子序列的最小可能取值。最终栈的长度就是最长公上升子序列。

## 7、最小路径和
 - 难度： Medium
 - 来源： ***LeetCode 64. Longest Increasing Subsequence***
 - 题意： 给定一个用非负数填充的 m x n 网格，找到一条从左上角到右下角的路径，它最小化沿其路径的所有数字的总和。
 - 思路： dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])。需要初始化dp的首行和首列，为grid首行、首列的累加和。

## 8、地牢游戏
 - 难度： Medium
 - 来源： ***LeetCode 174. Dungeon Game***
 - 题意： 
 - 思路： 从右下向左上倒推。在终点至少需要血量dp[-1][-1] = max(1, 1 - dungeon[-1][-1])；向上倒推，至少需要血量为前驱减去当前消耗(血量需要大于0，故和1之间取大者)  dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])；向左倒推，dp[-1][j] = max(1, dp[-1][j+1] - dungeon[-1][j] )。dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])。

## 9、最长公共子序列
 - 难度： Medium
 - 来源： ***LeetCode 1143. Longest Common Subsequence***
 - 思路： 如果text1[i] == text2[j], dp[i+1][j+1] = dp[i][j] + 1；否则，dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])。 

## 10、最短公共超序列
 - 难度： Hard
 - 来源： ***LeetCode 1092. Shortest Common Supersequence***
 - 思路： dp[i][j]用来标记公共部分的长度。dp回溯时，如果dp[i][j] == dp[i-1][j]，说明str1[i-1]和str2[j-1]两字符不相等，将str1[i-1]放入结果中，并将i指针前移；如果dp[i][j] == dp[i][j-1]，说明str1[i-1]和str2[j-1]两字符不相等，将str2[j-1]放入结果头部，并将j指针前移；否则，说明str1[i-1]和str2[j-1]两字符相等，将该字符放入结果头部，并将i，j指针前移。回溯结束时，str1或str2剩余的部分即为不同的部分，放入结果头部。

## 牛客：矩形覆盖
 - 题目描述
    我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
 - 思路：同斐波那契数列。

# 发现重叠子问题

## LeetCode 343. Integer Break
 - 思路： dp[i] = max(dp[i], j*(i-j), j*dp[i-j])

## LeetCode 91. Decode Ways

## LeetCode 92. Decode Ways II


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

## LeetCode 188. Best Time to Buy and Sell Stock IV
 

## 0-1 背包问题
 - F(n, C) 表示将n个物品放进容器为C的背包，使得价值最大。
 - 初始状态，放置第1个物品到容器为c的背包中，F(0,c)，当容量大于第一个物品的重量w[0]时，最大值为v[0]，否则为0（容量不足）
 - 状态转移方程：F(i, c) = max(F(i-1, c), v[i] + F(i-1, c - w[i]))，即，是保持上一状态，还是放入当前物品能够使得价值最大。放入当前物品，需要保证容量足够，及c>=w[i]，由状态F(i-1, c-w[i])转移得到，即刨除当前物品重量的前一个容量。
 

    
## LeetCode 416. Partition Equal Subset Sum
 - 思路：背包，n个物品，sum(nums)/2 容量

## LeetCode 322. Coin Change
