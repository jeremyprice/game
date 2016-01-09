#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import random


class player(object):
    """
    this object represents the player within the game. It handles creation and storage of all player statistics.
    will change stats to dictionary in the future
    """

    strg = agi = end = hp = chp = arm = ap = roomCt = 0
    name = ""

    def rollStats(self):
        """
        Desc: generates player stats
        Called by: player.player.__init__
        """
        roll = {'strg': 0, 'agi': 0, 'end': 0}
        roll['strg'] = random.randint(1, 18)
        roll['agi'] = random.randint(1, 18)
        roll['end'] = random.randint(1, 18)
        # make sure total stars are between 15 and 45, if not reroll
        while (roll['strg'] + roll['agi'] + roll['end']) > 45 or (roll['strg'] + roll['agi'] + roll['end']) <= 25 or \
                        roll['strg'] < 5 or roll['agi'] < 8 or roll['end'] < 5:
            roll = self.rollStats()
        return roll

    def showHP(self):
        "standard format to print players current HP"
        print "Player HP: {}/{} AP:{}/100".format(self.chp, self.hp, self.ap)

    def death(self):
        "called when the player dies"
        print "{0} has died, like many before. {0} survived {1} rooms.".format(self.name, self.roomCt)
        exit()

    def win(self):
        "called when the player wins the game"
        print "\n{0} has escaped the dungeon, as few before have. {0} survived {1} rooms.\n".format(self.name, self.roomCt)
        exit()

    def __str__(self):
        return "Your stats are: \nStrength: {} \nAgility: {} \nEndurance: {} \nHit Points: {} \nArmor: {}".format(
            self.strg, self.agi, self.end, self.hp, self.arm)

    def __init__(self):
        print "Creating character.\n"

        while len(self.name) < 1:
            try:
                self.name = str(raw_input("What is your name, traveler? "))
            except:
                print "That is not a valid name."

        print "You will have three rolls to choose from."
        print "Rolling stats."

        roll1 = self.rollStats()
        roll2 = self.rollStats()
        roll3 = self.rollStats()

        # Debug stats. Special name 'AlexRocks' sets stats very high to allow for in-game testing with super stats.
        if self.name == 'AlexRocks':
            roll1 = {'strg': 100, 'agi': 100, 'end': 100}

        print "1) Str: {}, Agi: {}, End: {}".format(roll1['strg'], roll1['agi'], roll1['end'])
        print "2) Str: {}, Agi: {}, End: {}".format(roll2['strg'], roll2['agi'], roll2['end'])
        print "3) Str: {}, Agi: {}, End: {}".format(roll3['strg'], roll3['agi'], roll3['end'])

        choice = int(raw_input("Which option will you choose?: "))
        while choice not in (1, 2, 3):
            choice = int(raw_input("Please choose either 1, 2 or 3: "))

        if choice == 1:
            self.strg = roll1['strg']
            self.agi = roll1['agi']
            self.end = roll1['end']
        elif choice == 2:
            self.strg = roll2['strg']
            self.agi = roll2['agi']
            self.end = roll2['end']
        else:
            self.strg = roll3['strg']
            self.agi = roll3['agi']
            self.end = roll3['end']

        # set secondary stats based on primary
        self.hp = self.chp = 100 + (self.end * 5)
        if self.end % 2 == 0:
            self.arm = self.end / 2
        else:
            self.arm = (self.end - 1) / 2

        print ""
        print "Hail, {}.".format(self.name)
        print ""
        print self


def main():
    char = player()


if __name__ == "__main__":
    main()
