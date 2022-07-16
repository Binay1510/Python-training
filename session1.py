#session- storage containers

#textual storage -> string  -> ' ', " " or """ """
#decimal storage container-> float,int..

#crearing storage container
dish_name ="poori thali"   #name=identifier
dish_rating=4.5
dish_price=148

#read storage continer

print(dish_name,id(dish_name),hex(id(dish_name)))              #id->hash numbers  hex-> hexadecimal notation ,oct,bin
print(dish_rating,hex(id(dish_rating)))
print(dish_price,hex(id(dish_price)))

#copy operation+create operation
mojito_price=dish_price    #also craeted mojitio_price
print(mojito_price,id(dish_price))          #same id as dishprice

age=148
print(age, id(age),hex(id(age)))        #same object will not be created twice

#
print("class dish name",type(dish_name))
print("class dish rate",type(dish_rating))
print("class dish price",type(dish_price))