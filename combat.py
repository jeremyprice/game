#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import random
from time import sleep


def combat(player, mob):
    print "Prepare to face off against the {}!".format(mob.name)
    while player.chp > 0 and mob.chp > 0:
        while player.ap < 100 and mob.ap < 100:
            player.ap += player.agi
            mob.ap += mob.agi
            print player.showHP()
            print mob.showHP() + '\n'
            sleep(.5)
        if player.ap >= 100 and mob.ap <= 100:
            player.attack(mob)
        elif mob.ap >= 100 and player.ap <= 100:
            mob.attack(player)
        elif player.ap >= 100 and mob.ap >= 100:
            if player.agi > mob.agi:
                player.attack(mob)
            elif player.agi <= mob.agi:
                mob.attack(player)
            else:
                random.choice(player.attack(mob), mob.attack(player))
    if mob.chp <= 0:
        print "You have killed the {}!\n".format(mob.name)
        player.ap = 0
        print player.showHP()
    elif player.chp <= 0:
        print "You have been defeated by the {}!".format(mob.name)


def main():
    pass


if __name__ == "__main__":
    main()
