
import time

current_y = 0
current_x = 0

max_x = 5
max_y = 4
min_x = 0
min_y = 0

class locatie:
    naam = ""

    def __init__(self, naam):
        self.naam = naam

#locaties voor het spel
locaties = [ [locatie("0,0"), locatie("1,0"), locatie("2,0"), locatie("3,0"), locatie("4,0"), locatie("5,0")],
             [locatie("0,1"), locatie("1,1"), locatie("2,1"), locatie("3,1"), locatie("4,1"), locatie("5,1")],
             [locatie("0,2"), locatie("1,2"), locatie("2,2"), locatie("3,2"), locatie("4,2"), locatie("5,2")],
             [locatie("0,3"), locatie("1,3"), locatie("2,3"), locatie("3,3"), locatie("4,3"), locatie("5,3")],
             [locatie("0,4"), locatie("1,4"), locatie("2,4"), locatie("3,4"), locatie("4,4"), locatie("5,4")],
           ]

player_data = {
    "name": "",
    "location": locaties[0][0],
    "location_name": "starting room",
}


#class locatie:
#    locatie = player_data["location"]

    #def __init__(self, n, e, s, w):
     #   self.n = north
      #  self.e = east
       # self.s = south
        #self.w = west





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

location_controls = ["n", "e", "s", "w"]

def location_error(location):
    print("You cannot go " + location + " from here")

def game():
    control = input("Where do you want to go?")
    control = control.lower()

    global current_x
    global current_y
    global max_y
    global max_x

    if control in location_controls:
        if control == "n":
            # controleer of we niet tegen de grens zijn aangelopen
            if current_y == max_y:
                location_error("north")
                game()
            else:
                current_y = current_y + 1
        elif control == "e":
            if current_x == max_x:
               location_error("east")
               game()
            else:
                current_x = current_x + 1
        elif control == "s":
            if current_y == min_y:
                location_error("south")
                game()
            else:
                current_x = current_x - 1
        elif control == "w":
            if current_x == min_x:
                location_error("west")
                game()
            else:
                current_y = current_y - 1

        (player_data["location"]) = locaties[current_y][current_x]
        game()
    elif control == "help":
        help_file()
        game()
    elif control == "location":
        print(str(player_data["location"].naam))
        game()
    elif control == "quit":
        quit = input("Are you sure you want to stop?")
        quit = quit.lower()
        if quit == "yes":
            exit()
        if quit == "no":
            game()
    else:
        print("That is not an option")
        game()
game()

def locaties():
    current_location = (player_data["location"])
    #if current_location ==