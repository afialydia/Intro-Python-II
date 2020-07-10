# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    """ Player class holds information about the players and what room that they are currently in """

    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

        # print('player.__init__')
    
    def __str__(self):
        return f"{self.name} is currently playing the game."

    def move(self, cmd):
    # print("You chose:", cmd)
        if cmd == 'n' and self.current_room.n_to != None:
            self.current_room = self.current_room.n_to

        elif cmd == 's' and self.current_room.s_to != None:
            self.current_room = self.current_room.s_to

        elif cmd == 'e' and self.current_room.e_to != None:
            self.current_room = self.current_room.e_to

        elif cmd == 'w' and self.current_room.w_to != None:
            self.current_room = self.current_room.w_to

        elif cmd == 'i':
            self.display_inventory()

        else:
            print('All you can see in this direction is darkness.. best not go there.')
            return

    def display_inventory(self):
        if len(self.items) <= 0:
            print('\nYou have nothing in your inventory!\n')
        else:
            output = ','.join(map(str, self.items))
            print(f"\nYou have: {output}\n")


    def getItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)

# add movementy to player as method rather than in game

# test = Player("Carlyn", "backyard")

# print(test)