def perfectsquare():
    n=1
    while n<=10:
        square=n*n
        yield square
        n+=1
value=perfectsquare()

for i in value:
    print(i)


