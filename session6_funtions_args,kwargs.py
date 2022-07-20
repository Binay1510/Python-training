# args and kwargs
# Arguments and KeyWord Argument

#args ->TUPLE
def add(*args):
    print(args)
    print(len(args))
    print(type(args))
    print(max(args))
    print(min(args))
    print(sum(args))

add(10,20,30,40,50,60)
#add(10,20,30,'john',40,50)     Crash the Program -> error cuz str nd int cant be compared or added

# kwargs -> DICTIONARY

def book_fligt(**kwargs):
    print(kwargs)
    print(type(kwargs))

book_fligt(source='delhi',destination='banglore',travellers=2)

# function with both *args and **kwargs

def demo(*args,**kwargs):
    print(args)
    print(kwargs)


demo(10,20,30,a=1,b=2,c=3 )

