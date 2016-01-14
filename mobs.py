#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import mechanics
import json, random

#load mob data from external json file
with open('./resources/mobs.json') as mobjson:
    mobData = json.load(mobjson)

#initialize empty mob index
mobIndex = {0:[], 1:[], 2:[], 3:[], 4:[]}

#fill mob index. This is used by mobLoader() to build mobs.
for i, data in enumerate(mobData):
     mobIndex[data['stats']['bdiff']].append(i)


class mob(object):
    """
    all non-player characters in the game will be based off of this base class.
    mobs should be built with a base agility of 10. Slower than that can cause high agility players to have too easy of a time. Faster than that can be overwhelming. Agility has a major impact on difficulty, due to the way turns happen.
    will make stats a dictionary in the future.
    """

    def showHP(self):
        return "{} HP: {}/{} AP:{}/100".format(self.name, self.chp, self.hp, self.ap)

    def calcArm(self, end):
        "calculate Armor based on endurance"
        arm = end / 2
        return arm

    def calcHP(self, end):
        "calculate HP based on Endurance"
        hp = 50 + (end * 5)
        return hp

    def calcStats(self):
        self.arm = self.calcArm(self.end)
        self.hp = self.chp = self.calcHP(self.end)

    def attack(self, player):
        if self.strg - player.arm > 1:
            dmg = self.strg - player.arm
        else:
            dmg = 1
        if dmg > 1:
            print "The {} attacks you for {} damage!\n".format(self.name, dmg)
            player.chp -= dmg
        else:
            print "The {} lands a glancing blow!\n".format(self.name)
            player.chp -= 1
        self.ap -= 100

    def __init__(self, stats, name, desc):
        self.strg = stats['strg']
        self.agi = stats['agi']
        self.end = stats['end']
        self.bdiff = stats['bdiff']
        self.name = name
        self.desc = desc
        self.ap = self.hp = self.chp = self.arm = 0
        self.calcStats()


def pickMob(diff, debug=0):
    """
    Desc: handles rules for spawning monsters when entering a room. Logic is documented in readme.
    Called by: room.enter().

    Notes:
    spawnRoll will determine if a monster will spawn. mightRoll will determine the might of a monster if it does spawn.
    both spawnRoll and mightRoll are handled differently based on difficulty of room.
    if a monster is spawned, a mob of appropriate might will be chosen and returned. If a monster is not spawned, None will be returned.
    set debug = 1 for roll details
    diff -1 is for rooms that should never spawn a mob
    """
    spawnRoll = mechanics.roll100()
    mightRoll = mechanics.roll100()
    if diff == -1:
        return None
    elif diff == 0:
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if spawnRoll > 50:
            if mightRoll in range(1, 67):
                return mobLoader(0)
            elif mightRoll in range(68, 99):
                return mobLoader(1)
            elif mightRoll == 100:
                return mobLoader(2)
        else:
            return None
    elif diff == 1:
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if spawnRoll > 50:
            if mightRoll in range(1, 20):
                return mobLoader(0)
            elif mightRoll in range(21, 86):
                return mobLoader(1)
            elif mightRoll in range(87, 99):
                return mobLoader(2)
            elif mightRoll == 100:
                return mobLoader(3)
        else:
            return None
    elif diff == 2:
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if spawnRoll > 20:
            if mightRoll in range(1, 20):
                return mobLoader(1)
            elif mightRoll in range(21, 86):
                return mobLoader(2)
            elif mightRoll in range(87, 100):
                return mobLoader(3)
        else:
            return None
    else:
        # Difficulty 4 rooms have 100% spawn rate, so spawnRoll is not considered
        if debug == 1:
            print "Diff: {} \nmightRoll: {} \nspawnRoll: {}".format(diff, mightRoll, spawnRoll)
        if mightRoll in range(1, 40):
            return mobLoader(2)
        elif mightRoll in range(41, 95):
            return mobLoader(3)
        elif mightRoll in range(96, 100):
            return mobLoader(4)


def mobLoader(diff):
    """
    Desc: Constructs a mob object based on data loaded from ./resources/mobs.json
    Called by: mobs.pickMob()

    Notes:
    mobIndex[diff] uses the difficulty handed into the function to look into the mobIndex and get a list of index locations inside mobData that contain mobs of the requested difficulty.
    random.choice is used to pick one of those mobs at random
    chosenMob = mobData[] sets chosenMob to the data set for the randomly selected mob of the requested difficulty
    newMob = ... hands the data into the mob classes __init__ in its required format
    """
    chosenMob = mobData[random.choice(mobIndex[diff])]
    newMob = mob(chosenMob['stats'], chosenMob['name'], chosenMob['desc'])
    return newMob


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
