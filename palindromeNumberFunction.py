def palindrome(n):
    sum=0
    x=n
    while(n):
        b=n%10
        sum=(sum*10)+b
        n=n//10
    if sum==x:
        return True
    return False
n=int(input()) 
print(palindrome(n))