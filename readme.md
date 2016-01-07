Basic game written to practice python.

Player will have a character that moves through rooms and randomly encounters monsters to fight. Possibility of finding equipment in rooms or from dead monsters.

+------------------------------------------------------------------------------------------------------------------------+
+!!!                                                     Classes                                                      !!!+
+------------------------------------------------------------------------------------------------------------------------+
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
+ Imports random
+ Imported by game

- Stats:
    -strg (strength): Determines how much damage player does with attacks.
    -agi (agility): Determines chance to hit, chance to dodge, how often you attack(?). 
    -end (endurance): Determines base hit points and bonus armor. 
    -lck (luck): Influences dodge, loot and chance (future).
    -int (intelligence): Influences exp gain (future).
    -hp (hit points): Determines how much damage player can take. Based on endurance.
    -arm (armor): Decreases incoming damage. Mostly based on items, with a bonus from agility.
    -level (future).
    -exp (experience): Allows player to level up. Gained by killing mobs.  (future).
    -name.
    -ap (action points): Used in combat to control turns. Influenced by agility. 

- Equipment
- Inventory
- Skills (future)
- Race (future)
- Class (future)



+------------------------------------------------------------+
+                            Mob                             +
+------------------------------------------------------------+
+ Imported by room

- Stats
    - Same as player stats, with some additions.
    - mgt (might): !!!may remove this. Not currently used!!! 0 through 99. General rating of the monster's difficulty. Will be used to modify a base monster type's stats. For example, a base type of monster will be a goblin. A goblin with might 0 will be a Weak Goblin, and will have all stats slightly decreased. A goblin with might 10 might be a Champion Goblin, and have severely increased stats.
        - Might of 0 through 19 will be considered easy monster, 20 through 39 as medium, 40 through 59 as hard, 60 through 79 as very hard, and 80 through 99 as god-like. 
    - bdiff (base difficulty): used for mob selection when spawning. A general rating of the base monster type's difficulty. 
- Title: Added to name, based on Might.  
- Desc (description): Short description of mob. Displayed when player enters a room with the mob. 
- Skills


! Notes:
    - Mobs are currently generated only based on the difficulty result. Room Difficulty influences the roll table for mobs.PickMob. Within the roll table, there is a spawn roll and a might roll. For any given difficulty, there is a value above which a spawn roll must be to spawn a mob. Once that spawn roll check is passed, the might roll determines the actual difficulty of the mob to be spawned. The might roll will land within a difficulty bucket, and a monster of that difficulty will be spawned using mobs.spawnMob.
    - Mobs will be generated based on the might value rolled (currently in mobs.pickMob). There will be basic types of mobs (goblin, dragon, skeleton etc.), and titles that act as modifiers for those types (weak, sly, vicious, champion etc) which will provide various stat modifications. Types will be based on a certain base value, for instance goblins will have a base might of 5. The range for a type, based on titles, will be something like plus or minus 25, meaning a roll of anywhere between 0 and 30 can get you a goblin. A roll of 0 would get you a weak goblin: weak (-5 from base) and goblin (base might of 5). There will be overlaps between types, so a roll of 60 may be you a strong skeleton or a weak dragon. 
    - Mobs will be generated when a room is entered.

+------------------------------------------------------------+
+                           Room                             +
+------------------------------------------------------------+
+ Imports mechanics, mob, random
+ Imported by game

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
- monCount (Monster Count): Current number of monsters in the room.

+------------------------------------------------------------+
+                          Items                             +
+------------------------------------------------------------+
(not implemented)
- Stats
- Location worn
- Use

+------------------------------------------------------------+
+                          Skills                            +
+------------------------------------------------------------+
(not implemented)
- Effect?

+------------------------------------------------------------+
+                          Combat                            +
+------------------------------------------------------------+
+ Imports random, time
+ Imported by game 

- Turns
- Damage mechanism
- Item generation? (maybe on monster) (ni)

+------------------------------------------------------------+
+                          Mechanics                         +
+------------------------------------------------------------+
+ Imported by room

+ Base level class
+ Houses game mechanics used by other classes


- Rolls

+------------------------------------------------------------+
+                           Game                             +
+------------------------------------------------------------+
+ Imports room, player, combat

+ Class that ties all others together and runs the game


! Notes:
    - Basic flow of the game:
        - Create character
        - Spawn in beginning room
        - Generate difficulty for first room
        - Upon entry in a room:
            - Roll for chance event
            - Roll next rooms
            - Roll to check for a monster
            - Roll monster might
            - Spawn monster based on might and spawn roll
                - Determine type of monster
                - Determine title of monster
            - Fight monster until either the monster of player's HP reaches < 1
                - Combat will occur based on actions
                - Monsters and player gain actions based on their agility
                - During combat, there will be ticks. Each tick, the player's and monster's agility is added to their action points. When action points reach 100, they get a turn. If both reach 100 at the same time, whoever has the higher agility acts first.
                - When the player has a turn, they can choose to attack, flee, use a skill or use an item.
                - At monster death, there will be a chance to spawn loot (items).
            - Chance event, if any, takes place
            - Player selects next room