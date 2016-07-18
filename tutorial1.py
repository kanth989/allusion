def multiplication(x, y):
# keyword func. Name x: parameter that is taken by the function
    return x*y

# print multiplication(7, 8),"This is the result"
q = "ramya"

def string_manipulation(x, y, z="tiger"):
    l = x.replace(y,z)
    local_variable = "ramya"
    global q
    q = x
    return l

k = "Hello, i'm srikanth, this is my first python class"
# print string_manipulation(x=k,z="srikanth",y="first")
# print q, "changed Global variable"
'''
fact(0) and fact(1)= 1
fact(4) = 4*3*2*1*0
  = 4 * (4-1) * (4-1-1) * 1   

fact(4) = 4*fact(4-1) -- all the values below comes here
    fact(4-1) = (4-1)* fact(4-1-1)
        fact(4-1-1)  = (4-1-1) * fact(4-1-1-1)
            fact(4-1-1-1) = 1
            finally what happens = 4* (4-1)* (4-1-1)* 1 
'''
def fact(x):
    if x <1000:
        if x == 1 or x== 0:
            return 1
        else:
            # print x, fact(x-1) 
            return x*fact(x-1)
    return "po be"
# print fact(4), "Hi this the result"
def mult(x):
    for i in range(21):
        print i*x
    
a = []
a.append("kanth")
a.append("ramya")
a.append("sravani")
a.append("deepika")
a.append("koundi")
a.append("satish")

# d = []
# for name in a:
#     d.append( name + " " + "python")
# print d

# List comprehension

d = [n + " "+ "python" for n in a]
# print d

# Lambda functions
y = lambda x: x + " " + "python"
# print map(y, a)
# mult(10)

ff = lambda  x: fact(x)

k = range(10)
# print k
# print map(ff, k)

def abc(x):
    return lambda x: x*2
print abc(10)

# website: https://docs.python.org/2/tutorial/index.html
















