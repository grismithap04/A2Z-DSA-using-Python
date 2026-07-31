class Solution:
    def pattern4(self, n):
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                if j<=i:
                    print(i,end='')
            print(end="\n")
