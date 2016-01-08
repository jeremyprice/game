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
    doorDiffs = [999,999,999,999]

    def __init__(self):
        "This is an abstract base class and should not be used directly"
        raise NotImplementedError

    def rollChance(self, player):
        """
        Desc: rolls and enacts chance events.
        Called by: Main game loop in game.

        Notes:
        chance events have a chance of occurring once per room.
        chance events occur after a battle and before the next door is chosen.
        """
        chance = mechanics.roll100()
        # scaffold for chance events
        if chance in range(0, 24):
            # nothing. 25% chance of no event.
            pass
        elif chance in range(25, 29):
            if player.chp < player.hp:
                print "This room has a small fountain containing clean water. You quickly drink it, restoring your health."
                if (player.chp + 50) <= player.hp:
                    player.chp += 50
                else:
                    player.chp = player.hp
            else:
                print "This room has a small fountain containing clean water. You quickly drink it, but your health is already full."
            player.showHP()

        elif chance in range(30, 34):
            print "An imp throws a rock at you before disappearing in a puff of smoke."
            player.chp -= 5
            player.showHP()

        elif chance in range(35, 49):
            pass

        elif chance in (50, 51):
            print "You find a piece of armor on the floor in this room. You strap it onto yourself as best you can. You feel more protected. (Armor increased to {}).".format(
                player.arm + 2)
            player.arm += 2

        elif chance in range(52, 95):
            pass

        elif chance in (96, 97):
            # Keep this in mind once levels are implemented
            print "A lost spirit appears to you. 'I perished here, like many before me. I give you my blessing, that you may find freedom again'. As the spirit disappears, you feel slightly more healthy. (Health permanently increased to  {}).".format(
                player.hp + 30)
            player.hp += 30
            if (player.chp + 30) <= player.hp:
                player.chp += 30
            else:
                player.chp = player.hp
            player.showHP()

        elif chance == 98:
            print "You find a pair of leather shoes to protect your bare feet, allowing you to move slightly more quickly. (Agility increased to {}.)".format(
                player.agi + 1)
            player.agi += 1

        elif chance == 99:
            pass
            # Some very rare event

    def rollDiff(self):
        """
        Desc: determines the difficulty of a room.
        Called by: room.map.rollNextRooms()

        Notes:
        the difficulty will be used to modify monster stats, and perhaps item drops.
        it uses ranges so that chances can be modified easily and is then bucketed for use.
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
        """
        Desc: determines how many exits a given room has.
        Called by: room.map.miscRoom.__init__()
        """
        exitsRoll = mechanics.roll100()
        # exits are bucketed similar to difficulty
        if exitsRoll in range(0, 4):
            return 1
        elif exitsRoll in range(5, 54):
            return 2
        elif exitsRoll in range(55, 89):
            return 3
        else:
            return 4

    def rollNextRooms(self):
        """
        Desc: chooses the difficulty for each next door.
        Called by: room.map.miscRoom.__init__()

        Notes:
        ensures that each door is a different difficulty."""
        self.doorDiffs[0] = self.rollDiff()
        while self.doorDiffs[1] == 999 or self.doorDiffs[1] == self.doorDiffs[0]:
            self.doorDiffs[1] = self.rollDiff()
        while self.doorDiffs[2] == 999 or self.doorDiffs[2] == self.doorDiffs[0] or self.doorDiffs[2] == self.doorDiffs[1]:
            self.doorDiffs[2] = self.rollDiff()
        while self.doorDiffs[3] == 999 or self.doorDiffs[3] == self.doorDiffs[0] or self.doorDiffs[3] == self.doorDiffs[1] or self.doorDiffs[3] == self.doorDiffs[2]:
            self.doorDiffs[3] = self.rollDiff()

    def doorDesc(self, diff):
        """
        Desc: returns door descriptions
        Called by: room.map.nextRooms()
        """
        if diff == 0:
            return "This wooden door feels warm and inviting."
        elif diff == 1:
            return "This is a solid wooden door."
        elif diff == 2:
            return "You hear the sounds of some great beast behind this steel door."
        else:
            return "Blood seeps beneath this black stone door, and the sounds of something angry emanate from within."

    def nextRooms(self, exits):
        """
        Desc: displays exits for the next rooms.
        Called by: room.map.miscRoom.__init__() and main game loop in game
        """
        if exits > 1:
            print ""
            print "This room has {} exits.".format(exits)
        else:
            print ""
            print "This room only has 1 exit."
        print "1) {}".format(self.doorDesc(self.doorDiffs[0]))
        if exits > 1:
            print "2) {}".format(self.doorDesc(self.doorDiffs[1]))
        if exits > 2:
            print "3) {}".format(self.doorDesc(self.doorDiffs[2]))
        if exits > 3:
            print "4) {}".format(self.doorDesc(self.doorDiffs[3]))

    def chooseDoor(self, doorDiffs, exits):
        """
        Desc: prompts player for door choice and returns the new room.
        Called by: main game loop in game

        Notes:
        receives the difficulty number for each possible door but only the actual number of exits to display.
        this is the main prompt for the player currently. it will have its functionality greatly expanded and may need to move into mechanics
        """
        newRoom = None
        choice = None
        while not newRoom:
            while type(choice) != int:
                try:
                    choice = raw_input("Which exit will you take? ")
                    choice = int(choice)
                except:
                    if type(choice) == str:
                        if choice.lower() in ['exit', 'quit']:
                            print "\nYou no longer have the strength to continue on. You hear what sounds like laughter far off in the dungeon as you lay down and die.\n"
                            exit()
                    print "That is not a valid choice."
            if choice > exits:
                print "That is not a valid choice."
                choice = None
            elif choice == 1:
                newRoom = miscRoom(doorDiffs[0])
            elif choice == 2:
                newRoom = miscRoom(doorDiffs[1])
            elif choice == 3:
                newRoom = miscRoom(doorDiffs[2])
            elif choice == 4:
                newRoom = miscRoom(doorDiffs[3])
            else:
                print "That is not a valid choice."
                choice = None
        return newRoom

    def enter(self, player):
        """
        Desc: takes actions when a player enters a room.
        Called by: main game loop in game

        Notes:
        i would like to move combat into this, but it needs to interrupt the regular game loop, so it is currently implemented there.
        """
        print ""
        print self.desc
        monster = mobs.pickMob(self.difficulty)
        if type(monster) != type(None):
            self.monCount += 1
            print monster.desc
            print ""
            return monster
        else:
            print "You appear to be alone here."
            return None


class miscRoom(map):
    def rollDesc(self):
        """
        Desc: randomly assigned descriptions to rooms.
        Called by: room.map.miscRoom.__init__()

        Notes:
        in the future, I plan to move these out to a flat file which will be read from.
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
        self.doorDiffs[0] = 1
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
    print "Door 1 diff: {}".format(room1.doorDiffs[0])
    print "Door 2 diff: {}".format(room1.doorDiffs[1])
    print "Door 3 diff: {}".format(room1.doorDiffs[2])
    print "Door 4 diff: {}".format(room1.doorDiffs[3])


if __name__ == "__main__":
    main()
