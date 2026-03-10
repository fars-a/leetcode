class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x>=0:
        #     rev=0
        #     y=x
        #     while(x!=0):
        #         rem=x%10
        #         rev=rev*10+rem
        #         x=x//10
        #     if rev==y:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False
        x=str(x)
        if x==x[::-1]:
            return True
        else:
            return False
        