#Recusrssion in memory
"""
data=[10,20,30]
max=data[0]

for idx in range(1,len(data)):
    if data[idx]>max:
        max=data[idx]
print("max is: ",max)
"""
# recursive function to get maximum number out of 3
def get_max(numbers, length):
    if length==1:
        return numbers[0]
    else:
        number=get_max(numbers,length-1)
        if number>numbers[length-1]:
            return number
        else:
            return numbers[length-1]

data=[10,20,30]
max=get_max(data,len(data))
print("max is :",max)

