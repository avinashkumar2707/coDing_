def count(n):
    count=0
    while(n):
        n=n//10
        count=count+1
    return count
n=int(input())
print(count(n))