class Solution:
    def pattern4(self, n):
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                if i>=j:
                    print(i,end='')
                else:
                    print(' ',end='')
            print(end="\n")
