class Solution:
    def isPalindrome(self, n):
        n=rev=str(n)
        rev=rev[::-1]
        if rev==n:
            return True
        else: 
            return False
