class Solution:
    def printNumbers(self, n):
        if n==0:
            return
        else:
            n-=1
            self.printNumbers(n)
            print(n)
