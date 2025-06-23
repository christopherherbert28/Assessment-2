from room import Room
from character import Friend, Enemy
from item import Item

#Defining rooms
entrance = Room("Entrance")
entrance.set_description("A small, stone-walled room.")

west_passage = Room("West Passage")
west_passage.set_description("A passageway to the west.")

east_passage = Room("East Passage")
east_passage.set_description("A passageway to the east.")

weapon_room = Room("Weapon Room")
weapon_room.set_description("A silver sword lays on the floor, beckoning your wielding.")

boss_passage = Room("Boss Passage")
boss_passage.set_description("The way to the Demon King.")

grand_hall = Room("Grand Hall")
grand_hall.set_description("Where the Demon King lies.")

main_hallway = Room("Main Hallway")
main_hallway.set_description("The castle's main hallway.")

storage = Room("Storage")
storage.set_description("A storage room.")

prison_cell = Room("Prison Cell")
prison_cell.set_description("A prison cell - something gleams through a crack in the wall.")

balcony = Room("Balcony")
balcony.set_description("The desolate landscape left in ruins reminds you of your objective.")

key_passage = Room("North Passage")
key_passage.set_description("A passageway in the north.")

key_room = Room("Empty Room?")
key_room.set_description("A golden key lies on the floor.")

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
lower_demon = Enemy("LOWER DEMON", "A low-class demon", 30, 10)
west_passage.set_character(lower_demon)
east_passage.set_character(lower_demon)

upper_demon = Enemy("UPPER DEMON", "An upper-class demon", 80,10)
main_hallway.set_character(upper_demon)

gargoyle = Enemy("GARGOYLE", "The castle sentry", 45, 20)
balcony.set_character(gargoyle)

undead_knight = Enemy("UNDEAD KNIGHT", "A headless knight", 80, 25)
key_passage.set_character(undead_knight)

demon_king = Enemy("THE DEMON KING", "The final boss", 200, 50)
grand_hall.set_character(demon_king)

jester = Friend("Jester", "The castle Jester")
jester.set_conversation("Gidday")
key_room.set_character(jester)

#Coding items 
sword = Item("Sword", "WEAPON")
sword.set_item_description("A simple silver sword")
weapon_room.set_item(sword)

health_potion = Item("Health potion", "CONSUMABLE")
health_potion.set_item_description("Heals 100 HP")
storage.set_item(health_potion)

key = Item("Golden Key", "KEY")
key.set_item_description("I wonder what this opens")
key_room.set_item(key)

player_health = 100
player_damage = 10
bag = {}
door_lock = True

current_room = entrance
possible_directions = ["west", "east", "north", "south"]
dead = False
valid_input= False
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
        if current_room.get_name == "Boss Passage" and command == "north":
            if door_lock == True:
                print("The door is locked. You can't go there.")
        elif inhabitant is None or isinstance(inhabitant, Friend) == True:
            current_room = current_room.move(command)
        else: 
            print("You can't leave, there is an enemy in the room!")
    elif room_item is not None:
        if command == "take":
            print(f"You put the {room_item.get_item_name()} in your bag")
            bag[room_item.get_item_name()] = room_item
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
    elif command == "inventory":
        for key,value in bag.items():
            print(key + ": " + value.get_item_description())
        while valid_input == False:
            print("Which item would you like to access? (Type none to exit)")
            command = input("> ")
            if command in bag:
                choice_item = bag[command]
                print("What would you like to do?")
                command = input("> ")
                if command == "inspect":
                    choice_item.describe()
                    valid_input = True
                elif command == "use":
                    if choice_item.get_item_type() == "KEY":
                        if current_room.get_name == "Boss Passage":
                            print(f"You use the [{choice_item.get_item_name}]!")
                            door_lock = False
                            del bag[choice_item]
                        else:
                            print("You can't use that here.")
                    elif choice_item.get_item_type() == "CONSUMABLE":
                        print(f"You use the [{choice_item.get_item_name}]!")
                        player_health = 100
                        print("HP maxed out.")
                        del bag[choice_item]
                    else:
                        print("You can't use that item.")
                    valid_input = True
                else:
                    print("Invalid input.")
            elif command == "none":
                valid_input = True
            else: 
                print("Invalid input.")
        valid_input == False
    else:
        print("Please enter a valid command")
        
