import random
import threading
import time
class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    #Description of Character

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    #Set character dialogue

    def set_conversation(self, conversation):  
        self.conversation = conversation

    #Talk to the Character

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")

    #Fight with this Character

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description, health_points, attack_stats):
        super().__init__(char_name, char_description)
        self.enemy_hp = health_points
        self.enemy_atk = attack_stats
        self.enemy_full_hp = health_points

    def get_fight_input(self):
        global user_input
        user_input = None
        user_input = input("Enter something: ")

    def attack_round(self, damage):
        random_deviation = random.randint(-3, 3)
        damage += random_deviation
        self.enemy_hp -= damage

    def defend_round(self, damage, player_health):
        random_deviation = random.randint(-3, 3)
        damage += random_deviation
        return (player_health - damage), damage
    
    def threading_function(self):
        global input_thread
        input_thread = threading.Thread(target=self.get_fight_input)
        input_thread.daemon = True
        input_thread.start()

    def attack(self):
        print(f"{49*"|"}<0>{49*"|"}")
        input_bar = 0
        ascending = True
        self.threading_function()
        while True:
            if user_input is not None:
                if input_bar > 50:
                    attack = abs(100 - input_bar)
                else:
                    attack = input_bar
                attack *= 2
                break
            else:
                print(input_bar*"|")
                time.sleep(0.01)
                if input_bar < 100 and ascending == True:
                    input_bar += 1
                elif input_bar == 100:
                    input_bar -= 1
                    ascending = False
                elif input_bar > 0 and ascending == False:
                    input_bar -= 1
                elif input_bar == 0 and ascending == False:
                    input_bar += 1 
                    ascending = True
                print("\033[1A\033[2K", end = "")
        return attack
        


    def fight(self, player_damage, player_health):
        while self.enemy_hp > 0 and player_health > 0:
            #Player attack
            attack = round(self.attack()/4)
            if attack > 24:
                print("Critical hit!")
                attack *= 2
            attack *= player_damage
            self.attack_round(attack)
            print(f"You dealt {attack} damage!")
            """valid_input = False
            while valid_input != True:
                print("Choose your attack type! [heavy] or [light]")
                decision = input("> ")
                if decision == "heavy":
                    valid_input = True
                    if random.random() < 0.5:
                        attack = player_damage*3
                        self.attack_round(attack)
                        print("A heavy swing!")
                        print(f"You dealt {attack} damage!")
                    else:
                        print("You missed!")
                elif decision == "light":
                    valid_input = True
                    attack = player_damage
                    self.attack_round(attack)
                    print(f"You dealt {attack} damage!")
                else:
                    print("Invalid input! Please type [heavy] or [light]")"""
            #Enemy attack
            if self.enemy_hp > 0:
                player_health, damage_dealt = self.defend_round(self.enemy_atk, player_health)
                print(f"The enemy dealt {damage_dealt} damage!")
                if player_health < 0: 
                    player_health = 0
                print(f"You are on {player_health} HP")
                print(f"The enemy is on {self.enemy_hp} HP")
        if player_health == 0:
            return False, 0
        else:
            self.enemy_hp = self.enemy_full_hp
            return True, player_health
            
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

        
