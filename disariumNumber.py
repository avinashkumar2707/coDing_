def digitcount(n):
    count=0
    while(n):
        n=n//10
        count=count+1
    return count
def disariumnumber(n):
    count=digitcount(n)
    sum=0
    x=n
    while(n):
        b=n%10
        sum=sum+(b**count)
        count=count-1
        n=n//10
    if (sum==x):
        return True
    return False
n=int(input())
print(disariumnumber(n))
