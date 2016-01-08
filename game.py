#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import player
import room
import combat


def main():
    currentRoom = room.startRoom()

    print "Welcome to Pygame.\n"
    char = player.player()

    while char.chp > 0:
        monster = currentRoom.enter(char)
        while currentRoom.monCount > 0 and type(monster) != type(None):
            combat.combat(char, monster)
            currentRoom.monCount -= 1
            if char.chp < 1:
                char.death()
        currentRoom.rollChance(char)
        currentRoom.nextRooms(currentRoom.exits)
        currentRoom = currentRoom.chooseDoor(currentRoom.doorDiffs, currentRoom.exits, char)

    if char.chp < 1:
        char.death()


if __name__ == "__main__":
    main()