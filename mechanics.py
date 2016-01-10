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
    command = raw_input(player.showHP() + ">")



def main():
    pass


if __name__ == "__main__":
    main()