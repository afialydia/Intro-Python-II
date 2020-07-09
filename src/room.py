# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    """ Room has name and description attributes """ 
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to 
        self.s_to = s_to 
        self.e_to = e_to 
        self.w_to = w_to 
        
        # print('room. __init__')
    
    def __str__(self):
        return f" you are currently in the {self.name}."

   


# test = Room("Dining", "we eat here", )

# outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons", s_to="foyer")

# print(outside)