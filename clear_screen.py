#Importing from os to make the clear screen function
from os import system, name

#Clear screen function 
def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")