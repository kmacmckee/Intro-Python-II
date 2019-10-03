from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Add Items to rooms
room['foyer'].items.append(Item("Coins"))
room['foyer'].items.append(Item("Old Book"))
room['outside'].items.append(Item("Shovel"))
room['overlook'].items.append(Item("Old Key"))
room['treasure'].items.append(Item("Treasure Chest"))


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("Please enter your name:")
player1 = Player(player_name, room['outside'])
player1.items.append(Item("Flash Light"))
print(f"You find yourself at {player1.current_room.name}")
print(player1.current_room.description)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def get_user_input():
    user_input = input("Please press:\n W (To move North),\n D (To move East),\n S (To move South),\n A (To move West),\n F (To pickup Item),\n G (To drop Item),\n X (To Check for Items),\n I (To check Inventory)\n or Q to Quit:\n")
    
    switcher = {
        "q" : "quit",
        "w" : "north",
        "d" : "east",
        "s" : "south",
        "a" : "west",
        "f" : "pickup",
        "g" : "drop",
        "i" : "inventory",
        "x" : "check"
    }
    return switcher.get(user_input, "nothing")



should_quit = False
while should_quit != True:

    command = get_user_input()


    def get_item(item_name):
        #Get the names of items in the room
        room_items_names = []
        for item in player1.current_room.items:
            room_items_names.append(item.name)

        #Check if requested item_name is in the room
        if item_name in room_items_names:
            #if it is, add to players inventory
            player1.items.append(Item(item_name))
            #remove it from the list of item names in the room
            room_items_names.remove(item_name)
            #update the rooms list of items based
            updated_room_items = []
            for name in room_items_names:
                updated_room_items.append(Item(name))
            #set current_room's items equal to updated list of items
            player1.current_room.items = updated_room_items
            
            #update list of items in players inventory
            item_names = []
            for item in player1.items:
                #get the names of those items
                item_names.append(item.name)
            print(f"You are carrying {item_names}")
        else:
            print("There is not an item here with that name")



    def drop_item(item_name):
        #Get the names of the items in players inventory
        players_items_names = []
        for item in player1.items:
            players_items_names.append(item.name)

        #check if requested item is in players inventory
        if item_name in players_items_names:
            #if it is, add it to the rooms items
            player1.current_room.items.append(Item(item_name))
            #remove its name from the inventory list of item names
            players_items_names.remove(item_name)
            
            #update players inventory with remaining items
            updated_inventory = []
            for name in players_items_names:
                updated_inventory.append(Item(name))
            #set players inventory to updated inventory
            player1.items = updated_inventory


            item_names = []
            for item in player1.items:
                item_names.append(item.name)
            print(f"You are carrying {item_names}")
        else:
            print("You are not carrying an item with that name")


    
    if command == "quit":
        should_quit == True
        break
    elif command == "nothing":
        print("ERROR: You can't do that!")
        print(f"You're standing in {player1.current_room.name}")
    elif command == "north":
        if player1.current_room.s_to != None:
            next_room = player1.current_room.s_to
            player1.current_room = next_room
            print(f"You move to: {player1.current_room.name}, {player1.current_room.description}")
        else:
            print("You ran face first into a wall. Oops")
            print(f"You're standing in {player1.current_room.name}")
    elif command == "east":
        if player1.current_room.w_to != None:
            next_room = player1.current_room.w_to
            player1.current_room = next_room
            print(f"You move to: {player1.current_room.name}, {player1.current_room.description}")
        else:
            print("You ran face first into a wall. Oops")
            print(f"You're standing in {player1.current_room.name}")
    elif command == "south":
        if player1.current_room.n_to != None:
            next_room = player1.current_room.n_to
            player1.current_room = next_room
            print(f"You move to: {player1.current_room.name}, {player1.current_room.description}")
        else:
            print("You ran face first into a wall. Oops")
            print(f"You're standing in {player1.current_room.name}")
    elif command == "west":
        if player1.current_room.e_to != None:
            next_room = player1.current_room.e_to
            player1.current_room = next_room
            print(f"You move to: {player1.current_room.name}, {player1.current_room.description}")
        else:
            print("You ran face first into a wall. Oops")
            print(f"You're standing in {player1.current_room.name}")
    elif command == "pickup":
        name = input("Enter the name of the item you would like to pick up:\n")
        get_item(name)
    elif command == "drop":
        name = input("Enter the name of the item you would like to drop:\n")
        drop_item(name)
    elif command == "inventory":
        item_names = []
        for item in player1.items:
            item_names.append(item.name)
        print(f"You are carrying {item_names}")
    elif command == "check":
        item_names = []
        if player1.current_room.items:
            for item in player1.current_room.items:
                item_names.append(item.name)
            print(f"You look around and find {item_names}")
        else:
            print("You search the room but find nothing")







print("GAME OVER")
