#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'alex barnes'

import json

with open('./resources/weapons.json') as weaponjson:
    weaponData = json.load(weaponjson)

weaponIndex = {0:[], 1:[], 2:[], 3:[], 4:[]}

#cleanup any empty entries
for i, data in enumerate(weaponData):
    if not data['name']:
        weaponData.pop(i)


#weapons are indexed based on their rarity
for i, data in enumerate(weaponData):
    weaponIndex[data['rarity']].append(i)

#load armor
with open('./resources/armor.json') as armorjson:
    armorData = json.load(armorjson)

armorIndex = {0:[], 1:[], 2:[], 3:[], 4:[]}

#cleanup any empty entries
for i, data in enumerate(armorData):
    if not data['name']:
        armorData.pop(i)


#armor is indexed based on its rarity
for i, data in enumerate(armorData):
    armorIndex[data['rarity']].append(i)

class item(object):
    def __init__(self, name, desc, value, special, rarity, keyword):
        self.name = name
        self.desc = desc
        self.value = value
        self.special = special
        self.rarity = rarity
        self.keyword = keyword


    def __str__(self):
        return "{} - Value: {} - {}".format(self.name, self.value, self.desc)

class weapon(item):
    """
    all weapons are based off of this class. Weapon data will be loaded from an external JSON file.
    location key: 0 = body, 1 = head, 2 = hands, 3 = legs, 4 = feet
    """
    def __init__(self, name, desc, value, special, rarity, keyword, location, damage, strgReq, weight):
        self.location = location
        self.damage = damage
        self.strgReq = strgReq
        self.weight = weight
        super(weapon, self).__init__(name, desc, value, special, rarity, keyword)

    def __str__(self):
        return "{} - Damage: {} - Weight: {} - Minimum Strength: {} \n{}".format(self.name, self.damage, self.weight, self.strgReq, self.desc)


class armor(item):
    def __init__(self, name, desc, value, special, rarity, keyword, location, armVal, strgReq, weight):
        self.location = location
        self.armVal = armVal
        self.strgReq = strgReq
        self.weight = weight
        super(armor, self).__init__(name, desc, value, special, rarity, keyword)




def main():


    sword = weapon(weaponData[0]['name'], weaponData[0]['desc'], weaponData[0]['value'], weaponData[0]['special'], weaponData[0]['rarity'], weaponData[0]['keyword'], weaponData[0]['location'], weaponData[0]['damage'], weaponData[0]['strgReq'], weaponData[0]['weight'])
    print "Weapon Info: \nIndex: {} \nRaw Data Example: {} \nInstance Example: {}".format(weaponIndex, weaponData[0], sword)

    print "\nArmor Info: \nIndex: {} \nRaw Data Example: {}".format(armorIndex, armorData[1])


if __name__ == "__main__":
    main()