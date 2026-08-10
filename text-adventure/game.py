class Room:
    def __init__(self,description,exits,items):
        self.description = description
        self.exits = exits
        self.items = items
forest = Room("You are in a quiet forest clearing.", {},[])
cave = Room("You are in a dark cave.", {},['rusty key'])

forest.exits = {"north": cave}
cave.exits = {"south": forest}

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory=[]
    def move(self,direction):
        if direction in self.current_room.exits:
            self.current_room= self.current_room.exits[direction]
        else:
            print("you cant go that way")
    def pick_up(self,item_name):
        if item_name in self.current_room.items:
            self.current_room.items.remove(item_name)
            self.inventory.append(item_name)
        else:
            print(f"{item_name} is not in the room")
       
        

player =Player(forest)
print(player.current_room.description)
player.move("north")
print(player.current_room.description)

player.move("north")

player.pick_up("rusty key")
print(player.inventory)
print(cave.items)

player.pick_up("sword")