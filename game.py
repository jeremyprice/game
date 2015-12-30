#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex8955'

from player import player
from room import room

def enter(room):
    print room.desc


def main():
    print "Welcome to Pygame."
    print ""
    char = player()
    char.create()

    currentRoom = room()
    currentRoom.startRoom()
    enter(currentRoom)



if __name__ == "__main__":
    main()