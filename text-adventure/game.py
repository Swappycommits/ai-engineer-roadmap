class Room:
    def __init__(self,description,exits):
        self.description = description
        self.exits = exits
forest = Room("You are in a quiet forest clearing.", {})
cave = Room("You are in a dark cave.", {})

forest.exits = {"north": cave}
cave.exits = {"south": forest}

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
    def move(self,direction):
        if direction in self.current_room.exits:
            self.current_room= self.current_room.exits[direction]
        else:
            print("you cant go that way")
        
        

player =Player(forest)
print(player.current_room.description)
player.move("north")
print(player.current_room.description)

player.move("north")
