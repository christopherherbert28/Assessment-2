from room import Room
from character import Friend, Enemy
from item import Item
import time

#Defining rooms
entrance = Room("Entrance")
entrance.set_description("The start of your quest of vengence...\nA small, stone-walled room surrounded by passageways")

west_passage = Room("West Passage")
west_passage.set_description("A passageway to the west...\nA tight corridor illuminated by a single chandelier")

east_passage = Room("East Passage")
east_passage.set_description("A passageway to the east...\nA tight corridor illuminated by a single chandelier")

weapon_room = Room("Weapon Room")
weapon_room.set_description("The skeleton of a dead knight lays on the floor...\nA murky weapon's chamber")

boss_passage = Room("Boss Passage")
boss_passage.set_description("The way to the Demon King...\nA lavishly decorated passage to the castle's ruler brightly lit by candle light")

grand_hall = Room("Grand Hall")
grand_hall.set_description("Where the Demon King lies...\nA huge royal hall with the Demon King's throne in the centre")

main_hallway = Room("Main Hallway")
main_hallway.set_description("The castle's main hallway...\nA wide hallway connecting the castle's northern and southern sections")

storage = Room("Storage")
storage.set_description("A storage room...\nBoxes lay around haphazardly on the floor")

prison_cell = Room("Prison Cell")
prison_cell.set_description("A prison cell...\nScratches and cracks are littered over the walls from those it contained")

balcony = Room("Balcony")
balcony.set_description("A balcony overseeing the landscape...\nThe desolate landscape left in ruins reminds you of your objective")

key_passage = Room("North Passage")
key_passage.set_description("A passageway in the north...\nA corridor lined in alternating suits of armor and torch-light")

key_room = Room("Empty Room?")
key_room.set_description("A seemingly empty room...\nThe room is dimly lit by a crack in the wall")

#Linking rooms
entrance.link_room(west_passage, "west")
entrance.link_room(east_passage, "east")
entrance.link_room(boss_passage, "north")

boss_passage.link_room(entrance, "south")
boss_passage.link_room(grand_hall, "north")

grand_hall.link_room(boss_passage, "south")

west_passage.link_room(entrance, "east")
west_passage.link_room(weapon_room, "south")
west_passage.link_room(prison_cell, "north")

prison_cell.link_room(west_passage, "south")

weapon_room.link_room(west_passage, "north")

east_passage.link_room(entrance, "west")
east_passage.link_room(main_hallway, "north")

main_hallway.link_room(east_passage, "south")
main_hallway.link_room(storage, "east")
main_hallway.link_room(balcony, "north")

storage.link_room(main_hallway, "west")

balcony.link_room(main_hallway, "east")
balcony.link_room(key_passage, "west")

key_passage.link_room(balcony, "north")
key_passage.link_room(key_room, "south")

key_room.link_room(key_passage, "north")

#Coding the Enemy
lower_demon = Enemy("LOWER DEMON", "A low-class demon", 30, 20)
west_passage.set_character(lower_demon)
east_passage.set_character(lower_demon)

upper_demon = Enemy("UPPER DEMON", "An upper-class demon", 80, 25)
main_hallway.set_character(upper_demon)

gargoyle = Enemy("GARGOYLE", "The castle sentry", 50, 30)
balcony.set_character(gargoyle)

undead_knight = Enemy("UNDEAD KNIGHT", "A headless knight", 80, 40)
key_passage.set_character(undead_knight)

demon_king = Enemy("THE DEMON KING", "The final boss", 200, 100)
grand_hall.set_character(demon_king)

jester = Friend("Jester", "The castle Jester")
jester.set_conversation("Gidday")
key_room.set_character(jester)

#Coding items 
sword = Item("Sword", "WEAPON")
sword.set_item_description("Multiplies damage output by 1.5x")
weapon_room.set_item(sword)

health_potion = Item("Health Potion", "CONSUMABLE")
health_potion.set_item_description("Heals 100 HP")
storage.set_item(health_potion)

key = Item("Golden Key", "KEY")
key.set_item_description("I wonder what this opens")
key_room.set_item(key)

#Coding room messages 
entrance.set_message("""There's an inscription on the wall:

WEST - THE PATH OF THE WISE
EAST - THE PATH OF PROGRESS
""")

prison_cell.set_message("""Something catches your eye in a crack in the wall... 
a [Golden Key] glistens in the room beyond.
""")

player_health = 100
player_damage = 1
sword_damage = 1.5
bag = {}
door_lock = True

current_room = entrance
possible_directions = ["west", "east", "north", "south"]
dead = False
valid_input = False
print("WELCOME TO THE GAME...")
time.sleep(2)
print("YOUR TOWN HAS BEEN DESTROYED BY THE DEMON KING - NOW YOU HAVE COME FOR REVENGE")
time.sleep(3)
print("OPENING THE CASTLE GATES, YOU ARRIVE AT THE ENTRANCE OF THE DEMON CASTLE.")
time.sleep(3)

