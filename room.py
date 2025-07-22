#Importing required functions from files and modules
import time
from clear_screen import clear_screen

class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.message = None

    #Getter and setter functions for description
    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    #Getter and setter functions for putting a character (i.e. Enemy) in the room
    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character
    
    #Getter and setter functions for putting an item in the room
    def set_item(self, item_name):
        self.item = item_name

    def get_item(self):
        return self.item

    #Getter and setter functions for messages in the room
    def set_message(self, message):
        self.message = message

    def get_message(self):
        return self.message

    #Getter and setter functions for name of the room
    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    #Linking the rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    #Describing the room 
    def get_details(self):
        time.sleep(0.4)
        print(self.get_name())
        time.sleep(0.9)
        print(self.get_description())

    #Informing the user of directions they can move in
    def get_directions(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")

    #Moving between rooms
    def move(self, direction):
        if direction in self.linked_rooms:
            clear_screen()
            return self.linked_rooms[direction]
        else: 
            print("You can't go that way.")
            time.sleep(1)
            return self

    
