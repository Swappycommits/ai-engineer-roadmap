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

       
        

player = Player(forest)
goblin = Enemy(30,5)
while True:
    command = input("> ").split()
    
    if command[0] == "quit":
        print("Thanks for playing!")
        break
    elif command[0] == 'go':
        if len(command) > 1:
            player.move(command[1])
            print(player.current_room.description)
            if player.current_room.items:
                print("Items here",player.current_room.items)
        else:
            print("Go where?")
    elif command[0] =='look':
        print(player.current_room.description)
        if player.current_room.items:
            print("Items Here",player.current_room.items)
    elif command[0] == 'take':
        if len(command) > 1:
            item_name =' '.join(command[1:])
            
            player.pick_up(item_name)
        else:
            print("Take what?")
    elif command[0] == "attack":
        player.attack(goblin)
    else:
        print("Give a Valid Command")
