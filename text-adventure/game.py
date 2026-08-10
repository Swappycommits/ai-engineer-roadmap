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
        self.health = 100
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
    def attack(self,enemy):
        enemy.health = enemy.health -10
        print(f"You attack! Enemy health is now {enemy.health}")

        if enemy.health<=0:
            print("Enemy Killed! You Win ")

        
class Enemy:
    def __init__(self,health,attack_power):
        self.health = health
        self.attack_power = attack_power
    def attack(self,player):
        player.health = player.health - self.attack_power
        print(f"Enemy attacked! your health is {player.health}")

        if player.health <=0:
            print("You die! Game Over")

       
        

player =Player(forest)
print(player.current_room.description)
player.move("north")
print(player.current_room.description)

player.move("north")

player.pick_up("rusty key")
print(player.inventory)
print(cave.items)

player.pick_up("sword")

goblin = Enemy(30, 5)
player.attack(goblin)
print(goblin.health)

goblin.attack(player)
print(player.health)

player.attack(goblin)
player.attack(goblin)
