#create single value container

fries_price=50
#create+copy op
coke_price=fries_price

#update
coke_price=70

print("fries price ",fries_price,hex(id(fries_price)))
print("coke price ",coke_price,hex(id(coke_price)))

#create multivalue container
dish_price=[10,20,30,40,50]
johns_cafe_dish_price=dish_price

print("dish price",dish_price,hex(id(dish_price)))
print("Johns cafe dish price",johns_cafe_dish_price,hex(id(johns_cafe_dish_price)))

#update

johns_cafe_dish_price[2]=375
johns_cafe_dish_price[3]=400

print("johns cafe dish price",johns_cafe_dish_price,hex(id(johns_cafe_dish_price)))

del johns_cafe_dish_price[1]
del johns_cafe_dish_price

print("dish prices",dish_price,hex(id(dish_price)))