#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alex8955'

from room import miscRoom, endRoom
import mechanics


class action(object):
    """base class for all actions
    all actions need to be plugged into the game.prompt"""

    def __init__(self, name, desc, helpTxt, shortcut = None, **kwargs):
        self.name = name
        self.desc = desc
        self.helpTxt = helpTxt
        self.shortcut = shortcut
        self.kwargs = kwargs

    def __str__(self):
        if self.name == "help":
            return self.helpTxt
        else:
            return self.desc + "See help {} for more details.".format(self.name)

class ghelp(action):
    def __init__(self, target = 'help'):
        super(ghelp, self).__init__(
            name = "help",
            desc = "Display help for a topic, or the general help file.",
            helpTxt = """The basic commands in Pygame are:
                help: Display help for a given topic, of the general help file if no topic is given.
                enter: Enter a door. (You can also just enter the number of the door).
                look: Display a rooms information.
                status: Display player's information.
                quit or exit: Exit the game, losing all progress."""
        )

class enter(action):
    newRoom = None

    def __init__(self, exit, room, player):
        super(enter, self).__init__(
            name = "enter",
            desc = "Enter the next room via the indicated door.",
            helpTxt = "[enter] <#>: enter the door associated with the number. The word enter is optional. ex: enter 1 OR 1."
        )
        if exit > room.exits:
            print "That is not a valid door."
        elif player.roomCt + mechanics.roll20() > 40:
            self.newRoom = endRoom(player)
        elif exit == 1:
            self.newRoom = miscRoom(room.doorDiffs[0])
        elif exit == 2:
            self.newRoom = miscRoom(room.doorDiffs[1])
        elif exit == 3:
            self.newRoom = miscRoom(room.doorDiffs[2])
        elif exit == 4:
            self.newRoom = miscRoom(room.doorDiffs[3])


class look(action):
    def __init__(self, room):
        super(look, self).__init__(
            name ="look",
            desc = "Look at the room and its exits.",
            helpTxt = "Displays the room's description and exit information."
        )
        print "\n" + room.desc
        room.nextRooms(room.exits)

class quit(action):
    def __init__(self, player):
        super(quit, self).__init__(
            name = "quit",
            desc = "Quit the game.",
            helpTxt = "Quit the game like a coward, losing all progress. Synonym of exit."
        )
        print "\nYou no longer have the strength to continue on. You hear what sounds like laughter far off in the dungeon as you lay down and die.\n"
        player.death()

class status(action):
    def __init__(self, player):
        super(status, self).__init__(
            name = "status",
            desc = "Print the players stats",
            helpTxt = "Display player information. Acceptable commands are stat, stats and status."
        )
        print player

def main():
    print help()


if __name__ == "__main__":
    main()