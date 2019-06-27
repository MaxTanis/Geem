
import time



class location:
    name = ""
    description = ""

    items = []
    door = False

    start = False
    end = False
    current = False
    visited = False

    def __init__(self, name, description = ""):
        self.items = []
        self.name = name
        self.description = description

        self.door = False # is er een deur?

        self.north = False # boolean of de speler naar het noorden kan
        self.east = False # boolean of de speler naar het oosten kan
        self.south = False # boolean of de speler naar het zuiden kan
        self.west = False # boolean of de speler naar het westen kan

        self.start = False # startpunt
        self.end = False # eindpunt
        self.current = False # huidige kamer
        self.visited = False # doorlopen kamer

    def add_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

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

    def set_has_door(self, has_door):
        self.door = has_door

    def set_is_start(self, is_start):
        self.start = is_start


    def set_is_end(self, is_end):
        self.end = is_end


    def set_is_current(self, is_current):
        self.current = is_current


    def set_is_visited(self, is_visited):
        self.visited = is_visited

# hier maken wij het rooster voor het spel
grid_columns = 5 # maximum aantal kolommen
grid_rows = 4 # maximum aantal rijen

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


# hier geven we de route aan die speler alleen kan lopen
locations[0][0].set_coordinates(True, True)
locations[1][0].set_coordinates(True, False, True)
locations[2][0].set_coordinates(True, False, True)
locations[3][0].set_coordinates(False, True, True)
locations[3][1].set_coordinates(False, True, False, True)
locations[3][2].set_coordinates(False, False, True, True)
locations[2][2].set_coordinates(True, False, True)
locations[1][2].set_coordinates(True, True, True)
locations[1][3].set_coordinates(False, True, False, True)
locations[1][4].set_coordinates(True, False, False, True)
locations[2][4].set_coordinates(False, True, True, True)
locations[2][3].set_coordinates(True, True)
locations[3][3].set_coordinates(True, False, True)
locations[4][3].set_coordinates(False, True, False, True)
locations[4][4].set_coordinates(False, True, False, True)
locations[4][5].set_coordinates(False, False, False, False)

locations[2][1].set_coordinates(True)
locations[0][1].set_coordinates(True, False, False, True)
locations[1][1].set_coordinates(False, False, True, False)
locations[0][2].set_coordinates(True)
locations[2][5].set_coordinates(False, False, False, True)
locations[4][2].set_coordinates(False, True)
locations[4][0].set_coordinates(False, False, True)

locations[1][1].add_item("key") # Key voor de deur

#description per locatie
locations[0][0].add_description("You are in the middle of a desert")
locations[1][0].add_description("You see some light in the far North")
locations[2][0].add_description("You have entered a village.")
locations[3][0].add_description("You are now in an abandoned house.")
locations[3][1].door = True
locations[3][1].add_description("You are now standing outside the house. You see a pad on your East")
locations[3][2].add_description("There is a pad heading towards the South. Follow it")
locations[2][2].add_description("You have walked for hours, but the pad goes on...")
locations[1][2].add_description("You are standing in front of a dark wood.")
locations[1][3].add_description("You hear some noises on your East.")
locations[1][4].add_description("You found a stream, but you cannot cross it...")
locations[2][4].add_description("You see a high mountain in front of you. It would be easier to go around it.")
locations[2][3].add_description("There is a small city in the far North.")
locations[3][3].add_description("It's a long walk but you're almost there.")
locations[4][3].add_description("You are in the middle of the city now.")
locations[4][4].add_description("You see many people on your right, maybe you could ask them where you are.")
locations[4][5].add_description("The people told you where you are and helped you to go home.\nYou have now completed the game!\nIf you want to quit enter 'q'.")


