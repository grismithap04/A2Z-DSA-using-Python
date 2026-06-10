class Solution:
    def whileLoop(self, d : int) -> int:
        sum=0
        count=0
        while(count<50):
            sum+=d
            d+=10
            count+=1
        return sum
