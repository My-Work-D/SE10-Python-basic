
# test01

print("sachini")

 # test02

a,b = 1,3
if a>b :
 print("a is greater than b")
else:
    print("b is greater than or equal to a")

# test03

mystring = "hallow"
myfloat = 10.5
myint= 20

if mystring:
    print("String: %s" % mystring)
    print("String" + mystring)

if isinstance(myfloat,float) and myfloat == 10.5:
    print("Float: %f" % myfloat )

if isinstance(myint,int) and myint == 20:
     print("Int: %i" % myint)


  # test04

fruits= ["apple","mango"]
for x in fruits:
    print(x)

    # test05

def my_function():
    print("Hello from a function")
my_function()

# test06

def count(x,y):
    print(x*y)
    count(10,5)

    # test07
def count_num(a,b):
 return (a*b)

print(count_num(10,5))




