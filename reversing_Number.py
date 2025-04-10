def reverse(n):
    sum=0
    while(n):
        b=n%10
        sum=(sum*10)+b
        n=n//10
    return sum
n=int(input())
print(reverse(n))