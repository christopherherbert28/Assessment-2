import random
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

    def attack_round(self, damage):
        self.enemy_hp -= damage

    def defend_round(self, damage, player_health):
        return (player_health - damage), damage

    def fight(self, player_damage, player_health):
        while self.enemy_hp > 0 and player_health > 0:
            #Player attack
            valid_input = False
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
                    print("Invalid input! Please type [heavy] or [light]")
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

        
