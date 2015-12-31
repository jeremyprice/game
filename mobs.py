#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex8955'

import mechanics

class mob(object):
    """
    Abstract base class.
    All non-player characters in the game will be based off of this base class.
    """
    strg = agi = end = mgt = 0
    hp = arm = 0
    name = ""
    title = ""

    def calcArm(self, agi):
        "calculate Armor based on Agility"
        if agi % 2 == 0:
            arm = self.agi / 2
        else:
            arm = (agi - 1) / 2
        return arm

    def calcHP(self, end):
        "calculate HP based on Endurance"
        hp = 50 + (end * 5)
        return hp

    def calcStats(self):
        self.arm = self.calcArm(self.agi)
        self.hp = self.calcHP(self.end)

    def __init__(self):
        raise NotImplementedError

class goblin(mob):
    name = "Goblin"
    strg = 2
    agi = 2
    end = 2
    mgt = 1

    def __init__(self):
        self.calcStats()

class dragon(mob):
    name = "Dragon"
    strg = 18
    agi = 10
    end = 14
    mgt = 15

    def __init__(self):
       self.calcStats()



def randomMob(diff):
    """
    Handles rules for spawning monsters when entering a room. Logic is documented in readme
    spawnRoll will determine if a monster will spawn. mightRoll will determine the might of a monster if it does spawn.
    Both spawnRoll and mightRoll are handled differently based on difficulty of room.
    If a monster is spawned, a mob of appropriate might will be chose and returned. If a monster is not spawned, None will be returned.
    """
    spawnRoll = mechanics.roll100()
    mightRoll = mechanics.roll100()
    if diff == 0:
        if spawnRoll > 49:
            if mightRoll in range(0,66):
                #spawn easy
                pass
            elif mightRoll in range(67,98):
                #spawn medium
                pass
            elif mightRoll == 99:
                #spawn hard
                pass
        else:
            return None
    elif diff == 1:
        if spawnRoll > 49:
            if mightRoll in range(0,19):
                #spawn easy
                pass
            elif mightRoll in range(20,85):
                #spawn medium
                pass
            elif mightRoll in range(86,98)
                #spawn hard
                pass
            elif mightRoll == 99:
                #spawn very hard
                pass
        else:
            return None
    elif diff == 2:
        if spawnRoll > 19:
            if mightRoll in range(0,19):
                #spawn medium
                pass
            elif mightRoll in range(20,85):
                #spawn hard
                pass
            elif mightRoll in range(86,99)
                #spawn very hard
                pass
        else:
            return None
    else:
        #Difficulty 4 rooms have 100% spawn rate, so spawnRoll is not considered
        if mightRoll in range(0,39):
            #spawn hard
            pass
        elif mightRoll in range(40,94):
            #spawn very hard
            pass
        elif mightRoll in range(95,99)
            #spawn god-like
            pass



def main():
    monster = dragon()
    print monster.name
    print monster.hp
    print monster.arm


if __name__ == "__main__":
    main()