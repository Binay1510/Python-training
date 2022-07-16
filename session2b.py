#list
#mutable
# real life application- shooping cart list like in amazon can be changed so stored in list

prices=[10,20,30,40,90]
print(prices,type(prices))

del prices[1]     #delete at specific index
print(prices)

prices[2]=55   #update at specif index
print(prices)

prices.append(500)    #add at end
print(prices)