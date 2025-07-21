class Item:
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type
        self.description = None

    def set_item_name(self, name):
        self.name = name

    def get_item_name(self):
        return self.name
    
    def set_item_type(self, item_type):
        self.item_type = item_type

    def get_item_type(self):
        return self.item_type
    
    def set_item_description(self, description):
        self.description = description
    
    def get_item_description(self):
        return self.description

    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")
        print(f"This item can be used as a [{self.item_type}]")

import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load the music file (replace 'music.mp3' with your file path)
pygame.mixer.music.load(music.mp3)

# Play the music in a loop (-1 means loop indefinitely)
pygame.mixer.music.play(-1)

# Keep the script running to allow the music to play
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
time.sleep(20)

# Ensure the music stops when the script finishes
pygame.mixer.music.stop()
pygame.quit()


    
    
        


    
