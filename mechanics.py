#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'


import random

def roll100(bonus = 0):
    "Desc: roll values between 1 and 100"
    try:
        int(bonus)
        return random.randint(1,100) + bonus
    except TypeError:
        return None

def roll20(bonus = 0):
    try:
        int(bonus)
        return random.randint(1,20) + bonus
    except TypeError:
        return None



def main():
    print roll100()
    print roll20()
    print roll100(10)
    print roll20(5)
    print roll100('string')


if __name__ == "__main__":
    main()