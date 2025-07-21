from room import Room
from character import Special_Enemy, Enemy
from item import Item
import time
from clear_screen import clear_screen

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

undead_knight = Enemy("UNDEAD KNIGHT", "A headless knight", 120, 40)
key_passage.set_character(undead_knight)

demon_king = Enemy("THE DEMON KING", "The final boss", 200, 100)
grand_hall.set_character(demon_king)

jingles = Special_Enemy("JINGLES", "The castle Jester", "???", "???")
key_room.set_character(jingles)

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
inventory = {}
door_lock = True
conversation = False
kill_count = 0

current_room = entrance
possible_directions = ["west", "east", "north", "south"]
dead = False
valid_input = False

clear_screen()
print("WELCOME TO THE GAME...")
time.sleep(2)
print("YOUR TOWN HAS BEEN DESTROYED BY THE DEMON KING - NOW YOU HAVE COME FOR REVENGE")
time.sleep(3)
print("OPENING THE CASTLE GATES, YOU ARRIVE AT THE ENTRANCE OF THE DEMON CASTLE.")
time.sleep(3)

while dead == False:
    clear_screen()
    current_room.get_details()
    print()
    inhabitant = current_room.get_character()
    room_item = current_room.get_item()
    if isinstance(inhabitant, Enemy) == False or isinstance(inhabitant, Special_Enemy) == True:
        current_room.get_directions()
    if inhabitant is not None:
        if isinstance(inhabitant, Special_Enemy) == True:
            print("\n— FRIENDLY ENCOUNTER —\n")
            inhabitant.describe()
            print(f"\nType [talk] to talk with [{inhabitant.name}]")
        else:
            print("— ENEMY ENCOUNTER —\n")
            inhabitant.describe()
    elif current_room.message is not None or room_item is not None:
        print("\nThere's something to inspect in this room.")
    print("\nType [help] for a list of commands!")
    command = input("> ")
    command = command.lower()
    print()
    clear_screen()
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
[check] - Allows you to see the stats of an enemy before fighting them
[inspect] - Inspects the room if there is something there (i.e. a message or any detail)
[stats] - Opens up the players stats including HP, equipped weapon and enemies killed
              
(COMMANDS CAN BE USED BY TYPING THE KEYWORDS SHOWN BY [] - NOTE: TYPE COMMANDS WITHOUT THE ENCASING [])          
""")
        input("Press enter to leave.")
    elif command == "stats":    
        if "Sword" in inventory:
            print(f"""PLAYER STATISTICS
              
    HP {player_health}/100
    WEAPON: Sword
    ENEMIES KILLED: {kill_count}
""")
        else:
            print(f"""PLAYER STATISTICS             
    
    HP {player_health}/100
    WEAPON: None
    ENEMIES KILLED: {kill_count}
