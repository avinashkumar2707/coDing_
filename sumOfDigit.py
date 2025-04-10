def sumofdigit(n):
    sum=0
    while(n):
        b=n%10
        sum=sum+b
        n=n//10
    return sum
n=int(input())
print(sumofdigit(n))