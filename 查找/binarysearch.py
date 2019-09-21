# 递归
def bs(nums, begin, end, target):
    if begin > end:
        return False
    mid = (begin + end)//2
    if target == nums[mid]:
        return True
    elif target < nums[mid]:
        return bs(nums, begin, mid - 1, target)
    else:
        return bs(nums, mid, end + 1, target)

# 循环
def bs2(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = (begin + end)//2
        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            end = mid - 1
        else:
            begin = mid + 1
    return False




if __name__ == "__main__":
    example = [1, 3, 5, 6, 7, 9, 11, 17, 43, 67, 432]

    # print(bs(example, 0, len(example)-1,  17))   
    print(bs2(example,  17))   