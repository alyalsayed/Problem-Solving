
# https://codeforces.com/problemset/problem/1154/A

x1,x2,x3,x4=[int(x) for x in input().split()]
mx=max(max(max(x1,x2),x3),x4)
x=[x1,x2,x3,x4]
x.remove(mx)
a=mx-x[0]
b=mx-x[1]
c=mx-x[2]
print(a,b,c)
    
    