def perfect_number(n):
    sum=0
    end=n//2+1
    for i in range(1,end,1):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True
    return False
n=int(input())
print(perfect_number(n))