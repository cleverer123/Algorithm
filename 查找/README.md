
## 二分查找

根据头尾索引(begin, end)计算中间索引mid，将mid对应的值与目标target比较，如果nums[mid]等于target，即找到，直接返回mid；如果target< nums[mid]，说明，目标在前半部分，更新end = mid - 1；如果target > nums[mid]，说明，目标在后半部分，更新begin = mid + 1。直到begin>end，终止查询。

### 1、插入位置
 - 难度： Easy
 - 来源： ***LeetCode 35. Search Insert Position***
 - 思路： 初始化index==-1，作为插入位置存储变量。在二分查找的过程中，如果target等于nums[mid]，返回index = mid；当target < nums[mid]，如果target > nums[mid-1]或者mid=0，返回index = mid作为插入位置，否则更新end = mid - 1继续二分；当target > nums[mid], 如果target < nums[mid+1]或者mid = len(nums) - 1，返回index = mid+1作为插入位置。当index不等于-1的时候终止查询。

### 2、

 - 难度： Medium
 - 来源： ***LeetCode 34. Find First and Last Position of Element in Sorted Array***
 - 思路： 分解成两个二分查询，一个查询同一元素的左边界，一个查询该元素的右边界。查询左边界：在二分查找过程中，当target == nums[mid]，如果nums[mid-1] < target或者mid=0，找到左边界mid，否则更新end = mid - 1，继续二分；当target < nums[mid]，更新end = mid -1；当target > nums[mid]，更新begin = mid + 1。查询右边界，当target == nums[mid]，如果nums[mid+1] > target或者mid = len(nums) - 1，找到右边界mid，否则继续二分。

### 3、旋转数组查找

 - 难度： Medium
 - 来源： ***LeetCode 33. Search in Rotated Sorted Array***
 - 思路： 根据头尾索引(begin, end)计算中间索引mid，将mid对应的值与目标target比较，
    - 当nums[mid]等于target，即找到，直接返回mid。
    - 当target< nums[mid]，
        - 如果nums[begin] < nums[mid]，则target落在该递增区间内，更新end = mid - 1，
        - 如果nums[begin] > nums[mid]，再比较target与nums[begin], 
            - 若target >= nums[begin], 目标落在（begin， mid-1）区间，更新end = mid - 1，
            - 若target < nums[begin], 目标落在（mid + 1,end)，更新begin = mid + 1。
        - 如果nums[begin] = nums[mid]，目标落在(mid+1, end)，更新begin = mid + 1。
    - 当target > nums[mid]，
        - 如果nums[begin] < nums[mid]， begin = mid + 1
        - 如果nums[begin] > nums[mid], 
            - 若target >= nums[begin], 目标落在(begin, mid-1)更新end = mid -1，
            - 若target < nums[begin], 目标落在(mid+1, end)，更新begin = mid + 1。
        - nums[begin] = nums[mid]，目标落在(mid+1, end)，更新begin = mid + 1。

## 二叉查找树

### 4、二叉查找树编码与解码
 - 难度： Medium
 - 来源： ***LeetCode 449. Serialize and Deserialize BST***
 - 思路： 

### 5、逆序数
 - 难度： Medium
 - 来源： ***LeetCode 315. Count of Smaller Numbers After Self***
 - 思路： (LeetCode 315 Hard 逆序数计算 方法三)[https://blog.csdn.net/qq_28327765/article/details/84674868]