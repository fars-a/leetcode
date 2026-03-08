class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=(-2**31) and x<=(2**31):
            rev=0
            y=x
            if x<0:
                x=x*-1
            while x!=0:
                rem=x%10
                rev=rev*10+rem
                x=x//10
            if y<0:
                rev*=-1
            if rev>=-2**31 and rev<=2**31:
                return rev
            else:
                return 0
        else:
            return 0