locations[2][1].add_description("There is a closet. Nothing in here. Go back...")
locations[0][1].add_description("There is something on your North, go there.")
locations[1][1].add_description("You found a chest, would you like get the items from the chest?")
locations[0][2].add_description("You are in the middle of a dark wood, you can only go back...")
locations[2][5].add_description("You found the stream again, you have to go back...")
locations[4][2].add_description("There is a supermarket. You bought some food and drinks. You have to go back now")
locations[4][0].add_description("You are standing in front of a closet. Nothing here...")

player_data = {
    "name": "",
    "location": locations[0][0],
    "location_name": "starting room",
}
locations[0][0].set_is_current(True) # stel de huidige kamer in
locations[0][0].set_is_start(True) # stel de start kamer in
locations[0][0].set_is_visited(True) # stel gelijk in dat de eerste kamer is doorlopen
locations[4][5].set_is_end(True) # stel de eindkamer in

#wordt aan het begin laten zien en elke keer als de speler "help" typt
def help_file():
    print("--------------------------")
    print("During this interactive game you will be exploring different places.")
    time.sleep(1)
    print("You can only use 'n', 'e', 's' and 'w' to choose a direction.")
    time.sleep(1)
    print("If you want to quit the game enter 'q'")
    time.sleep(1)
    print("If you want to pick up an item enter 'g'. To use it enter 'u'")
    time.sleep(1)
    print("To know what is in your inventory type 'i'")
    time.sleep(1)
    print("If you need a description where you are enter 'l'.")
    time.sleep(1)
    print("If you want to know which directions you can go type 'd'.")
    time.sleep(1)
    print("If you want the map to be showed enter 'm'.")
    time.sleep(1)
    print("To see this introduction again type 'h'.")
    time.sleep(1)
    print("When you are ready, please press ENTER.")
    print("--------------------------")
    input()

# introductie van het spel
print("Welcome to the game.")
time.sleep(1)
def introduction ():
    name = input("What is your name?: \n")
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

# wordt laten zien als de speler een locatie opwilt die niet kan
def location_error(location):
    print("You cannot go " + location + " from here")

# functie waarmee de lijst met kamers wordt omgezet naar een kaart
def list_to_map(map_list):
    map_string = ''

    column_string = '+-----'  # dit tonen we boven elke cel
    column_string_end = '+'  # dit tonen we aan het eind van de regel

    column_empty = '     '  # lege cel
    column_current = '  X  '  # huidige cel
    column_visited = '  *  ' # doorlopen cel
    column_start = '  S  '  # start cel
    column_end = '  F  '  # eind cel

    for row_i in range(len(map_list)):
        row_string = ''

        col_i = 0
        while col_i < len(map_list[row_i]):
            row_string += column_string
            col_i += 1
        row_string += column_string_end + '\n'  # we beginnen elke regel met een +----+ regel

        # dan gaan we voor alle kolommen bepalen welke tekst we er in moeten tonen
        for column_i in range(len(map_list[row_i])):
            current_column_string = column_empty  # standaard tonen we de lege cel
            if map_list[grid_rows-row_i][column_i].start == True:
                # als de cel waar we op zitten de startcel is, tonen we de bijbehorende tekst
                current_column_string = column_start
            elif map_list[grid_rows-row_i][column_i].current == True:
                # als de cel waar we op zitten de huidige is, tonen we de bijbehorende tekst
                current_column_string = column_current
            elif map_list[grid_rows-row_i][column_i].end == True:
                # als de cel waar we op zitten het eind is, tonen we de bijbehorende tekst
                current_column_string = column_end
            elif map_list[grid_rows-row_i][column_i].visited == True:
                # als de cel waar we op zitten een doorlopen cel is, tonen we de bijbehorende tekst
                current_column_string = column_visited
            row_string += '|' + current_column_string  # we eindigen altijd met ee | om de regel af te sluiten
        row_string += '|'

        # als laatste maken we ook een onderkant van de regel
        if row_i == (len(map_list) - 1):
            row_string += '\n'
            col_i = 0
            while col_i < len(map_list[row_i]):
                row_string += column_string
                col_i += 1
            row_string += column_string_end + '\n'

        map_string += row_string + '\n'  # vul de tekst van de complete kaart aan
    return map_string  # geef de tekstuele vorm van de kaart terug

