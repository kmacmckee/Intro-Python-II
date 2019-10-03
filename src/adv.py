from room import Room
from player import Player

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("Please enter your name:")
player1 = Player(player_name, room['outside'])
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
    user_input = input("Please press W (To move North), D (To move East), S (To move South), A (To move West), or Q to Quit:\n")
    
    switcher = {
        "q" : "quit",
        "w" : "north",
        "d" : "east",
        "s" : "south",
        "a" : "west"
    }
    return switcher.get(user_input, "nothing")



should_quit = False
while should_quit != True:

    command = get_user_input()
    
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

print("GAME OVER")
