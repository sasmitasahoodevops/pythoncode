n=10
num_1=0
num_2=1
next_number=num_2
count=1
while count<=n:
    print(next_number , end="")
    count+=1
    num_1,num_2=num_2,next_number
    next_number=num_1+num_2

print()