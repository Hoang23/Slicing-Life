init python:
    class InventoryItem:
        def __init__(self, name, value):
            self.name  = name
            self.value = value


    class Consumable(InventoryItem): # inherits from InventoryItem
        def __init__(self, name, value, hp_gain, intelligence_gain): # extends the previous class?
            InventoryItem.__init__(self, name, value)
            self.hp_gain = hp_gain
            self.intelligence_gain = intelligence_gain
            self.is_equipped = False # add an is_equipped attribute so that statements can be made on it


        def use(self, target):
            inventory.remove(self) # 'remove' removes object from a list
            target.addHP(self.hp_gain)
            target.addIntelligence(self.intelligence_gain)
            
            global selected_item
            selected_item = None

    class Equipable(InventoryItem):
        def __init__(self, name, value):
            InventoryItem.__init__(self, name, value)
            self.is_equipped = False
            self.equipped_to = None

        def equip(self, target):
            self.is_equipped = True
            self.equipped_to = target

        def unequip(self):
            self.is_equipped = False
            self.equipped_to = None
            

    class Weapon(Equipable):
        def __init__(self, name, value, weight, slot):
            Equipable.__init__(self, name, value)
            self.weight = weight
            self.slot = slot
            

        # override Equip method for Equipable
        def equip(self, target):
            Equipable.equip(self, target)
            target.equip_weapon(self, self.slot)

        # likewise override Unequipd method for Equipable
        def unequip(self): # target was added (might need to be removed)
            self.equipped_to.unequip_weapon(self.slot)
            Equipable.unequip(self)

           
            
            # Equipable.unequip(self)
            # target.unequip_weapon(self,self.slot)

            # self.equipped_to.unequip_weapon(self.wpn_type)
            # Equipable.unequip(self)
            

    class Armor(Equipable):
        def __init__(self, name, value, persuasion, charisma, slot):
            Equipable.__init__(self, name, value) # name and value inherited from equipable?
            self.persuasion = persuasion
            self.charisma = charisma
            self.slot = slot

        def equip(self, target):
            Equipable.equip(self, target)
            target.equip_armor(self, self.slot)

        def unequip(self): # target might need to be deleted
            self.equipped_to.unequip_armor(self.slot)
            Equipable.unequip(self)

            # Equipable.unequip(self)
            # target.unequip_armor(self,self.slot)
    # key item (zero value thus can't sell it)
    class KeyItem(InventoryItem):
        def __init__(self, name):
            InventoryItem.__init__(self, name, 0) # InventoryItem.__init__(self, name, 0)
