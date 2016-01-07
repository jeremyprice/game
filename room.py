#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import random
import mechanics
import mobs

class map(object):
    __str__ = "Base class for generating and managing rooms in pygame."

    difficulty = 0
    desc = ""
    exits = 0
    monCount = 0
    door1diff = door2diff = door3diff = door4diff = 999

    def __init__(self):
        "This is an abstract base class and should not be used directly"
        raise NotImplementedError


    def rollChance(self, player):
        chance = mechanics.roll100()

        #scaffold for chance events
        if chance in range(0, 25):
            print "Chance event 1"

        elif chance in range(26, 30):
            if player.chp < player.hp:
                print "This room has a small fountain containing clean water. You quickly drink it, restoring your health."
                if (player.chp + 50) <= player.hp:
                    player.chp + 50
                else:
                    player.chp = player.hp
            else:
                print "This room has a small fountain containing clean water. You quickly drink it, but your health is already full."

        elif chance in (31, 50):
            print "Chance event 2"

        elif chance in (51, 52):
            print "You find a piece of armor on the floor in this room. You strap it onto yourself as best you can. You feel more protected. (Armor increased to {}).".format(player.arm+2)
            player.arm += 2

        elif chance in (53, 98):
            print "Chance event 3"

        elif chance == 99:
            pass
            #Some very rare event


    def rollDiff(self):
        """Determines the difficulty of a room.
        The difficulty will be used to modify monster stats, and perhaps item drops.
        It uses ranges so that chances can be modified easily and is then bucketed for use.
        """
        diffRoll = mechanics.roll100()
        if diffRoll in range(0, 24):
            return 0
        elif diffRoll in range(25, 74):
            return 1
        elif diffRoll in range(75, 89):
            return 2
        else:
            return 3


    def rollExits(self):
        "Determines how many exits a given room has."
        exitsRoll = mechanics.roll100()
        #exits are bucketed similar to difficulty
        if exitsRoll in range(0, 4):
            return 1
        elif exitsRoll in range(5, 54):
            return 2
        elif exitsRoll in range(55, 89):
            return 3
        else:
            return 4


    def rollNextRooms(self):
        "Chooses the difficulty for each next door. Ensures that each door is a different difficulty."
        #Need to change this to treat doorDiffs as an array
        self.door1diff = self.rollDiff()
        while self.door2diff == 999 or self.door2diff == self.door1diff:
            self.door2diff = self.rollDiff()
        while self.door3diff == 999 or self.door3diff == self.door1diff or self.door3diff == self.door2diff:
            self.door3diff = self.rollDiff()
        while self.door4diff == 999 or self.door4diff == self.door1diff or self.door4diff == self.door2diff or self.door4diff == self.door3diff:
            self.door4diff = self.rollDiff()


    def doorDesc(self, diff):
        "selects door descriptions"
        if diff == 0:
            return "This wooden door feels warm and inviting."
        elif diff == 1:
            return "This is a solid wooden door."
        elif diff == 2:
            return "You hear the sounds of some great beast behind this steel door."
        else:
            return "Blood seeps beneath this black stone door, and the sounds of something angry emanate from within."


    def nextRooms(self, exits):
        "displays exits for the next rooms."
        if exits > 1:
            print "This room has {} exits.".format(exits)
        else:
            print "This room only has 1 exit."
        print "1) {}".format(self.doorDesc(self.door1diff))
        if exits > 1:
            print "2) {}".format(self.doorDesc(self.door2diff))
        if exits > 2:
            print "3) {}".format(self.doorDesc(self.door3diff))
        if exits > 3:
            print "4) {}".format(self.doorDesc(self.door4diff))

    def chooseDoor(self, d1d, d2d, d3d, d4d, exits):
        "Prompts player for door choice and returns the new room."
        newRoom = None
        while not newRoom:
            choice = int(raw_input("Which exit will you take? "))
            if choice == 1:
                newRoom = miscRoom(d1d)
            elif choice == 2:
                if exits > 1:
                    newRoom = miscRoom(d2d)
                else:
                    print "That is not a valid choice."
            elif choice == 3:
                if exits > 2:
                    newRoom = miscRoom(d3d)
                else:
                    print "That is not a valid choice."
            elif choice == 4:
                if exits > 3:
                    newRoom = miscRoom(d4d)
                else:
                    print "That is not a valid choice."
            else:
                print "That is not a valid choice."
        return newRoom



    def enter(self, player):
        print ""
        print self.desc
        monster = mobs.pickMob(self.difficulty)
        if type(monster) != type(None):
            self.monCount += 1
            print monster.desc
            print ""
            return monster
        else:
            print "You appear to be alone here\n"
            return None
        self.rollChance(player)



class miscRoom(map):

    def rollDesc(self):
        """
        Randomly assigned descriptions to rooms. In the future, I plan to move these out to a flat file which will be read from.
        """
        descRoll = random.randint(0, 4)
        if descRoll == 0:
            self.desc = "You walk through the door into a stone corridor, dimly lit by a flickering torch on the wall. Filthy water drips from the ceiling, and the walls are cast in shadows."
        elif descRoll == 1:
            self.desc = "You enter into a dark room. You can barely make out a partially collapsed wall. The smell of earth fills your nose."
        elif descRoll == 2:
            self.desc = "You walk into a warm room. It appears there was a fire burning here just moments ago."
        elif descRoll == 3:
            self.desc = "You walk through the door into a room strewn with the remains of a bloody battle. Your feet stick to the floor, and your nose is filled with the smell of death."
        elif descRoll == 4:
            self.desc = "Your enter into what appears to have been a great hall, long ago. The room has been heavily looted, but the high ceilings provide a stark contrast to the cramped tunnels you have been traveling."
        else:
            self.desc = "There appears to be a problem generating a description."


    def __init__(self, diff):
        self.difficulty = diff
        self.rollDesc()
        self.exits = self.rollExits()
        self.rollNextRooms()
        pass



class startRoom(map):

    def __init__(self):
        self.exits = 1
        self.desc = "You awaken in a cramped stone cell. Your head aches and you have no memory of how you came to be here. There are a few items bundled together in the center of the room, and the door hangs slightly open. You hear the distant sound of creatures in the darkness beyond."
        self.door1diff = 1
        self.difficulty = -1
        pass



class endRoom(map):

    def __init__(self):
        self.desc = "You step through the door and are immediately blinded by bright light. You smell fresh air and feel a breeze on your bloody and bruised face. As your eyes adjust, you see stone steps leading up to the surface. You've survived."
        self.difficulty = -1

def main():
    room1 = miscRoom(1)

    print "Room debug info:"
    print "Difficulty - {},".format(room1.difficulty)
    print "Exits - {}.".format(room1.exits)
    print "Door 1 diff: {}".format(room1.door1diff)
    print "Door 2 diff: {}".format(room1.door2diff)
    print "Door 3 diff: {}".format(room1.door3diff)
    print "Door 4 diff: {}".format(room1.door4diff)


if __name__ == "__main__":
    main()