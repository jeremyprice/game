#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex8955'

import player
import room
import random

def enter(room):
    print ""
    print room.desc

def roll100():
    return random.randint(0,99)

def main():
    print "Welcome to Pygame."
    print ""
    char = player.player()

    currentRoom = room.startRoom()
    enter(currentRoom)




if __name__ == "__main__":
    main()