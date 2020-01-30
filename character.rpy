init python:
    
    class Player:
        def __init__(self, hp, persuasion, perseverance, motivation, intelligence, charisma, weight, coin): 
            self.hp = hp
            self.persuasion = persuasion
            self.perseverance = perseverance
            self.max_hp = hp
            self.motivation = motivation
            self.intelligence = intelligence
            self.charisma = charisma
            self.hold = {"hold": None} # None # does not have to have one during the initialisation (A player can be a player object without a weapon)
            self.armor = {"head": None, "hold": None, "acc": None, "outfit": None}
            self.weight = weight
            self.coin = coin

        def buy(self, item):
            if self.coin >= item.value:
                self.coin -= item.value
                return True # return True (the player bought the item) - boolean is for conditional statements to figure whether it was bought or not 
            else:
                return False # The player didn't buy the item. - boolean is for conditional statements to figure whether it was bought or not 

            

        def addHP(self, amount):
            self.hp += amount
            if self.hp > self.max_hp: # don't want to hp to go over max hp
                self.hp = self.max_hp 

        def addIntelligence(self, amount):
            self.intelligence += amount
    

        # def calculateStats(self, amount, trait):
        #     self.hp += amount
        #     if self.hp > self.max_hp: # don't want to hp to go over max hp
        #         self.hp = self.max_hp 

        #     self.intelligence +=
            

        def equip_weapon(self, weapon, slot):
            if self.weapon != None: # remove weapon if another weapon exists
                self.unequip_weapon(slot)
            self.weapon[slot] = weapon
            self.weight += weapon.weight

        def unequip_weapon(self, slot):
            if self.weapon[slot] != None:
                self.atk -= self.weapon[slot].atk
                self.weapon[slot] = None

        def equip_armor(self, armor, slot):
            if self.armor[slot] != None:
                self.unequip_armor(slot)
            self.armor[slot] = armor
            self.charisma += armor.charisma
            self.persuasion += armor.persuasion

        def unequip_armor(self, slot):
            if self.armor[slot] != None:
                self.charisma -= self.armor[slot].charisma
                self.persuasion -= self.armor[slot].persuasion
                self.armor[slot] = None
