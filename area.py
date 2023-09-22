print("enter a number:",end="")
a=int(input())
temp=a
res=0
while a != 0:
    rem=a%10
    res=res*10+rem
    a//=10
print(res)
