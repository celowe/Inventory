#Inventory Group Code
#Cecil Lowe

####################### Weapon Object ##############################

class Weapon(object):
    def __init__(self, name, cost, weight, numDie, typeDie, critRoll, critDmg, rang, typ):
        self.name = name
        self.cost = cost
        self.weight = weight
        self.numDie = numDie
        self.typeDie = typeDie
        self.critRoll = critRoll
        self.critDmg = critDmg
        self.rang = rang
        self.typ = typ

    def __str__(self):
        rep = self.name + "\n" + "Cost: " + str(self.cost) + "\n"
        return rep

    
###################### Armor Object #################################

class Armor(object):
    def __init__(self, name, cost, prot, dexBonus, armrPen, spellRes, weight):
        self.name = name
        self.cost = cost
        self.prot = prot
        self.dexBonus = dexBonus
        self.armrPen = armrPen
        self.spellRes = spellRes
        self.weight = weight

    def __str__(self):
        rep = self.name + "\n" + "Cost: " + str(self.cost) + "\n"
        return rep

###################### Consumables ##################################

class Consumable(object):
    def __init__(self, name, cost, weight):
        self.name = name
        self.cost = cost
        self.weight = weight

    def __str__(self):
        rep = self.name + "\n" + "Cost: " + str(self.cost) + "\n"
        return rep
    
########################### Item Object #############################

class Item(object):
    def __init__(self, name, cost, weight):
        self.name = name
        self.cost = cost
        self.weight = weight

    def __str__(self):
        rep = self.name + "\n" + "Cost: " + str(self.cost) + "\n"
        return rep

    
#Dictonarys
class Inventory(object):
    def __init__(self):
        self.items = {}
        self.weapons = {}
        self.armors = {}
        self.consumables = {}
        
# Adding Items into dictonary
    def add_item(self, aItem):
        self.items[aItem.name] = aItem
        
    def add_weapon(self,aWeapon):
        self.weapons[aWeapon.name] = aWeapon

    def add_armor(self, aArmor):
        self.armors[aArmor.name] = aArmor

    def add_consumable(self, aConsumable):
        self.consumables[aConsumable.name] = aConsumable

#Print item functions
    def print_items(self):
        listOfKeys = self.items.keys()
        for itemName in listOfKeys:
            print(self.items[itemName])

    def print_armors(self):
        listOfKeys = self.armors.keys()
        for itemName in listOfKeys:
            print(self.armors[itemName])
    
    def print_weapons(self):
        listOfKeys = self.weapons.keys()
        for itemName in listOfKeys:
            print(self.weapons[itemName])

    def print_consumables(self):
        listOfKeys = self.consumables.keys()
        for itemName in listOfKeys:
            print(self.consumables[itemName])

#============ Adding spread sheet files to dictonaries ===================================================>

myInventory = Inventory()
weapon_file = open("Item List - Weapons.txt", "r")
for line in weapon_file:
    line.strip()
    data = line.split(',')
    temp_weapon = Weapon(data[0], int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7]), data[8])
    myInventory.add_weapon(temp_weapon)
weapon_file.close()
      
armor_file = open("Item List - Armor.txt", "r")
for line in armor_file:
    line.strip()
    data = line.split(',')
    temp_armor = Armor(data[0], int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]))
    myInventory.add_armor(temp_armor)
armor_file.close()

item_file = open("Item List - Goods.txt", "r")
for line in item_file:
    line.strip()
    data = line.split(',')
    temp_item = Item(data[0], int(float(data[1])), int(data[2]))
    myInventory.add_item(temp_item)
item_file.close()

consumables_file = open("Item List - Consumables.txt", "r")
for line in consumables_file:
    line.strip()
    data = line.split(',')
    temp_consumable = Consumable(data[0], int(float((data[1]))), int(float(data[2])))
    myInventory.add_consumable(temp_consumable)
consumables_file.close() 

#Print functions for objects
print("====== Weapons =======")
myInventory.print_weapons()
print("====== Goods ======")
myInventory.print_items()
print("====== Armor =======")
myInventory.print_armors()
print("====== Consumables ======")
myInventory.print_consumables()

input()

############# =END= ##############
