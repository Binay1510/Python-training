def add(num1,num2):
    result=num1+num2
    print("result from add ",result)

print("add is:",add)   #hashcode

#refrence copy
addition=add     #addition and add refrer to the same function

print("addition is:",addition)
addition(10,20)

def addition(num1, num2, num3):
    result = num1+num2+num3
    print("Result from addition is:", result)


# ReDefining the Function: Update the definition of the function
# Now, old definition does not exists and new one will work
def addition(amount):
    return amount*0.8


print("add now is:", add)               # HashCode
print("addition now is:", addition)     # HashCode which is same as of add

del addition

# addition(10, 20, 30) ->  error
print(addition(1200))
add(10, 20)