'''
class state:
    name=""
    capital=""
state1=state()
state1.name="odisha"
state1.capital="bbsr"
state2=state()
state2.name="maharastra"
state2.capital="mumbai"
print(f"{state1.capital} is the capital of {state1.name}")
print(f"{state2.capital} is the capital of {state2.name}")

class tiger:
    def name(self):
        print("my name is tipu")
    def age(self):
        print("my age is 34")
class  maletiger(tiger):
    def color(self):
        print("color is yellow")
maletiger1=maletiger()
maletiger1.name()
maletiger1.age()
maletiger1.color()

class animal:
    def type(self):
        print("type is..")
class tiger(animal):
    def type(self):
        print("tiger is dangerious")
class elephant(animal):
    def type(self):
        print("elephant is not dangerious")
t1=tiger()
t1.type()
e1=elephant()
e1.type()

class animal:
    def name(self):
        print("tipu")
class dog(animal):
    def name(self):
        super().name()
        print("tapu")
d1=dog()
d1.name()

class bike:

    def __init__(self,name=""):
        self.name=name
b1=bike("pleasure")
print(b1)


print(0xfb)

list=[1,"happy",3,4,4]
#list2=[8,9,1,7]
#list.append(8)
#list.extend(list2)
#for list1 in list:
print(len(list))

numbers=[n**2 for n in range(1,7)]
print(numbers)

a=("hello")
a1=("hello",1,2,3,"r","u","y")
a2=(3,6,1,5)
#for a2 in a1:
print(copy.a2 )

a=("hell0 is world")
#a2=a.replace('hell0','hye')
print(a.split('e'))

capital={"india":"delhi",
         "gujurat":"gandhinagar",
          "rajasthan":"jaypur"}
#cap={"india":"bbsr"}
#capital.update(cap1={"delhi":"delhi"})
#capital.update(cap)
print(capital.copy())

a={"what","is","this"}
b={1,9,7,5,3,9}
c=set()
d=[]
print(len(b))
print(any(c))
print(a)

class a:
    def name(self):
        print("my name is sasmita")
class b (a):
    def age(self):
        print("age is 16")
b1=b()
b1.name()
b1.age()

class polygon():
    def shape(self):
        print("shape is polygon")
class square(polygon):
    def shape(self):
        super().shape()
        print("shape is square")
class circle:
    def shape(self):
        print("shape is circle")
s1=square()
s1.shape()
c1=circle()
c1.shape()

a=int(input("enter a number"))
if (a <= 20):
    print("eligible for vote")
else:
    print("not elligible for vote")

class a:
    def name(self):
        print("my name is cocono")
class b:
    def age(self):
        print("My age is 16")
class c(a,b):
    def gender(self):
        print("male")
c1=c()
c1.name()
c1.age()
c1.gender()

class a:
    _a="smita"
    __b=10
    def show(self):
        print("a is",self._a)
        print("b is", self.__b)
a1=a()
a1.show()
print("b is ",a1._a)

#class a:
def add():
    print("sum of two number")
add()
#a1=a()
#a1.add()

def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
x=9
print(factorial(x))

def number(n):
    value=0
    while value<n:
        yield (value*value)
        value+=1
for n1 in number(8):
    print(n1)

a=[1,7,5,9]
iterator=iter(a)
for b in iterator:
    print(b)

def number(max=0):
    value=0
    while value<max:
        yield 2**value
        value+=1
for n in number(5):
    print(n)
# Output: 11
def all_even():
    n = 0
    while True:
        yield n
        n += 2
for p in all_even():
    print(p)

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)  # prints 11

# Output: 11

def mul(x):
    def mul1(y):
        return x*y
    return mul1
mul_1=mul(5)
result=mul_1(4)
print(result)

def mul(m):
    value=0
    while value<m:
        yield value
        value+=1
for n in mul(9):
    print(n)

def n(x):
    def m(y):
        return x*y
    return m
n1=n(6)
result=n1(7)
print(result)

def pretty(func):
    def make():
        print("i am beautiful")
        func()
    return make
def prettiest():
    print("i am ordinary")
pretty1=prettiest
pretty1()

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()

# Output: I am ordinary

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)

import first1
first1.add()

a={"cat":"domestic",
   "cow":"domesticw",
   "tiger":"non domestic"}
b={"cat":"non domestic"}
a.update(b)
print(a.get("tiger"))
b1=set()
b2={}
print(type(b2))

class a:
    def greet(self):
        print("welcome")
class b(a):
    def greet(self):
        super().greet()
        print("welcome to home")

a1=b()
a1.greet()

class A:
    _a="sasmita"
    __b="cocon"
    def show(self):
        print("a is",self._a)
        print("b is",self.__b)
a1=A()
a1.show()
print("a is ",A._a)
print("b is ",A.__b)

def makeup(func):
    def make():
        print ("you are beautiful")
        func()
    return make
def makeup1():
    print("you are pretty")
m1=makeup(makeup1)
m1()

def number(n):
    value=0
    while value<=n:
        yield value
        value+=1
for n1 in number(8):
    print(n1)

greet=lambda :print("hello world")
greet()

class a:
    def type(self):
        print ("hey")
class b(a):
    def type(self):
        print ("good morning")
class c(a):
    def type(self):
        print ("bye")

a1=b()
a1.type()
c1=c()
c1.type()
b1=a()
b1.type()

import first1
first1.add()

class a:
    __at=10
    _b="sasmita"
    def show(self):
        print (self._b)
        print (self.__at)
a1=a()
a1.show()

def outer(x):
    def inner(y):
        return x*y
    return inner
a1=outer(9)
result=a1(80)
print(result)

def number(n):
    value=0
    if (n%2==0):
        yield "even"
    else:
        yield "not even"

for n1 in number(10):
    print(n1)

class constructor:
    f1=0
    s1=0
    ans=0
    def __init__(self,first,second):
        self.f1=first
        self.s1=second
    def display(self):
        print("enter first number:"  +  str(self.f1))
        print("enter second number:"  +  str(self.s1))
        print("result:" + str(self.ans))
    def calculate(self):
        self.ans=self.f1 + self.s1
obj1=constructor(100,200)
obj1.calculate()
obj1.display()

import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

import re

b="good is odd pod"
result=re.split("\s",b,1)
print(result)

class a:
    x1=0
    y1=0
    ans=0
    def __init__(self,x,y):
        self.x1=x
        self.y1=y
    def display(self):
            print("enter first number",str(self.x1))
            print("enter second number", str(self.y1))
            print(self.ans)
    def calculate(self):
                self.ans=self.x1=self.y1
obj=a(100,200)
obj.calculate()
obj.display()
print(obj)

string=("hello")
print(string.isnumeric())

class a:
    a=0
    b=1
    x=a+b
    count=10
    while(x<=count):
        print(x)
        a=b
        b=x
        x+=1
a1=a()
'''
list=[1,2,3,"hello world"]
list=slice(2,3,4)
print(list)











