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
        print(f"{48*"|"}<0>{48*"|"}")
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
    
    def defend(self):
        print("Time your enter press with the attack of the enemy!\n")
        time.sleep(2)
        enemy_attack = random.random()*5
        print(f"[{self.name}] Attack -> {enemy_attack:.2f} seconds")
        start = time.time()
        defence = input(f"Press enter in {enemy_attack:.2f} seconds")
        end = time.time()
        timing = end-start
        print(f"Time elapsed: {timing:.2f} seconds")
        defence = abs(timing-enemy_attack)
        time.sleep(0.25)
        if defence < 1 and defence > 0.1:
            print(f"You blocked the attack with {100-defence*100:.0f}% efficiency!\n")
        elif defence <= 0.1:
            print("Perfect block!\n")
            defence = 0
        else:
            print("You missed!\n")
        return defence
        
    def fight(self, player_damage, player_health):
        while self.enemy_hp > 0 and player_health > 0:
            #Player attack
            time.sleep(1)
            print("\nATTACKING ROUND\n")
            time.sleep(1)
            attack = round(self.attack()/4)
            if attack >= 24:
                print("Critical hit!")
                attack *= 2
            attack *= player_damage
            attack = round(attack)
            self.attack_round(attack)
            print(f"You dealt {attack} damage!\n")
            time.sleep(1)
            #Enemy attack
            if self.enemy_hp > 0:
                print("\nDEFENDING ROUND\n")
                time.sleep(1)
                defence = self.defend()
                if defence > 1:
                    defence = 1
                enemy_damage = round(self.enemy_atk*defence)
                player_health, damage_dealt = self.defend_round(enemy_damage, player_health)
                time.sleep(0.5)
                print(f"The enemy dealt {damage_dealt} damage!\n")
                if player_health < 0: 
                    player_health = 0
                time.sleep(1)
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

        
