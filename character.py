import random
import threading
import time
from clear_screen import clear_screen

#Creating the character class
class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description

    #Description of Character
    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

#Creating the enemy class
class Enemy(Character):
    def __init__(self, char_name, char_description, health_points, attack_stats):
        super().__init__(char_name, char_description)
        self.enemy_hp = health_points
        self.enemy_atk = attack_stats
        self.enemy_full_hp = health_points

    #Input function for fighting
    def get_fight_input(self):
        global user_input
        user_input = None
        user_input = input()

    #Applying damage to the enemy after an attack
    def attack_round(self, damage):
        random_deviation = random.randint(-3, 3)
        damage += random_deviation
        if damage < 0:
            damage = 0
        self.enemy_hp -= damage
        return damage

    #Applying damage to the player after an attack
    def defend_round(self, damage, player_health):
        if damage > 0:
            random_deviation = random.randint(-3, 3)
            damage += random_deviation
        else:
            damage = 0
        return (player_health - damage), damage
    
    #Threading function to run the user's input simultaneously with the attack bar
    def threading_function(self):
        global input_thread
        input_thread = threading.Thread(target=self.get_fight_input)
        input_thread.daemon = True
        input_thread.start()

    #Combining the attack bar with the threading function to allow the user to attack
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
    
    #The player's defence in the fight
    def defend(self):
        print("Time your enter press with the attack of the enemy!\n")
        time.sleep(2)
        enemy_attack = random.random()*5
        while enemy_attack < 0.5:
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
        
    #The whole fighting function combining all related functions
    def fight(self, player_damage, player_health):
        while self.enemy_hp > 0 and player_health > 0:
            #Player attack
            time.sleep(1.5)
            clear_screen()
            print("\nATTACKING ROUND\n")
            time.sleep(1)
            attack = round(self.attack()/4)
            if attack >= 24:
                print("Critical hit!")
                attack *= 2
            attack *= player_damage
            attack = round(attack)
            attack = self.attack_round(attack)
            print(f"You dealt {attack} damage!\n")
            time.sleep(1.5)
            #Enemy attack
            if self.enemy_hp > 0:
                clear_screen()
                print("\nDEFENDING ROUND\n")
                time.sleep(1)
                defence = self.defend()
                if defence > 1:
                    defence = 1
                enemy_damage = round(self.enemy_atk*defence)
                player_health, damage_dealt = self.defend_round(enemy_damage, player_health)
                time.sleep(1)
                print(f"The enemy dealt {damage_dealt} damage!\n")
                if player_health < 0: 
                    player_health = 0
                time.sleep(1.5)
                print(f"You are on {player_health} HP")
                print(f"The enemy is on {self.enemy_hp} HP")
        #Checking if the player won or lost the fight
        if player_health == 0:
            return False, 0
        else:
            self.enemy_hp = self.enemy_full_hp
            return True, player_health
            
#Creating the special enemy class
class Special_Enemy(Enemy):
    def __init__(self, char_name, char_description, health_points, attack_stats):
        super().__init__(char_name, char_description, health_points, attack_stats)
        self.aggression = 0

    #Checking the player's input for the dialogue is valid
    def talk_validation(self, command):
        possible_options = ["1", "2", "3"]
        while command not in possible_options:
            print("Please enter either [1], [2] or [3].")
            command = input("> ")
        command = int(command)
        command -= 1
        return command
        
    #The player's conversation with the special enemy (JINGLES) and dialogue options
    def talk(self):
        key = False
        print(f"[{self.name} says]: Greetings PLAYER! What brings you round these parts?\n")
        time.sleep(2)
        #Dialogue 1
        dialogue_options = ["I'm here to take revenge for the destruction of my town.", "I'm here to kill your kind."]
        print(f"[1] - {dialogue_options[0]}")
        print(f"[2] - {dialogue_options[1]}")
        print("\nType [1] for option 1, [2] for option 2 or [3] to leave.")
        while True:
            command = input("> ")
            command = self.talk_validation(command)
            if command == 2:
                break
            clear_screen()
            print(f"\n[PLAYER says]: {dialogue_options[command]}")
            time.sleep(2)
            #Enemy response 1
            if command == 0:
                print(f"\n[{self.name} says]: Ohoho, I remember your town... NOT! [THE DEMON KING] has ruined many towns.\n")
            elif command == 1:
                print(f"\n[{self.name} says]: Bloodthirsty! No wonder you defeated so many demons already - even though they were weak! Ahahaha~!\n")
            time.sleep(3)
            #Dialogue 2
            dialogue_options = ["I saw a [Golden Key] here... do you have it?", "Just give me the [Golden Key] scum."]
            print(f"[1] - {dialogue_options[0]}")
            print(f"[2] - {dialogue_options[1]}")
            print("\nType [1] for option 1, [2] for option 2 or [3] to leave.")
            command = input("> ")
            command = self.talk_validation(command)
            if command == 2:
                break
            clear_screen()
            print(f"\n[PLAYER says]: {dialogue_options[command]}")
            time.sleep(2)
            #Enemy response 2
            if command == 2:
                print(f"\n[{self.name} says]: Yes, yes I do. But why would you think you need it?\n")
            elif command == 1:
                print(f"\n[{self.name} says]: Scary stuff! Do you even know what it's for?\n")
            time.sleep(2)
            #Dialogue 3
            dialogue_options = ["It opens the [Grand Hall].", "I mean it's an item so it's probably important."]
            print(f"[1] - {dialogue_options[0]}")
            print(f"[2] - {dialogue_options[1]}")
            print("\nType [1] for option 1, [2] for option 2 or [3] to leave.")
            command = input("> ")
            command = self.talk_validation(command)
            if command == 2:
                break
            clear_screen()
            print(f"\n[PLAYER says]: {dialogue_options[command]}")
            time.sleep(2)
            #Enemy response 3
            if command == 0:
                print(f"\n[{self.name} says]: Correct! For such foolishness, I have no qualms enabling your unhappy death at the hands of my King. Ahahaha~!\n")
                input("Press enter to leave.")
                time.sleep(0.5)
                key = True
                break
            elif command == 1:
                print(f"\n[{self.name} says]: Ahahaha~! For such humour the [Golden Key] is yours! It opens the door to the [Grand Hall] where you will meet (and die to) my King.\n")
                input("Press enter to leave.")
                time.sleep(0.5)
                key = True
                break
        return key
    
    #Getter and setter functions for aggression to allow fighting with the special enemy (Jingles)
    def set_aggression(self, aggression):
        self.aggression = aggression

    def get_aggression(self):
        return self.aggression
    
    #The unwinnable fighting function with Jingles
    def fight(self):
        #Player attack
        time.sleep(1)
        clear_screen()
        print("\nATTACKING ROUND\n")
        time.sleep(1)
        self.attack()
        print(f"[{self.name}] dodged!")
        time.sleep(0.5)
        print("You dealt 0 damage!\n")
        time.sleep(1)
        #Enemy attack
        clear_screen()
        print("\nDEFENDING ROUND\n")
        time.sleep(1)
        self.defend()
        print(f"[{self.name}] bypasses your block regardless!")
        time.sleep(0.5)
        print(f"The enemy dealt 100 damage!\n")
        time.sleep(1)
        print(f"You are on 0 HP")
        print(f"The enemy is on ??? HP")
        

        
