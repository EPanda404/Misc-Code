import random

point_total = 1_000

Available_Factions = ['Tribal', 'Farmers', 'Medieval', 'Ancient', 'Vikings', 'Dynasty', 'Renaissance', 'Pirate', 'Spooky', 'Wild West', 'Good', 'Evil', 'Legacy', 'Secret']
#Available_Factions = ['Renaissance', 'Pirate', 'Wild West']
Available_Units = []

unitlist = '''
Tribal
Clubber - 70
Protector - 80
Spear Thrower - 120
Stoner - 160
Bone Mage - 300
Cheiftan - 400
Mammoth - 2200

Farmers
Halfling - 50
Farmer - 80
Hay Baler - 140
Potionseller -340
Harvester - 500
Wheelbarrow - 1000
Scarecrow - 1200

Medieval
Bard - 60
Squire - 100
Archer - 140
Healer - 180
Knight - 650
Catapult - 1000
The King - 1500

Ancient
Shield Bearer - 100
Sarissa - 120
Snake Archer - 300
Ballista - 900
Minotaur - 1600
Zeus - 2000

Vikings
Headbutter - 90
Ice Archer - 160
Brawler - 220
Berserker - 250
Valkyrie - 500
Longship - 1000
Jarl - 1500

Dynasty
Samurai - 140
Firework Archer - 180
Monk - 250
Ninja - 500
Dragon - 1000
Hwacha - 1500
Monkey King - 2000

Renaissance
Painter - 50
Fencer - 150
Balloon Archer - 200
Musketeer - 250
Halberd - 400
Jouster - 1000
Da Vinci Tank - 4000

Pirate
Flintlock - 100
Blunderbuss - 160
Bomb Thrower - 250
Harpooner - 300
Cannon - 1000
Captain - 1500
Pirate Queen - 2500

Spooky
Skeleton Warrior - 80
Skeleton Archer - 180
Candlehead - 200
Vampire - 200
Pumpkin Catapult - 1000
Swordcaster - 1000
Reaper - 2500

Wild West
Dynamite Thrower - 100
Miner - 200
Cactus - 400
Gunslinger - 650
Lasso - 740
Deadeye - 900
Quickdraw - 1200

Good
Devout Gauntlet - 200
Celestial Aegis - 300
Radiant Glaive - 500
Righteous Paladin - 800
Divine Arbiter - 1000
Sacred Elephant - 2000
Chronomancer - 3000

Evil
Shadow Walker - 200
Exiled Sentinel - 300
Mad Mechanic - 500
Void Cultist - 800
Tempest Lich - 1000
Death Bringer - 2000
Void Monarch - 3000

Legacy
Peasant - 30
Banner Bearer - 100
Poacher - 120
Blowdarter - 220
Pike - 300
Barrel Roller - 350
Boxer - 450
Flag Bearer - 500
Pharaoh - 750
Wizard - 1200
Chariot - 1800
Thor - 2200
Tank - 6000
Super Boxer - 10000
Dark Peasant - 9999999
Super Peasant - 9999999

Secret
Ballooner - 120
Bomb On A Stick - 150
Fan Bearer - 200
Raptor - 200
The Teacher - 200
Jester - 300
Ball 'n' Chain - 350
Chu Ko Nu - 350
Executioner - 350
Shouter - 400
Taekwondo - 400
Raptor Rider - 450
Cheerleader - 500
Cupid - 500
Mace Spinner - 500
CLAMS - 500
Present Elf - 500
Ice Mage - 650
Bank Robbers - 850
Witch - 1000
Banshee - 1100
Necromancer - 1200
Wheelbarrow Dragon - 1400
Bomb Cannon - 1500
Skeleton Giant - 1700
Cavalry - 1800
Vlad - 1800
Gatling Gun - 2000
Blackbeard - 2600
Samurai Giant - 3000
Ullr - 3000
Lady Red Jade - 3500
Sensei - 3500
Shogun - 3500
Tree Giant - 4000
Artemis - 5500
Ice Giant - 6000
'''

add_Faction = ''
blank_check = True
faction_check = False
for line in unitlist.splitlines():
    if (line == ''):
        blank_check = True
        next

    elif (blank_check):
        add_Faction = line
        if (add_Faction in Available_Factions):
            faction_check = True
        else:
            faction_check = False
        blank_check = False

    elif (faction_check):
        splitLine = line.split('-')
        Available_Units.append((splitLine[0].strip(), int(splitLine[1].strip()), add_Faction))

#print(Available_Units)
Available_Units.sort(key = lambda x: x[1])



Team = []
while point_total >= Available_Units[0][1]:
    Remaining_Optional_Units = []
    for i in Available_Units:
        if(i[1] <= point_total):
            Remaining_Optional_Units.append(i)
        else:
            break

    index = random.randint(0, len(Remaining_Optional_Units) - 1)
    point_total = point_total - Remaining_Optional_Units[index][1]
    Team.append(Remaining_Optional_Units[index])

Team.sort(key = lambda x: x[1])
Team.sort(key = lambda x: x[2])
Team.sort(key = lambda x: x[0])

current_unit = Team[0]
current_unit_count = 0
for i in Team:
    if (i == current_unit):
        current_unit_count = current_unit_count + 1
    else:
        print(str(current_unit_count) + 'x ' + current_unit[2] + ' - ' + current_unit[0] + ' -  ' + str(current_unit[1]))
        current_unit = i
        current_unit_count = 1

print(str(current_unit_count) + 'x ' + current_unit[2] + ' - ' + current_unit[0] + ' -  ' + str(current_unit[1]))