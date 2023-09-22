def div(a,b):
    print(a/b)
def smart_div(func):

    def inner(a,b):
        if a<b:
         a,b = b,a
        return func
    return inner

div1 = smart_div(div)
div(2,4)
print(div1)



