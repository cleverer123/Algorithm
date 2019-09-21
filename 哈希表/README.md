# 哈希表：

--- 
## 1、最长回文串
 - 难度： Easy
 - 来源： ***LeetCode 409. Longest Palindrome***

## 2、词语模式
 - 难度： Easy
 - 来源： ***LeetCode 290. Word Pattern***

## 3、同字符词语分组
 - 难度： Easy
 - 来源： ***LeetCode 49. Group Anagrams***

## 4、无重复字符的最长子串
 - 难度： Medium
 - 来源： ***LeetCode 3. Longest Substring Without Repeating Characters*** 
 - 思路： 双指针，前指针向前移动，记录字符的数量，若当前字符数量等于1，那么从begin到前指针就为无重子串长度，更新最长长度；若当前字符数量超过1，说明出现重复数字，那么将begin指针后移，同时将对应的字符数量减去，直到当前字符数量等于1。继续下一个前指针。

## 6、最小窗口子串
 - 难度： Hard
 - 来源： ***LeetCode 76. Minimum Window Substring*** 