from room import Room
from character import Friend, Enemy
from item import Item

#Defining rooms
entrance = Room("Entrance")
entrance.set_description("A small, stone-walled room.")

westPassage = Room("West Passage")
westPassage.set_description("A passageway to the west.")

eastPassage = Room("East Passage")
eastPassage.set_description("A passageway to the east.")

weaponRoom = Room("Weapon Room")
weaponRoom.set_description("A silver sword lays on the floor, beckoning your wielding.")

bossPassage = Room("Boss Passage")
bossPassage.set_description("The way to the Demon King.")

grandHall = Room("Grand Hall")
grandHall.set_description("Where the Demon King lies.")

mainHallway = Room("Main Hallway")
mainHallway.set_description("The castle's main hallway.")

storage = Room("Storage")
storage.set_description("A storage room.")

prisonCell = Room("Prison Cell")
prisonCell.set_description("A prison cell - something gleams through a crack in the wall.")

balcony = Room("Balcony")
balcony.set_description("The desolate landscape left in ruins reminds you of your objective.")

keyPassage = Room("North Passage")
keyPassage.set_description("A passageway in the north.")

keyRoom = Room("Empty Room?")
keyRoom.set_description("A golden key lies on the floor.")

#Linking rooms
entrance.link_room(westPassage, "west")
entrance.link_room(eastPassage, "east")
entrance.link_room(bossPassage, "north")

bossPassage.link_room(entrance, "south")
bossPassage.link_room(grandHall, "north")

grandHall.link_room(bossPassage, "south")

westPassage.link_room(entrance, "east")
westPassage.link_room(weaponRoom, "south")
westPassage.link_room(prisonCell, "north")

prisonCell.link_room(westPassage, "south")

weaponRoom.link_room(westPassage, "north")

eastPassage.link_room(entrance, "west")
eastPassage.link_room(mainHallway, "north")

mainHallway.link_room(eastPassage, "south")
mainHallway.link_room(storage, "east")
mainHallway.link_room(balcony, "north")

storage.link_room(mainHallway, "west")

balcony.link_room(mainHallway, "east")
balcony.link_room(keyPassage, "west")

keyPassage.link_room(balcony, "north")
keyPassage.link_room(keyRoom, "south")

keyRoom.link_room(keyPassage, "north")

#Coding the Enemy
lower_demon = Enemy("Lower demon", "A low-class demon", 30, 10)
westPassage.set_character(lower_demon)
eastPassage.set_character(lower_demon)

upper_demon = Enemy("Upper demon", "An upper-class demon", 80,10)
bossPassage.set_character(upper_demon)

jester = Friend("Jester", "The castle Jester")
jester.set_conversation("Gidday")
keyRoom.set_character(jester)

#Coding items 
sword = Item("Sword")
sword.set_item_description("A simple silver sword")
weaponRoom.set_item(sword)

health_potion = Item("Health potion")
health_potion.set_item_description("Heals 10 HP")
storage.set_item(health_potion)

key = Item("Key")
key.set_item_description("I wonder what this opens")
keyRoom.set_item(key)

player_health = 100
player_damage = 10
bag = []

current_room = entrance
possible_directions = ["west", "east", "north", "south"]
dead = False
while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    room_item = current_room.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    if room_item is not None:
        room_item.describe()
    command = input("> ")
    
    if command in possible_directions:
        if inhabitant is None or isinstance(inhabitant, Friend) == True:
            current_room = current_room.move(command)
        else: 
            print("You can't leave, there is an enemy in the room!")
    elif room_item is not None:
        if command == "take":
            print(f"You put the {room_item.get_name()} in your bag")
            bag.append(room_item)
            current_room.set_item(None)
    elif inhabitant is not None:
        if command == "talk":
            inhabitant.talk()
        elif command == "fight":
            if isinstance(inhabitant, Enemy) == True:
                print("The fight begins!")
                if inhabitant.fight(player_damage, player_health) == True:
                    print(f"You defeated {inhabitant.name}!")
                    current_room.set_character(None)
                else:
                    print(f"{inhabitant.name} defeated you.")
                    print("Game over!")
                    dead = True
            else:
                print(f"{inhabitant.name} does not wish to fight.")
        elif command == "pat":
            if isinstance(inhabitant, Enemy) == True:
                print("I wouldn't do that if I were you.")
            else:
                inhabitant.pat()
        else:
            print("Please enter a valid command")
    else:
        print("Please enter a valid command")
        
