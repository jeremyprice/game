#!/usr/bin/env python2
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import random
from time import sleep


def pAttack(player, mob):
    print "You attack the {} for {} damage!\n".format(mob.name, player.strg)
    mob.chp -= player.strg
    player.ap -= 100


def mAttack(mob, player):
    print "The {} attacks you for {} damage!\n".format(mob.name, mob.strg)
    player.chp -= mob.strg
    mob.ap -= 100


def combat(player, mob):
    print "Prepare to face off against the {}!".format(mob.name)
    while player.chp > 0 and mob.chp > 0:
        while player.ap < 100 and mob.ap < 100:
            player.ap += player.agi
            mob.ap += mob.agi
            print "Player HP: {}/{} AP:{}/100 \nMob HP: {}/{} AP:{}/100\n".format(player.chp, player.hp, player.ap,
                                                                                  mob.chp, mob.hp, mob.ap)
            sleep(.5)
        if player.ap >= 100 and mob.ap <= 100:
            pAttack(player, mob)
        elif mob.ap >= 100 and player.ap <= 100:
            mAttack(mob, player)
        elif player.ap >= 100 and mob.ap >= 100:
            if player.agi > mob.agi:
                pAttack(player, mob)
            elif player.agi <= mob.agi:
                mAttack(mob, player)
            else:
                random.choice(pAttack(player, mob), mAttack(mob, player))
    if mob.chp <= 0:
        print "You have killed the {}!".format(mob.name)
        player.ap = 0
        print "Player HP: {}/{} AP:{}/100 \n".format(player.chp, player.hp, player.ap)
    elif player.chp <= 0:
        print "You have been defeated by the {}!".format(mob.name)


def main():
    pass


if __name__ == "__main__":
    main()
