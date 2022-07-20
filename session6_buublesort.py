# using bubble sort to sort data

     #0,1,2,3,4
data=[7,2,4,6,1]

print("DATA BEFORE SORTING:",data)

def sort_numbers(data):
    n=len(data)
    for idx1 in range(0,len(data)):
        for idx2 in range(0,n-idx1-1):

            if data[idx2]>data[idx2+1]:
                data[idx2],data[idx2+1]=data[idx2+1],data[idx2]



sort_numbers(data)
print("DATA AFTER SORTING :",data)