current_y = 0
current_x = 0
last_y = 0
last_x = 0

min_x = 0
min_y = 0
inventory = []

# hoofd spel
def game():
    control = input("\nWhat do you want to do? \n")
    control = control.lower() # zorgt ervoor dat alles in kleine letters is

    global current_x
    global current_y
    global last_x
    global last_y

    global grid_columns
    global grid_rows

    global inventory
    # n e s w
    if control in location_controls:
        old_x = current_x
        old_y = current_y

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
        # als de deur een kamer heeft wordt dit getoond
        if locations[current_y][current_x].door == True:
            print("This room has a door which blocks the entrance")
            # in de inventory kijken van de speler of er een 'key' inztit
            for inventory_item in inventory:
                if inventory_item == "key":
                    # stel de vorige kamer weer in als huidige, omdat je nog niet verder kan
                    print("You have a key in your inventory, press 'u' to open the door with the key")
                    current_x = old_x
                    current_y = old_y
                    game()
                    # the speler heeft nog geen sleutel en moet hem eerst zoeken
            print("You do not have a key to open the door, find it somewhere else.")
            # stel de vorige kamer weer in als huidige, omdat je nog niet verder kan
            current_x = old_x
            current_y = old_y
            game()

        # als er geen deur is kan de speler verder

        player_data["location"].set_is_current(False) # we gaan een kamer verder, dus is dit niet meer de huidige
        player_data["location"] = locations[current_y][current_x]
        player_data["location"].set_is_current(True) # dit is nu de huidige kamer geworden
        player_data["location"].set_is_visited(True) # stel ook in dat deze kamer is doorlopen

        # als er een omschrijving is, tonen we de omschrijving
        description = player_data["location"].get_description()
        if description != "":
            print((str(description)))
        game()
    elif control == "h": # help file die aan het begin ook is laten zien
        help_file()
        game()
    elif control == "l": # locatie met description
        description = player_data["location"].get_description()
        print(str(description))
        game()
    elif control == "d":
        directions = str(player_data["location"].get_coordinates())
        if directions == "":
            print("There is no way to go")
        else:
            print("You can go " + directions + " from here")
        game()
    elif control == "i": # inventory van de speler
        if len(inventory) > 0:
            seperator = ", "
            print("The following items are in your inventory: " + seperator.join(inventory))
            game()
        else:
            print("You have no items in your inventory")
            game()
    elif control == "g": # als de speler een item wilt oppakken
        location_items = player_data["location"].get_items()
        if len(location_items) > 0:
            for item in location_items:
                inventory.append(item)
            seperator = ", "
            print("You found the following item(s): " + seperator.join(location_items))
            player_data["location"].set_items([])  # remove the items from the room
        else:
            print("There are no (more) items to pickup")
        game()
    elif control == "u": # als de speler een item wilt gebruiken
        if len(inventory) > 0:
            for inventory_i in range(len(inventory)):
                if inventory[inventory_i] == "key":
                    print("You used the key to open the door")
                    del inventory[inventory_i] #  key weg van invertory
                    #player_data["location"].set_has_door(False) #  haalt de deur weg
                    locations[3][1].set_has_door(False) # haal de deur weg
                    game()
            print("You do not have a key that you can use")
            game()
        else:
            print("You have no items in your inventory")
        game()
    elif control == "m": # de code voor de map
        print(list_to_map(locations))

        print("'S' is the start location")
        print("'*' is a visited location")
        print("'F' is the last location")
        print("'X' is your current location")
        game()
    elif control == "q":
        quit = input("Are you sure you want to stop?")
        quit = quit.lower()
        if quit == "yes" or quit =="y":
            go = False
        if quit == "no" or quit == "n":
            game()
    else:
        print("That is not an option")
        game()
game()
