#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import player
import room
import combat


def main():
    currentRoom = room.startRoom()

    print "Welcome to Pygame."
    print ""
    char = player.player()

    while char.chp > 0:
        monster = currentRoom.enter(char)
        while currentRoom.monCount > 0 and type(monster) != type(None):
            combat.combat(char, monster)
            currentRoom.monCount -= 1
            print ""
            if char.chp < 1:
                print "You have died, like many before you."
                exit()
        currentRoom.nextRooms(currentRoom.exits)
        currentRoom = currentRoom.chooseDoor(currentRoom.door1diff, currentRoom.door2diff, currentRoom.door3diff, currentRoom.door4diff, currentRoom.exits)

    if char.chp < 1:
        print "You have died, like many before you."
        exit()


if __name__ == "__main__":
    main()