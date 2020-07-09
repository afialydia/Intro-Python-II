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


# test = Player("Carlyn", "backyard")

# print(test)