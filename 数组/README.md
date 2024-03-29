# 数组

---

## 剑指Offer（一）：二维数组中的查找
 - 思路： 从二维数组的右上角开始比较，如果相等，则找到；如果大于目标，说明在这一列之前，列索引向前移动；如果小于目标，说明在这行之下，行索引向下移动。

## 剑指Offer（六）：旋转数组的最小数字
 - 思路： 观察数组，发现上升序列的头部有可能是旋转数组的最小数字，因此找到下降的那个数，与之前下降的数比较，取小者。

## 剑指Offer（十三）：调整数组顺序使奇数位于偶数前面
 - 思路： 奇数弹出，从0向后依次插入

## 剑指Offer（二十八）：数组中出现次数超过一半的数字
 - 思路：数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现次数的和还要多。因此我们可以考虑在遍历数组的时候保存两个值：一个是数组的一个数字，一个是次数。当我们遍历到下一个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数加1；如果下一个数字和我们之前保存的数字不同，则次数减1。如果次数为零，我们需要保存下一个数字，并把次数设为1。由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，那么要找的数字肯定是最后一次把次数设为1时对应的数字。

## 剑指Offer（三十）：连续子数组的最大和
 - 思路： 动态规划，dp[i]表示以nums[i]结尾的连续子数组的最大和，那么dp[i]=max(dp[i-1] + nums[i], nums[i])。

## 剑指Offer（三十五）：数组中的逆序对
 - 思路： 同LeetCode 315。

## 剑指Offer（三十七）：数字在排序数组中出现的次数
 - 思路： 二分查找，分别查找左边界和右边界。查找左边界时，如果target == data[mid]，需要判断是否为左边界，如果target > data[mid-1],或者mid==0,即找到左边界。查找右边界，如果target == data[mid]，需要判断是否为右边界，如果target < data[mid+1]， 或者mid = len(data) -1,即找到右边界。

## 剑指Offer（四十）：数组中只出现一次的数字
 - 思路： 相同数字异或结果为0，数组所有元素异或所得结果必然不为0，依据结果第一个出现1的位置的不同，将数组分为两部分，两个不同的数字就分别出现在两部分中。

## 剑指Offer（五十）：数组中重复的数字
 - 思路： 将数组下标与元素值对应起来，如果下标与元素相等，指针后移；如果下标与元素不等，如果以数组元素为下标的数组值与其相等，则找到第一个重复的数字，否则交换该元素与以该元素为下标对应的元素，这样该元素与下标一致了。

## 剑指Offer（五十一）：构建乘积数组
 - 思路： 从头部累计乘和从尾部累计乘。