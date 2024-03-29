# 栈&队列&堆

---

## 1、使用队列实现栈

 - 难度：Easy
 - 来源：***LeetCode 225. Implement Stack using Queues***
 - 思路：压栈(push)，将新数据放入一个临时队列，将原队列内容push进入临时队列，将临时队列内容push进数据队列。

## 2、使用栈实现队列
 - 难度：Easy
 - 来源：***LeetCode 232. Implement Queue using Stacks***
 - 思路：临时栈。

## 3、包含min函数的栈
 - 难度： Easy
 - 来源： ***LeetCode 155. Min Stack***
 - 思路： 采用一个最小数栈记录每个状态下的最小值。压栈时与当前最小值（mins栈顶）比较，mins栈顶压如比较后最小值；pop()时，数据栈与最小值栈同时pop。

 ## 4、检测顺序是否合法
  - 难度： Medium
  - 来源： ***Poj 1363. Rails***
  - 思路： 把order当成队列，原栈数据压入虚拟栈。 队列头部，与虚拟栈顶比较，如果相等则pop比较下一个，如果不等继续压栈。如果虚拟栈的没法清空，则不合法。

## 5、简单计算器
 - 难度： Hard
 - 来源： ***LeetCode 224. Basic Calculator***
 - 思路： 采用有限状态自动机遍历输入字符串，分为三个状态：BEGIN、NUMBER、OPERATION。BEGIN时判断是数字还是符号，转入对应状态，并退格索引。NUMBER状态下：如果是数字符，转化为十进制数;如果是符号，将数压如数栈（num_stack），依据compute_flag判断是否计算，修改状态为OPERATION。OPERATION状态下：如果是加号或减号，压操作符栈（op_stack），compute_flag改为1；如果是数字，修改状态，并退格；如果是左括号，compute_flag赋为1，



> 堆：对于任意一个下标为$$i(0 ≤ i ≤ n-1)$$的节点：
> - 父节点为$$ (i - 1)//2 $$
> - 左子节点 2 * i + 1 
> - 右子节点 2 * (i + 1)

## 6、寻找K最大元素
 - 难度： Medium
 - 来源： ***LeetCode 215. Kth Largest Element in an Array***
 - 思路： 
     - 1. 维护一个最大堆，堆底插入数据按如下方式向堆顶移动：与父节点比较，若比父节点大，则交换，否则不必交换，依此类推。堆顶数据更新按如下方式向堆底移动：左、右子节点的最大值与堆顶比较，若堆顶最大无须移动，否则与左右子节点大者交换，依次类推。堆顶元素为最大值，弹出堆顶元素(以堆底数据填充后更新堆)k-1次，堆顶则为第k大元素。
     - 2. 维护一个k大小的最小堆，堆顶则为第k大元素。堆中元素小于k时，直接进入堆；否则，当堆顶小于新元素时，弹出堆顶，将新元素加入堆。
     - 3. hash
     - 4. 分治

## 7、寻找中位数
 - 难度: Hard
 - 来源: ***LeetCode 295. Find Median from Data Stream***
 - 思路: 维护一个最大堆、一个最小堆。最大堆放较小的数，最小堆放较大的数，维持最大堆和最小堆规模一致（长度差不超过一），这样中位数就由两个堆顶产生。数据入堆，当两堆长度相等，与两个堆顶比较，只要大于最小堆堆顶，则入最小堆，否则入最大堆；当最大堆长度大于最小堆长度，若数据大于最大堆堆顶，则直接入最小堆，否则先将最大堆堆顶入最小堆，数据替代最大堆堆顶并更新最大堆；当最大堆长度小于最小堆长度，同理。最终，如果两堆长度相等，则中位数为两堆顶均值，否则为长度较大堆的堆顶。

## 8、射击气球
 - 难度： Medium
 - 来源： ***LeetCode 452. Minimum Number of Arrows to Burst Balloons***
 - 思路： 
