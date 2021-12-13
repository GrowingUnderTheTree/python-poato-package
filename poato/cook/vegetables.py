import random as r


def vegetables():
    vege = ["carrot", "potato", "cucumber", "broccoli", "cauliflower"]
    a = r.choice(vege)
    if a == "potato":
        print("Yo you found the potato, do you want to cook it?(Yes/No)")
    elif a == "carrot":
        print("Sadly you didn't found the potato")
    elif a == "cucumber":
        print("Sadly you didn't found the potato")
    elif a == "broccoli":
        print("Sadly you didn't found the potato")
    elif a == "cauliflower":
        print("Sadly you didn't found the potato")


def fruit():
    yum = ["apple", "orange", "tomato", "pineapple", "mango"]
    b = r.choice(yum)
    if b == "pineapple":
        print("Yo you found the pineapple, do you want to add it to pizza?(Yes/No)")
    elif b == "apple":
        print("Sadly you didn't find the pineapple")
    elif b == "orange":
        print("Sadly you didn't find the pineapple")
    elif b == "tomato":
        print("Sadly you didn't find the pineapple")
    elif b == "mango":
        print("Sadly you didn't find the pineapple")
