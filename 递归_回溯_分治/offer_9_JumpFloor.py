class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 2:
            return number

        f = [0] * (number + 1)
        f[0] = 1
        f[1] = 1
        for i in range(2, number+1):
            f[i] = sum(f[:i])

        return f[-1] 

    def jumpFloorII2(self, number):
        # write code here
        if number == 0:
            return 0
        return 2 ** (number-1)

if __name__ == "__main__":
    print(Solution().jumpFloorII(4))