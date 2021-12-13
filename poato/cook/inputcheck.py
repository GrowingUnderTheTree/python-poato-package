from poato.cook import vegetables as v
import random as r
import time

response = ["Yayyyyy! you cooked it!", "Oh wow! The potato turned into the super rare golden potato",
            "That's not a potato! That's a car!", "Why are you calling the bread as a potato?",
            "The potato exploded and you died. F"]

response1 = ["The Italians found you and I guess you know what happened. F",
             "The Italians found you but you escaped. How lucky!",
             "You forced the Italians who chased you to east the pineapple pizza. Brutal!",
             "The Italians didn't found you and you added it successfully!",
             "The pizza turns gold and explode. F",
             "Congrats! you unlocked the super rare golden flying pineapple pizza \n that will automatically hunt down the italians!"]


def cookcheck():
    v.vegetables()
    cook = input()
    if cook == "Yes":
        print("Cooking....")
        time.sleep(r.randint(1, 9))
        heh = r.choice(response)
        print(heh)
    elif cook == "No":
        print("Noo you missed the chance to cook a great meal!!!")


def addcheck():
    v.fruit()
    add = input()
    if add == "Yes":
        print("Adding....")
        time.sleep(r.randint(1, 7))
        print("hiding from the Italians.....")
        time.sleep(r.randint(2, 5))
        oh = r.choice(response1)
        print(oh)
    elif add == "No":
        print("Ok, have a great day!!!")