""")
        input("Press enter to leave.")
    elif command == "inventory":
        if inventory == {}:
            print("Your inventory is empty.")
            time.sleep(1)
        else:
            while valid_input == False:
                for key,value in inventory.items():
                    print(key + ": " + value.get_item_description())
                print("\nType the item name to access it! (e.g. Type [Sword])")
                print("Which item would you like to access? (Type none to exit)")
                command = input("> ")
                command = command.title()
                if command in inventory:
                    choice_key = command
                    choice_item = inventory[command]
                    print("\nWhat would you like to do?\n")
                    print("Type [inspect] to see the item's description.")
                    print("Type [use] to use the selected item.")
                    command = input("> ")
                    print()
                    if command == "inspect":
                        choice_item.describe()
                        input("Press enter to leave.")
                        valid_input = True
                    elif command == "use":
                        if choice_item.get_item_type() == "KEY":
                            if current_room.get_name() == "Boss Passage":
                                print(f"You use the [{choice_item.get_item_name()}]!")
                                time.sleep(1.5)
                                door_lock = False
                                del inventory[choice_key]
                            else:
                                print("You can't use that here.")
                                time.sleep(1)
                        elif choice_item.get_item_type() == "CONSUMABLE":
                            print(f"You use the [{choice_item.get_item_name()}]!")
                            time.sleep(1.5)
                            player_health = 100
                            print("HP maxed out.")
                            time.sleep(1)
                            del inventory[choice_key]
                        else:
                            print("You can't use that item.")
                            time.sleep(1)
                        valid_input = True
                    else:
                        print("Invalid input.")
                        time.sleep(1)
                elif command == "None":
                    valid_input = True
                else: 
                    print("Invalid input.")
                    time.sleep(1)
            valid_input = False
    elif command == "inspect":
        print()
        if current_room.message is not None:
            print(current_room.get_message())
            input("Press enter to leave.")
        elif room_item is not None:
            if room_item.get_item_name() == "Golden Key":
                print("There's nothing to inspect in this room.")
                time.sleep(1)
            else:
                print("There's an item here!\n")
                time.sleep(1)
                room_item.describe()
                print()
                print("Type [take] to store the item or press enter to leave!")
                while command != "" and command != "take":
                    command = input("> ")
                    if command == "take":
                        print(f"You put the [{room_item.get_item_name()}] in your inventory")
                        inventory[room_item.get_item_name()] = room_item
                        current_room.set_item(None)
                    elif command == "":
                        pass
                    else:
                        print("Invalid input.")
                        print("Type [take] to store the item or press enter to leave!")
                        time.sleep(2)
        else:
            print("There's nothing to inspect in this room.")
            time.sleep(1)
    elif command in possible_directions:
        if current_room.get_name() == "Boss Passage" and command == "north":
            if door_lock == True:
                print("The door is locked. You can't go there.")
                time.sleep(1.5)
            else: 
                current_room = current_room.move(command)
        elif inhabitant is None or isinstance(inhabitant, Special_Enemy) == True:
            current_room = current_room.move(command)
        else: 
            print("You can't leave, there is an enemy in the room!")
            time.sleep(2)
    elif inhabitant is not None:    
        if command == "talk":
            if isinstance(inhabitant, Special_Enemy) == True:
                if conversation == False:
                    conversation = inhabitant.talk()
                    if conversation == True:
                        print(f"You got the [{room_item.get_item_name()}]!")
                        time.sleep(1.5)
                        inventory[room_item.get_item_name()] = room_item
                        current_room.set_item(None)
                else:
                    print(f"\n[{inhabitant.name} says]: You have what you need... now run off and die already! Ahahaha~!\n")
                    time.sleep(2)
            else:
                print("You cannot talk to an enemy.")
                time.sleep(1)
        elif command == "check":
            print(f"""[{inhabitant.name}]
HP {inhabitant.enemy_hp}    ATK {inhabitant.enemy_atk}
""")
            input("Press enter to leave.")
        elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Special_Enemy) == False:
                time.sleep(0.5)
                print("The fight begins!")
                if "Sword" in inventory:
                    fight_result, player_health = inhabitant.fight(sword_damage, player_health)
                else: 
                    fight_result, player_health = inhabitant.fight(player_damage, player_health)
                if fight_result == True:
                    kill_count += 1
                    print(f"You defeated {inhabitant.name}!")
                    print(f"Player health: [{player_health} HP]")
                    time.sleep(2)
                    if inhabitant.name == "THE DEMON KING":
                        print("WITH THE DEMON KING DEFEATED, YOUR MISSION IS COMPLETE")
                        time.sleep(1.5)
                        print("CONGRATULATIONS! YOU BEAT THE GAME!")
                        dead = True
                    current_room.set_character(None)
                else:
                    print(f"{inhabitant.name} defeated you.")
                    time.sleep(1)
                    print("Game over!")
                    dead = True
            else:
                if inhabitant.get_aggression() == 0:
                    print(f"\n[{inhabitant.name} says]: Woah there, I'm not here to fight.")
                    time.sleep(2)
                    inhabitant.set_aggression(20)
                elif inhabitant.get_aggression() == 20:
                    print(f"\n[{inhabitant.name} says]: You better chill out.")
                    time.sleep(2)
                    inhabitant.set_aggression(50)
                elif inhabitant.get_aggression() == 50:
                    print(f"\n[{inhabitant.name} says]: I'm warning you. You don't want to fight me.")
                    time.sleep(2)
                    inhabitant.set_aggression(100)
                elif inhabitant.get_aggression() == 100:
                    print(f"\n[{inhabitant.name} says]: Don't say I didn't warn you.\n")
                    time.sleep(1.5)
                    print("The fight begins!")
                    inhabitant.fight()
                    print(f"{inhabitant.name} defeated you.")
                    time.sleep(1)
                    print("Game over!")
                    dead = True     
        else:
            print("Please enter a valid command")
            time.sleep(1)
    elif command == "fight":
        print("There's no one here to fight.")
        time.sleep(1)
    else:
        print("Please enter a valid command")
        time.sleep(1)
        
