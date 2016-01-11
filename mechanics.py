#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import actions

import random

def roll100():
    "Desc: roll values between 0 and 99"
    return random.randint(0,99)

def roll20():
    return random.randint(1,20)


def prompt(player, room, mob = None):
    #return -1 to let the calling function know not to print an "invalid command" message. This needs to be refined.
    command = None
    while not command:
        command = raw_input(player.showHP() + ">")
    if command in ('1','2','3','4'):
        return int(command)
    elif command == 'help':
        #need to extend this to look at other commands
        gamehelp = actions.ghelp()
        print gamehelp.helpTxt
        return -1
    elif command == "look":
        action = actions.look(room)
        return -1
    elif command in ('quit', 'exit'):
        action = actions.quit(player)
    else:
        return -1



def main():
    pass


if __name__ == "__main__":
    main()