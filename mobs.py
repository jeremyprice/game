#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import mechanics


class mob(object):
    """
    Abstract base class.
    All non-player characters in the game will be based off of this base class.
    Mobs should be built with a base agility of 10. Slower than that can cause high agility players to have too easy of a time. Faster than that can be overwhelming. Agility has a major impact on difficulty, due to the way turns happen.
    """
    strg = agi = end = bdiff = ap = hp = chp = arm = 0
    name = title = desc = ""

    def calcArm(self, end):
        "calculate Armor based on Agility"
        if end % 2 == 0:
            arm = end / 2
        else:
            arm = (end - 1) / 2
        return arm

    def calcHP(self, end):
        "calculate HP based on Endurance"
        hp = 50 + (end * 5)
        return hp

    def calcStats(self):
        self.arm = self.calcArm(self.end)
        self.hp = self.chp = self.calcHP(self.end)

    def __init__(self):
        raise NotImplementedError


### Monster definitions ###
# in the future, these will be reworked into a flat file

class goblin(mob):
    name = "Goblin"
    strg = 2
    agi = 10
    end = 2
    bdiff = 0
    desc = "A small green goblin is here, scratching himself"

    def __init__(self):
        self.calcStats()


class skeleton(mob):
    name = "Skeleton"
    strg = 4
    agi = 10
    end = 4
    bdiff = 1
    desc = "A skeleton is here, rattling his bones"

    def __init__(self):
        self.calcStats()


class orc(mob):
    name = "Orc"
    strg = 8
    agi = 10
    end = 4
    bdiff = 2
    desc = "A large green orc is here, banging his shield"

    def __init__(self):
        self.calcStats()


class elemental(mob):
    name = "Elemental"
    strg = 10
    agi = 10
    end = 8
    bdiff = 3
    desc = "A fire elemental is here, burning furiously"

    def __init__(self):
        self.calcStats()


class dragon(mob):
    name = "Dragon"
    strg = 18
    agi = 8
    end = 14
    bdiff = 4
    desc = "A huge dragon is here, chewing the bones of its last victim"

    def __init__(self):
        self.calcStats()


def pickMob(diff, debug=0):
    """
    Handles rules for spawning monsters when entering a room. Logic is documented in readme
    spawnRoll will determine if a monster will spawn. mightRoll will determine the might of a monster if it does spawn.
    Both spawnRoll and mightRoll are handled differently based on difficulty of room.
    If a monster is spawned, a mob of appropriate might will be chosen and returned. If a monster is not spawned, None will be returned.
    Set debug = 1 for roll details
    diff -1 is for rooms that should never spawn a mob
    """
    spawnRoll = mechanics.roll100()
    mightRoll = mechanics.roll100()
    if diff == -1:
        return None
    elif diff == 0:
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if spawnRoll > 49:
            if mightRoll in range(0, 66):
                return spawnMob(0, mightRoll)
            elif mightRoll in range(67, 98):
                return spawnMob(1, mightRoll)
            elif mightRoll == 99:
                return spawnMob(2, mightRoll)
        else:
            return None
    elif diff == 1:
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if spawnRoll > 49:
            if mightRoll in range(0, 19):
                return spawnMob(0, mightRoll)
            elif mightRoll in range(20, 85):
                return spawnMob(1, mightRoll)
            elif mightRoll in range(86, 98):
                return spawnMob(2, mightRoll)
            elif mightRoll == 99:
                return spawnMob(3, mightRoll)
        else:
            return None
    elif diff == 2:
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if spawnRoll > 19:
            if mightRoll in range(0, 19):
                return spawnMob(1, mightRoll)
            elif mightRoll in range(20, 85):
                return spawnMob(2, mightRoll)
            elif mightRoll in range(86, 99):
                return spawnMob(3, mightRoll)
        else:
            return None
    else:
        # Difficulty 4 rooms have 100% spawn rate, so spawnRoll is not considered
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if mightRoll in range(0, 39):
            # spawn hard
            return spawnMob(2, mightRoll)
        elif mightRoll in range(40, 94):
            # spawn very hard
            return spawnMob(3, mightRoll)
        elif mightRoll in range(95, 99):
            # spawn god-like
            return spawnMob(4, mightRoll)


def spawnMob(diff, might):
    """
    Returns a mob for a given difficulty
    In the future, this will have several mob types per difficulty and use something like random.choice to pick one.
    This function will call to the title assignment function, once implemented
    """
    if diff == 0:
        return goblin()
    elif diff == 1:
        return skeleton()
    elif diff == 2:
        return orc()
    elif diff == 3:
        return elemental()
    elif diff == 4:
        return dragon()


def main():
    monster = pickMob(1, 1)
    if type(monster) != type(None):
        print "Name: {} \nHP: {} \nArmor: {} \nBase Diff: {}".format(monster.name, monster.hp, monster.arm,
                                                                     monster.bdiff)
        print monster.desc
    else:
        print "No mob spawned"


if __name__ == "__main__":
    main()
