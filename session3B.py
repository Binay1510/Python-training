#loops
"""
idx=1
while idx <=10:
    print(idx)
    idx+=1
    """

"""for idx in range (1,11):
    print(idx)"""

for row in range(1,9):
         if row %2 == 0:
             for column in range(1, 5):
                print("\u2B1C" , end= "\u2B1B")
             print()
         else:
             for column in range(1, 5):
                print("\u2B1B", end="\u2B1C")
             print()

queen=int(input("ENter the cooridnates of Queen "))
coordinates=[]

#for x in range(5):
 #   for y in range(5):
  #      coordinates.append(x,y)




#queen[x,y]=int(input(" Enter the co-ordinates for Queen "),)
#print(" Queen placed at:", queen[x,y])


