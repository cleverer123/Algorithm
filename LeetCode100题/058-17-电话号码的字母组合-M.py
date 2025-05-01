from typing import Optional, List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']

        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:
                    queue.append(tmp + letter)
        return queue


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        
    def backtracking(conbination, nextdigit):
        if len(nextdigit) == 0:
            res.append(conbination)
        else:
            for letter in phone[nextdigit[0]]:
                backtracking(conbination + letter, nextdigit[1:])

        res = []
        backtracking('', digits)
        return res