while dead == False:
    print("\n")
    current_room.get_details()
    print()
    inhabitant = current_room.get_character()
    room_item = current_room.get_item()
    if isinstance(inhabitant, Enemy) == False:
        current_room.get_directions()
    if inhabitant is not None:
        if isinstance(inhabitant, Enemy) == True:
            print("— ENEMY ENCOUNTER —\n")
        inhabitant.describe()
    if current_room.message is not None or room_item is not None:
        if isinstance(inhabitant, Enemy) == True:
            pass
        else:
            print("\nThere's something to inspect in this room.")
    print("\nType [Help] for a list of commands!")
    command = input("> ")
    command = command.lower()
    print()
    
    if command == "help":
        print("""
HELP MENU  
MOVEMENT:
YOU CAN MOVE BETWEEN ROOMS USING COMPASS DIRECTIONS (i.e. [north], [south], [east], [west])
N.B. YOU CAN'T LEAVE A ROOM IF THERE IS AN ENEMY PRESENT.

FIGHTING:
(ATTACKING)
TO ATTACK THE ENEMY, TIME YOUR ENTER PRESS WITH THE CENTRE <0> OF THE BAR SHOWN:
    ||||||||||||||||||||||||||||||||||||||||||||||||<0>||||||||||||||||||||||||||||||||||||||||||||||||

THE CLOSER THE ATTACK IS TO THE CENTRE, THE MORE DAMAGE IT DOES!
ATTACKS THAT ARE TIMED IN THE CENTRE ARE CRITICAL HITS - CRITICAL HITS DO 2X DAMAGE!
              
(DEFENDING)
TO DEFEND AGAINST THE ENEMY, TIME YOUR ENTER PRESS TO THE TIME SPECIFIED BY THE ENEMY'S ATTACK.
EXAMPLE: 
    [LOWER DEMON] Attack -> 1.51 seconds
    YOU MUST WAIT 1.51 SECONDS THEN PRESS ENTER

THE CLOSER YOUR TIMING IS TO THE ENEMY'S ATTACK, THE LESS DAMAGE YOU TAKE.
TIMING WITHIN 0.1 SECONDS OF THE ATTACK RESULTS IN A PERFECT BLOCK - NO DAMAGE TAKEN!   
                         
GENERAL COMMANDS:
[inventory] - Opens your inventory where you can see and access your items
[fight] - Begins a fight if there is an enemy in the room
[inspect] - Inspects the room if there is something there (i.e. a message or any detail)
              
(COMMANDS CAN BE USED BY TYPING THE KEYWORDS SHOWN)          
""")
        input("Press enter to leave.")
    elif command == "inspect":
        print()
        if current_room.message is not None:
            print(current_room.get_message())
            input("Press enter to leave.")
        elif room_item is not None:
            print("There's an item here!\n")
            room_item.describe()
            print()
            print("Type [take] to store the item or press enter to leave!")
            while command != "" and command != "take":
                command = input("> ")
                if command == "take":
                    print(f"You put the {room_item.get_item_name()} in your bag")
                    bag[room_item.get_item_name()] = room_item
                    current_room.set_item(None)
                elif command == "":
                    pass
                else:
                    print("Invalid input.")
                    print("Type [take] to store the item or press enter to leave!")
                    time.sleep(1)
        else:
            print("There's nothing to inspect in this room.")
            time.sleep(1)
    elif command in possible_directions:
        if current_room.get_name() == "Boss Passage" and command == "north":
            if door_lock == True:
                print("The door is locked. You can't go there.")
                time.sleep(1)
            else: 
                current_room = current_room.move(command)
        elif inhabitant is None or isinstance(inhabitant, Friend) == True:
            current_room = current_room.move(command)
        else: 
            print("You can't leave, there is an enemy in the room!")
            time.sleep(1)
    elif inhabitant is not None:
        if command == "talk":
            inhabitant.talk()
        elif command == "fight":
            if isinstance(inhabitant, Enemy) == True:
                time.sleep(0.5)
                print("The fight begins!")
                if "Sword" in bag:
                    fight_result, player_health = inhabitant.fight(sword_damage, player_health)
                else: 
                    fight_result, player_health = inhabitant.fight(player_damage, player_health)
                if fight_result == True:
                    print(f"You defeated {inhabitant.name}!")
                    print(f"Player health: [{player_health} HP]")
                    if inhabitant.name == "THE DEMON KING":
                        print("WITH THE DEMON KING DEFEATED, YOUR MISSION IS COMPLETE")
                        print("CONGRATULATIONS! YOU BEAT THE GAME!")
                        dead = True
                    current_room.set_character(None)
                else:
                    print(f"{inhabitant.name} defeated you.")
                    time.sleep(1)
                    print("Game over!")
                    dead = True
            else:
                print(f"{inhabitant.name} does not wish to fight.")
                time.sleep(1)
        else:
            print("Please enter a valid command")
            time.sleep(1)
    elif command == "inventory":
        if bag == {}:
            print("Your inventory is empty.")
            time.sleep(1)
        else:
            while valid_input == False:
                for key,value in bag.items():
                    print(key + ": " + value.get_item_description())
                print("\nType the item name to access it! (e.g. Type [Sword])")
                print("Which item would you like to access? (Type none to exit)")
                command = input("> ")
                command = command.title()
                if command in bag:
                    choice_key = command
                    choice_item = bag[command]
                    print("What would you like to do?\n")
                    print("Type [inspect] to see the item's description.")
                    print("Type [use] to use the selected item.")
                    command = input("> ")
                    if command == "inspect":
                        choice_item.describe()
                        valid_input = True
                    elif command == "use":
                        if choice_item.get_item_type() == "KEY":
                            if current_room.get_name() == "Boss Passage":
                                print(f"You use the [{choice_item.get_item_name()}]!")
                                door_lock = False
                                del bag[choice_key]
                            else:
                                print("You can't use that here.")
                        elif choice_item.get_item_type() == "CONSUMABLE":
                            print(f"You use the [{choice_item.get_item_name()}]!")
                            player_health = 100
                            print("HP maxed out.")
                            del bag[choice_key]
                        else:
                            print("You can't use that item.")
                        valid_input = True
                    else:
                        print("Invalid input.")
                elif command == "none":
                    valid_input = True
                else: 
                    print("Invalid input.")
            valid_input = False
    else:
        print("Please enter a valid command")
        
