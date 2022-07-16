johns_age=20
#copy operation
fionas_age =johns_age
print("johns age hashcode:" ,hex(id(johns_age)))
print("fionas age hashcode:" ,hex(id(fionas_age)))

#update operaation
#fionas_age=30
#print("fionas age after updation",hex(id(fionas_age)))


#john and fionas age is refrencing to same int object so deletion of 
del johns_age
print(hex(id(fionas_age)))

del johns_age
del fionas_age
print(hex(id(fionas_age)))   #will give error