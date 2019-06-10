#wordt aan het begin laten zien en elke keer als de speler "help" typt

import time

player_data = {
    "name" : "",
    "location": "You are in the middle of a desert. You don't know where to go",
    "location_name" : "starting room",
}

def help_file():
    print("--------------------------")
    print("During this interactive game you will be exploring different places.")
    time.sleep(1)
    print("You can only use 'n', 'e', 's' and 'w' to choose a direction.")
    time.sleep(1)
    print("If you want to quit the game enter 'quit'")
    time.sleep(1)
    print("If you want to pick up an or drop an item, type in the name of the tool.")
    time.sleep(1)
    print("If you need a description where you are enter 'location'.")
    time.sleep(1)
    print("To see this introduction again type 'help'.")
    print("When you are ready, please press ENTER.")
    input()
    print("--------------------------")


print("Welcome to the game.")
time.sleep(1)
def introduction ():
    name = input("What is your name?: ")
    if len(name) < 1:
        print("Please enter a name.")
        introduction()
    else:
        player_data["name"] = name
introduction()

print("Welcome, " + str(player_data["name"]))
help_file()
print(str(player_data["name"]) + ",")
print("you have been dropped in the middle of a desert.")
print("You don't have anything with you...")
print("You're hungry and thirsty.")
print("You can go to each direction, however not all directions are good options...")

