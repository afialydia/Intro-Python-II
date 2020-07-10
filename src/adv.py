from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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

# print("test", room['narrow'].n_to)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


room['narrow'].items = [Item('keys', '\nYou may need this for what lies ahead\n')]


def newPlayerStart(name):
    global newPlayer
    newPlayer = Player(name, current_room= room['outside'])
    
   
def nav(newPlayer):
    print( newPlayer.name + "," + str(newPlayer.current_room)+ ' ' + str(newPlayer.current_room.description ))


def user_movement(newPlayer):
    global movement
    movement = input('You look down at your phone... still no service. I guess I can poke around until my phone has service. Choose: [n]:north, [s]:south, [e]:east, [w]:west, or [q]:quit\n\nTo check items in your inventory choose [i]:inventory\n')

    newPlayer.move(movement)
    
    nav(newPlayer)

def game_start():
    
    wander = input("It's 5pm on a Saturday.. you're shift is almost over and you can't wait to clock out. For the most part, Lifter pays well but since things have gone the way they have, over the last few months you've had to scrape together enough fare just to cover the cost of gas. You toy with the idea of just turning the app off and heading home to make dinner when something comes through... a cross town fare that will land you 3 blocks from home. You wonder if you've passed this patron on your way to the dry cleaners. The scenerary becomes serene as you let your mind wander.  \n \n What do you think about? ['A. going swimming with friends', 'B. eating dinner with your cats', 'C. the water crisis']")
    if wander.lower() in ["a", "b", "c"]:
       
        print("\n......\n")
        
        print(".................FDOJGNERONIE...\n \nYour car has a flat tire. And you've got to pull over. You notice that the tire is completely flat and the spare you thought you had in the boot of the car is gone.\n \n")
      

       

    name = input("You're in a heavily wooded area and when you get your phone out there's no service.. as you start walking to find reception, you notice a humanlike creature in the distance staring straight at you.. they yell,  'Welcome friend, or at least I think. Come now out of the shadows.. what is your name?'      ")
    

    newPlayerStart(name) 
    print("")

    nav(newPlayer)
    
    print("") 
    
    response = input("A worse for wear figure hobbles over to you from out of the shadows and says the following: '\n \n" + newPlayer.name + ", what a sight for sore eyes. My name is Isaac and I need to ask you a favor. You see I went on a wild bender three nights ago and I seem to have lost my keys.. will you help me find them?'\n\nWhat do you say? \n[y or n]")

    print("")

    if response.lower() in ["yes","y","sure"]:
        print("'Thank you sooo much my dear good friend. I shall never forget this. Feel free to look around and explore the home. They've got to be here somewhere.' Isaac then pats his cloak for effect and starts searching around the entrance to the cave.")

    if response.lower() in ["n","nope", "no"]:
        print("'Please I beg of you!!!!!' Isaac starts to tear up. And you are now feeling a bit awkward... This person seems weird but you've got very limited choices... \n \nYou might as well explore the area for better signal. \n")

    user_movement(newPlayer)





game_start()

while movement != 'q':
    user_movement(newPlayer)
    
exit()

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
