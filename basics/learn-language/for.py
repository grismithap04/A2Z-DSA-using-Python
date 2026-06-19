class Solution:
    def forLoop(self, low : int, high : int) -> int:
        sum=0
        for i in range(low,high+1,1):
            sum+=i
        return sum
