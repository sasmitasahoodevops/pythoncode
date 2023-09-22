print("enter the number", end=" ")
n=int(input())
temp=n
digit=len(str(n))
res=0
while n>0:
    rem=n%10
    res=res+(rem**digit)
    n=n+1

if res==temp:
    print(res,"is a armstrong number")
else:
    print(res,"is not armstrong")

