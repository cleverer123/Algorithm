class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        i = 0
        while i < len(numbers):
            if i == numbers[i]:
                i += 1
            else:
                j = numbers[i]
                if numbers[i] == numbers[j]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return False

if __name__ == "__main__":
    nums = [2,3,1,0,2,5,3]
    d = [0]
    print(Solution().duplicate(nums, d))
    print(d)
                
        