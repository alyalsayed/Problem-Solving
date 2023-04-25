class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=1
        b=2
        if(n==1): return a 
        if(n==2): return b
        tmp=0
        for i in range(n-2):
            tmp=a
            a=b
            b = a + tmp
        return b

#Math solution 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = math.sqrt(5)
        fibn = ((1 + sqrt5) / 2)**(n+1) - ((1 - sqrt5) / 2)**(n+1)
        return int(fibn / sqrt5)
        