class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res = numbers[0]
        time = 1
        for i in range(1, len(numbers)):
            if time == 0:
                res = numbers[i]
                time = 1
            elif res == numbers[i]:
                time += 1
            else: 
                time -= 1
        time = 0 
        for i in range(len(numbers)):
            if numbers[i] == res:
                time += 1
        
        return res if time > len(numbers) // 2 else 0

if __name__ == "__main__":
    nums = [1,2,3,2,2,2,5,4,2]
    print(Solution().MoreThanHalfNum_Solution(nums))