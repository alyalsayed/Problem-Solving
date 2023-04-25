#DP

class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if(n==0): return a 
        if(n==1): return b
        tmp=0
        for i in range(n-1):
            tmp=a
            a=b
            b = a + tmp
        return b

# math solution 

        
class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        return int(round((phi**n - (1-phi)**n) / sqrt5))
            
            
            
        