#set
#not stored in indexes
# uses hashing to store data
#unordered
#real life ex- mutual friends on social media 

johns_friends={"ross","joey","monica","gunther"}
print(johns_friends,type(johns_friends),hex(id(johns_friends)))

joes_friends={"joey","phoebe","rachel","ross"}
print(joes_friends,type(joes_friends),hex(id(joes_friends)))

mutual_friends=johns_friends.intersection(joes_friends)
print(mutual_friends)

johns_friends.add("tony stark")
print(johns_friends)