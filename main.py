from random import *

player_name = input("what's your name > ")
print(f"Hello, {player_name}, you are trapped in this dungeons")
print("to go to the next room type 'next room', to attack type 'attack' + name")
print("to check inventory, type 'inventory'")
print("to change weapon, typpe 'change weapon to' + weapon")

command = ""
douch = ""
kill = 0
xp = 0


def monster(enemy):
    global douch
    douch = entity(enemy, 20 + play.lvl + (randint(-5, 5)), randint(1, play.lvl + 5), lookup[enemy])
    print("there is a lvl " + str(douch.lvl) + " " + douch.name)
    action()


def action():
    global douch
    command = input(">").lower()
    if command == "":
        action()
    elif command == "next room":
        if douch != "":
            print("There's still a monster in this room!")
        else:
            room()
    elif command.split()[0] == "change":
        if len(command.split()) >= 3:
            change(command.split()[3])
    elif command == "inventory":
        print(invent.weapon)
    elif douch == "":
        print("theres no one here")
    elif command == "attack " + douch.name:
        attack()
    action()


def room():
    room = randint(1, 5)
    if (room == 1):
        monster("brick")
    elif (room == 2):
        monster("skeleton")
    elif (room == 3):
        monster("sans")
    elif (room == 4):
        monster("luis fonsi")
    elif (room == 5):
        print("Hey Vsauce, Micheal here")
        monster("vsauce")


def attack():
    global douch
    global kill
    global xp
    global inventory
    hit = randint(0, 10 + play.strength)
    if inven.weapon != []:
        # if inven.weapon[0] == "sword":
        print("you used " + inven.weapon[0] + ", +2 damage")
        hit += 2
    douch.health -= hit
    if douch.health <= 0:
        print("the " + douch.name + " died")

        heal()
        xp = randint(1, 50)
        play.xp += xp
        level()
        kill += 1
        inven.weapon.append(douch.wep)
        print("you got a " + douch.wep + "!")
        douch = ""
        print(inven.weapon)
    elif hit == 0:
        play.health -= 2
        print("you missed")
        print("you have " + str(play.health) + " health")
        if play.health <= 0:
            end()
    else:
        print("you hit " + douch.name + " for " + str(hit) + " damage!")
        print("the " + douch.name + " has " + str(douch.health) + " health")
    hit = randint(1, 4)
    if hit == 4 and douch != "":
        play.health -= 2
        print("You got hit")
        print("you have " + str(play.health) + " health")
        if play.health <= 0:
            end()
    elif douch != "":
        print(douch.name + " missed!")


def heal():
    play.health += 4
    if play.health > play.lvl + 20:
        play.health = play.lvl + 20
    print("You healed 4, you have " + str(play.health) + " health!")


class character:
    def __init__(self, health, lvl, xp, strength):
        self.health = health
        self.lvl = lvl
        self.xp = xp
        self.strength = strength
        self.inven = inventory()


play = character(20, 0, 0, 0)


class entity:
    def __init__(self, name, health, lvl, wep):
        self.name = name
        self.health = health
        self.lvl = lvl
        self.wep = wep


def end():
    print("You died :p")
    print("you killed " + str(kill) + " monsters!")


def level():
    global xp
    if play.xp >= 100:
        play.xp -= 100
        play.lvl += 1
        play.strength += 1
        print("You leveled up to " + str(play.lvl) + "!")
        print("Your health increase by 1")
        heal()
    else:
        print("you gained " + str(xp) + "xp, you have " + str(play.xp) + " experience")


lookup = {'skeleton': 'bow',
          'luis fonsi': 'fist',
          'sans': 'sword',
          'brick': 'brick',
          'vsauce': 'knowledge'}


def change(mw, player):
    j = 0
    for i in (0, len(player) - 1):
        if player.inven.weapon[i] == mw:
            j = i
    if player.inven.weapon[j] == mw:
        player.inven.weapon.insert(0, player.inven.weapon.pop(player.inven.weapon.index(player.inven.weapon[j])))
    else:
        print("you don't have that weapon")


class inventory:
    def __init__(self):
        self.weapon = []

action()