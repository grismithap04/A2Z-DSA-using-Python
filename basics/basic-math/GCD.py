class Solution:
    def GCD(self, n1, n2):
        a=min(n1,n2)
        b=max(n1,n2)
        rem=b%a
        if rem==0:
            return a
        else:
            return self.GCD(b,rem)
