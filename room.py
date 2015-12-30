#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex8955'

import random

class room(object):
    __doc__ = "Class for generating and managing rooms in pygame."

    difficulty = 0
    desc = ""
    chance = 0

    def generate(self):
        diffRoll = random.randint(0,99)
        self.chance = random.randint(0,99)
        descRoll = random.randint(0, 4)

        if descRoll == 0:
            self.desc = "You walk walk through the door into a stone corridor, dimly lit by a flickering torch on the wall. Filthy water drips from the ceiling, and the walls are cast in shadows."
        elif descRoll == 1:
            self.desc = "Description 1"
        elif descRoll == 2:
            self.desc = "Description 2"
        elif descRoll == 3:
            self.desc = "Description 3"
        elif descRoll == 4:
            self.desc = "Description 4"
        else:
            self.desc = "There appears to be a problem generating a description."

        #scaffold for chance events
        if self.chance in range(0, 25):
            pass
            #some event
        elif self.chance in (50, 51):
            pass
            #some rare event
        elif self.chance == 99:
            pass
            #Some very rare event

        #the difficulty will be used to modify monster stats, and perhaps item drops. It uses ranges so that chances can be modified easily and is them bucketed for use.
        if diffRoll in range(0, 24):
            self.difficulty = 0
        elif diffRoll in range(25, 74):
            self.difficulty = 1
        elif diffRoll in range(75, 89):
            self.difficulty = 2
        else:
            self.difficulty = 3

    def startRoom(self):
        self.desc = "You awaken in a cramped stone cell. Your head aches and you have no memory of how you came to be here. There are a few items bundled together in the center of the room, and the door hangs slightly open. You hear the distant sound of creatures in the darkness beyond."



def main():
    room1 = room()
    room1.generate()

    print "Room debug info:"
    print "Difficulty - {},".format(room1.difficulty)
    print "Chance - {}.".format(room1.chance)
    print room1.desc


if __name__ == "__main__":
    main()