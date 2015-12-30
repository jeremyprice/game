Basic game written to practice python.

Player will have a character that moves through rooms and randomly encounters monsters to fight. Possibility of finding equipment in rooms or from dead monsters.

+ Classes:
Player - the character and their information.
Mob - enemies to fight, possibly allies or nuetral characters in the future.
Room - create and manage rooms.
Game - mechanisms to bring the game together.
Items - Equipment for character, healing items, etc.
Skills? - special skills for player.
Combat? - Mechanics for battle between player and mobs. Probably end up as part of Game.

- Player:
Stats:
    strg (strength). Determines how much damage player does with attacks
    agi (agility). Determines chance to hit and chance to dodge.
    end (endurance). Determines base hit points and armor.
    hp (hit points). Determines how much damage player can take.
    arm (armor). Decreases incoming damage. Mostly based on items
    level (future)
    exp (future)
    name

Equipment
Inventory
Skills (future)
Race (future)
Class (future)



- Monster:
Stats
Skills

- Room:
Generate monster,
Items,
Directions to other rooms,
Room will be linear. A character can choose in which direction they progress. Any direction(forward, left, right, up, down) can have a given difficulty, with some indicator. Once a direction is chosen, the room will generate and the character will start a new encounter.
Difficulty: Value 0 through 99. To begin with, these with break down into easy (0 - 24), medium (25 - 74), hard (75 - 89), and very hard (90 - 99).
Chance: Value 0 through 99. Change that a special event will occur in a room. Things such as free healing, automatic damage etc.
Description: At first, description will randomly pull from a list of prewritten strings. May change this in the future.

- Items:
Stats
Location worn
Use

- Skills:
Effect?

- Combat:
Turns
Damage mechanism
Item generation? (maybe on monster)
