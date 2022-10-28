
class Person:
    def __init__(self, name) :
     self.name = name
    def greeting(self):
        return("Hi my name is {}".format(self.name))
some_person = Person("Andrew")
print(some_person)

