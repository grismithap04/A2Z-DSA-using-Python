class Solution:
    def pattern5(self, n):
        for i in range(n+1,1,-1):
            for j in range(i):
                if i>=j:
                    print('*',end='')
                else:
                    print(' ',end='')
            print(end="\n")
