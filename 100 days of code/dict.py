mydict = {"brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }

x = (mydict["brand"])
print(x)
print (type(mydict)) #check if it is a dictionary
#similar way of outputting
x = mydict.get("brand")
print(x)


#adding new elements
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change 

#x = mydict.items
print(x)

#updating adds if does not exist
mydict.update({"color": "red"}) 
print(x)
#removing specific items using pop() function
mydict.pop("color")
print(mydict) 
#popitem() removes the last item
#del() removes the dictionary
#clear() clears the dictionary

#looping dictionaries values() return values while keys() method returns the keys
for x in mydict.values():
  print(x) 


for x in mydict.keys():
  print(x) 
#items() returns both keys and values

for x, y in mydict.items():
  print(x, y) 



#copying dictionary using copy() and dict() methods
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 


#OR
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 