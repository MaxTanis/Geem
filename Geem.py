
import time


class locatie:
    naam = ""

    def __init__(self, naam):
        self.naam = naam

#locaties voor het spel
locaties = [ [locatie("0,0"), locatie("0,1"), locatie("0,2"), locatie("0,3"), locatie("0,4"), locatie("0,5")],
             [locatie("1,0"), locatie("1,1"), locatie("1,2"), locatie("1,3"), locatie("1,4"), locatie("1,5")],
             [locatie("2,0"), locatie("2,1"), locatie("2,2"), locatie("2,3"), locatie("2,4"), locatie("2,5")],
             [locatie("3,0"), locatie("3,1"), locatie("3,2"), locatie("3,3"), locatie("3,4"), locatie("3,5")],
             [locatie("4,0"), locatie("4,1"), locatie("4,2"), locatie("4,3"), locatie("4,4"), locatie("4,5")],
           ]

player_data = {
    "name" : "",
    "location": locaties[0][0],
    "location_name" : "starting room",
}


class locatie:
    locatie = player_data["location"]

    def __init__(self, n, e, s, w):
        self.n = north
        self.e = east
        self.s = south
        self.w = west




#wordt aan het begin laten zien en elke keer als de speler "help" typt
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
    time.sleep(1)
    print("When you are ready, please press ENTER.")
    print("--------------------------")
    input()




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


def game():
    control = input("Where do you want to go?")
    control = control.lower()
    if control == "n":
        (player_data["location"]) = locaties[0+1][0]
        game()
    elif control == "e":
        (player_data["location"]) = locaties[0][0+1]
        game()
    elif control == "s":
        (player_data["location"]) = locaties[0-1][0]
        game()
    elif control == "w":
        (player_data["location"]) = locaties[0][0-1]
        game()
    elif control == "help":
        help_file()
        game()
    elif control == "location":
        print(str(player_data["location"]))
        game()
    else:
        print("That is not an option")
        game()
game()


