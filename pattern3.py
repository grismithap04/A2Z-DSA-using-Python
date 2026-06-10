class Solution:
    def pattern3(self, n):
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                if i>=j:
                    print(j,end='')
                else:
                    print(' ',end='')
            print(end="\n")
