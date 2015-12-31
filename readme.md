Basic game written to practice python.

Player will have a character that moves through rooms and randomly encounters monsters to fight. Possibility of finding equipment in rooms or from dead monsters.

+------------------------------------------------------------+
+!!!                       Classes                        !!!+
+------------------------------------------------------------+
+ Player - the character and their information.
+ Actions -  actions the player can take.
+ Mob - enemies to fight, possibly allies or nuetral characters in the future.
+ Room - create and manage rooms.
+ Game - mechanisms to bring the game together.
+ Items - Equipment for character, healing items, etc.
+ Skills? - special skills for player.
+ Combat? - Mechanics for battle between player and mobs. Probably end up as part of Mechanics.
+ Mechanics - Misc game mechanics inherited by other classes. Base class.
+ Game - Ties all other classes together. Runs the game. 

+------------------------------------------------------------+
+                          Player                            +
+------------------------------------------------------------+
+Inherits random
+Inherited by game

- Stats:
    -strg (strength): Determines how much damage player does with attacks.
    -agi (agility): Determines chance to hit, chance to dodge, how often you attack(?) and bonus armor. 
    -end (endurance): Determines base hit points.
    -lck (luck): Influences dodge, loot and chance (future)
    -int (intelligence): Influences exp gain (future)
    -hp (hit points): Determines how much damage player can take. Based on endurance
    -arm (armor): Decreases incoming damage. Mostly based on items, with a bonus from agility.
    -level (future)
    -exp (experience): Allows player to level up. Gained by killing mobs.  (future)
    -name

- Equipment
- Inventory
- Skills (future)
- Race (future)
- Class (future)



+------------------------------------------------------------+
+                            Mob                             +
+------------------------------------------------------------+
+Inherited by room

- Stats
    - Same as player stats, with some additions.
    - mgt (might): 0 through 99. General rating of the monster's difficulty. Will be used to modify a base monster type's stats. For example, a base type of monster will be a goblin. A goblin with might 0 will be a Weak Goblin, and will have all stats slightly decreased. A goblin with might 10 might be a Champion Goblin, and have severely increased stats.
        - Might of 0 through 19 will be considered easy monster, 20 through 39 as medium, 40 through 59 as hard, 60 through 79 as very hard, and 80 through 99 as god-like. 
 - Title: Added to name, based on Might.  
- Skills

+------------------------------------------------------------+
+                           Room                             +
+------------------------------------------------------------+
+ Inherits mechanics, mob, random
+ Inherited by game

- Generate monster.
    - Based on difficulty of room. Chances:
        - An easy room: 50% chance to spawn an enemy. If there is an enemy, its might will be:
            - 67% chance to spawn easy enemy
            - 32% medium
            - 1% hard
            - 0% very hard
            - 0% god-like
        - medium: 50% chance to spawn. Might chances:
            - 20% chance to spawn easy enemy
            - 66% medium
            - 13% hard
            - 1% very hard
            - 0% god-like
        - hard 80%
            - 0% chance to spawn easy enemy
            - 16% medium
            - 71% hard
            - 13% very hard
            - 0% god-like
        - very hard 100%
            - 0% chance to spawn easy enemy
            - 0% medium
            - 40% hard
            - 55% very hard
            - 5% god-like
- Items.
- Directions to other rooms,
- Room will be linear. A character can choose in which direction they progress. Any direction(forward, left, right, up, down) can have a given difficulty, with some indicator. Once a direction is chosen, the room will generate and the character will start a new encounter.
- Difficulty: Value 0 through 99. To begin with, these with break down into easy (0 - 24), medium (25 - 74), hard (75 - 89), and very hard (90 - 99).
- Chance: Value 0 through 99. Change that a special event will occur in a room. Things such as free healing, automatic damage etc.
- Description: At first, description will randomly pull from a list of prewritten strings. May change this in the future.

+------------------------------------------------------------+
+                          Items                             +
+------------------------------------------------------------+
- Stats
- Location worn
- Use

+------------------------------------------------------------+
+                          Skills                            +
+------------------------------------------------------------+
- Effect?

+------------------------------------------------------------+
+                          Combat                            +
+------------------------------------------------------------+
- Turns
- Damage mechanism
- Item generation? (maybe on monster)

+------------------------------------------------------------+
+                          Mechanics                         +
+------------------------------------------------------------+
+ Base level class
+ Houses game mechanics used by other classes
+ Inherited by room

- Rolls

+------------------------------------------------------------+
+                           Game                             +
+------------------------------------------------------------+
+ Class that ties all others together and runs the game
+ Inherits room, player