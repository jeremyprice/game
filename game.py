#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import player
import room
import combat
import actions

currentRoom = None

def prompt(player, room):
    """
    Desc: Main game prompt.
    Called by: main game loop

    Notes:
    returns either a room or None. If returning None, all necessary actions are taken within the called function.
    """
    command = None
    while not command:
        commandFull = raw_input(player.showHP() + ">")
        command = commandFull.split(' ')[0].lower()
        try:
            args = commandFull.split(' ', 1)[1].lower()
        except:
            args = None
    if command in ('1','2','3','4','enter'):
        if command in ('1','2','3','4'):
            command = int(command)
            #this seems hacky, but actions are classes and must return themselves. Making the new room a variable of the action instance allows it to return a room.
            return actions.enter(command, room, player).newRoom
        elif command == "enter":
            try:
                args = int(args)
                return actions.enter(args, room, player).newRoom
            except:
                print "That is not a valid door."
    elif command == 'help':
        #need to extend this to look at other commands
        gamehelp = actions.ghelp()
        print gamehelp.helpTxt
        return None
    elif command in ('l', 'look'):
        action = actions.look(room)
        return None
    elif command in ('quit', 'exit'):
        action = actions.quit(player)
    elif command in ('stat','stats','status'):
        action = actions.status(player)
        return None
    else:
        return None

def main():
    currentRoom = room.startRoom()

    print "Welcome to Pygame.\n"
    char = player.player()

    #while player is alive
    while char.chp > 0:
        #check to see if a monster is in the room, if so set it to monster
        monster = currentRoom.enter(char)
        #if there is a monster in the room, begin combat
        while currentRoom.monCount > 0 and type(monster) != type(None):
            combat.combat(char, monster)
            currentRoom.monCount -= 1
            if char.chp < 1:
                char.death()
        #check for chance event
        currentRoom.rollChance(char)
        #display next room options
        currentRoom.nextRooms(currentRoom.exits)
        #(re)initialize results to None
        result = None
        #display game prompt. If the user selects a new room, restart the loop
        while not result:
            result = prompt(char, currentRoom)
            if isinstance(result, room.maps):
                currentRoom = result



    if char.chp < 1:
        char.death()


if __name__ == "__main__":
    main()