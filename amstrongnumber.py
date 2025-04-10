def digit_counter(n):
    count=0
    while(n):
        n=n//10
        count=count+1
    return count
def amstrongnumber(n):
    count=digit_counter(n)
    sum=0
    x=n
    while(n):
        b=n%10
        sum=sum+(b**count)
        n=n//10
    if (sum==x):
        return True
    return False
n=int(input())
print(amstrongnumber(n))