import random
friends =  input("gives me everybody's name separated with comas. ")
names = friends.split(",")

num_items = len(names)
#random_choice = random.randint(0, num_items-1)
#person_who_wil_pay = names[random_choice]
person_who_will_pay = random.choice(names)

print(person_who_will_pay +" is going to buy the meal today")