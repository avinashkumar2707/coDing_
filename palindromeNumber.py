n=int(input())
sum=0
x=n
while(n):
    b=n%10
    sum=(sum*10)+b
    n=n//10
if (x==sum):
    print("palindrome number")
else:
    print("not a palindrome number")
