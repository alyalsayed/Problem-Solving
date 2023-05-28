n=input()
def solve(n):
    steps = 1
    result=int(n)
    if(result<10):
        print(1)
        exit()
    while True:
        diff=max([int(i) for i in n])
        result =  result - diff
        steps+=1
        n = str(result)
        if(result < 10 ):
            return steps
        else :
            continue
print(solve(n))
        
    

    