def decode_ways(s):
    M = 1000000007
    dp = [0] * (len(s))
    dp[0] = helper(s[0])
    if len(s) >=2:
        dp[1] = (helper(s[0:2])  + dp[0] * helper(s[1]))%M

    for i in range(2, len(s)):
        dp[i] = (dp[i-2] * helper(s[i-1:i+1]) + dp[i-1] * helper(s[i]))%M

    # for i in range(2, len(s) + 1):
    #     u = s[i-1]
    #     pre_u = s[i-2] 
        
    #     if u == '*':
    #         if pre_u == '*':
    #             dp[i] = dp[i-2] * 15
    #         elif pre_u == '1' :
    #             dp[i] = dp[i-2] * 9 + dp[i-1] * 9         
    #         elif pre_u == '2':
    #             dp[i] = dp[i-2] * 6  + dp[i-1] * 9
    #         else:
    #             dp[i] = dp[i-1] * 9
    #     else:
    #         u = int(u)
    #         if pre_u == '*':
    #             if u == 0:
    #                 dp[i] = dp[i-2] * 2 
    #             if u >6:   
    #                 dp[i] = dp[i-2] * 1 + dp[i-1] * 1
    #             else:
    #                 dp[i] = dp[i-1] * 2 + dp[i-1] * 1
    #         else:
    #             pre_u = int(pre_u)
    #             dd = pre_u * 10 + u
    #             if pre_u == 0:
    #                 if dd < 10 or dd >26:
    #                     dp[i] = 0
    #                 else:
    #                     dp[i] = dp[i-2]
    #             else:
    #                 if dd < 10 or dd >26:
    #                     dp[i] = dp[i-1]
    #                 else:
    #                     dp[i] = dp[i-2] + dp[i-1]

             

    return dp[-1]            

def helper(ss):
    if len(ss) == 1:
        if ss[0] == '*':
            return 9
        elif ss[0] == '0':
            return 0
        else:
            return 1
    else:
        if ss == '**':
            return 15
        else:
            if ss[1] == '*':
                if ss[0] == '1':
                    return 9
                elif ss[0] == '2':
                    return 6
                else:
                    return 0
            elif ss[0] == '*':
                if int(ss[1]) <= 6:
                    return 2
                else:
                    return 1
            else:
                if int(ss) <10 or int(ss) >26:
                    return 0
                else:
                    return 1 
# https://blog.csdn.net/tzyshiwolaogongya/article/details/81290033
# https://blog.csdn.net/phoenix198425/article/details/78236761
print(decode_ways('*1*')) 
# print(decode_ways('*0')) 
# # print(decode_ways('*1')) 
# print(decode_ways('*6'))    
# # print(decode_ways('**'))    
# print(decode_ways('1*'))  
# print(decode_ways('2*'))      
print(decode_ways("*10*1"))   