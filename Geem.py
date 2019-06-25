import time

class location:
    name = ""
    discription = ""

    items = []
    door = False

    def __init__(self, name, discription = ""):
        self.items = []
        self.name = name
        self.discription = discription

        self.north = False
        self.east = False
        self.south = False
        self.west = False

    def set_coordinates(self, north = False, east = False, south = False, west = False):
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def get_coordinates(self):
        coordinates = []
        seperator = ", "
        if self.north == True:
            coordinates.append('North')
        if self.east == True:
            coordinates.append('East')
        if self.south == True:
            coordinates.append('South')
        if self.west == True:
            coordinates.append('West')

        return seperator.join(coordinates)

    def add_item(self, item):
        self.items.append(item)

    def set_items(self, items):
        self.items = items

    def get_items(self):
        return self.items

# here we define the grid
grid_columns = 5 # maximum amount of columns per row
grid_rows = 4 # maximum amount of rows

grid_row = 0
locations = []
while grid_row <= grid_rows:
    grid_column = 0
    row_locations = []
    while grid_column <= grid_columns:
        row_locations.append(location(str(grid_row) + ',' + str(grid_column)))
        grid_column += 1

    locations.append(row_locations)

    grid_row += 1

# here we define the route that the player can use
locations[0][0].set_coordinates(True, True)
locations[1][0].set_coordinates(True, False, True)
locations[2][0].set_coordinates(True, False, True)
locations[3][0].set_coordinates(False, True, True)
locations[3][1].set_coordinates(False, True, False, True)
locations[3][2].set_coordinates(False, False, True, True)
locations[2][2].set_coordinates(True, False, True)
locations[1][2].set_coordinates(True, True)
locations[1][3].set_coordinates(False, True, False, True)
locations[1][4].set_coordinates(True, False, False, True)
locations[2][4].set_coordinates(False, False, True, True)
locations[2][3].set_coordinates(True, True)
locations[3][3].set_coordinates(True, False, True)
locations[4][3].set_coordinates(False, True, False, True)
locations[4][4].set_coordinates(False, True, False, True)
locations[4][5].set_coordinates(False, False, False, True)

locations[1][0].set_coordinates(False, True, False, True)
locations[2][0].set_coordinates(False, False, False, True)

locations[2][0].add_item("Key") # Key for the door



player_data = {
    "name": "",
    "location": locations[0][0],
    "location_name": "starting room",
}

#wordt aan het begin laten zien en elke keer als de speler "help" typt
def help_file():
    print("--------------------------")
    print("During this interactive game you will be exploring different places.")
    time.sleep(1)
    print("You can only use 'n', 'e', 's' and 'w' to choose a direction.")
    time.sleep(1)
    print("If you want to quit the game enter 'q'")
    time.sleep(1)
    print("If you want to pick up an or drop an item, type in the name of the tool.")
    time.sleep(1)
    print("If you need a description where you are enter 'location'.")
    time.sleep(1)
    print("If you want to know which directions you can go type 'directions'.")
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

current_y = 0
current_x = 0

min_x = 0
min_y = 0
inventory = []

def game():
    control = input("What do you want to do?")
    control = control.lower()

    global current_x
    global current_y

    global grid_columns
    global grid_rows

    global inventory

    if control in location_controls:
        if control == "n":
            # controleer of we niet tegen de grens zijn aangelopen
            if current_y == grid_rows or player_data["location"].north == False:
                location_error("north")
                game()
            else:
                current_y = current_y + 1
        elif control == "e":
            if current_x == grid_columns or player_data["location"].east == False:
               location_error("east")
               game()
            else:
                current_x = current_x + 1
        elif control == "s":
            if current_y == min_y or player_data["location"].south == False:
                location_error("south")
                game()
            else:
                current_y = current_y - 1
        elif control == "w":
            if current_x == min_x or player_data["location"].west == False:
                location_error("west")
                game()
            else:
                current_x = current_x - 1

        player_data["location"] = locations[current_y][current_x]

        location_items = player_data["location"].get_items()
        if len(location_items) > 0:
            for item in location_items:
                inventory.append(item)
            seperator = ", "
            print("You found the following item(s): " + seperator.join(location_items))

        game()
    elif control == "help":
        help_file()
        game()
    elif control == "location":
        print(str(player_data["location"].name))
        game()
    elif control == "directions":
        directions = str(player_data["location"].get_coordinates())
        if directions == "":
            print("There is no way to go")
        else:
            print("You can go " + directions + " from here")
        game()
    elif control == "inventory":
        if len(inventory) > 0:
            seperator = ", "
            print("You found the following item(s): " + seperator.join(inventory))
        else:
            print("You have no items in your inventory")
        game()
    elif control == "q":
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
