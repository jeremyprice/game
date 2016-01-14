Basic game written to practice python.

Player will have a character that moves through rooms and randomly encounters monsters to fight. Possibility of finding equipment in rooms or from dead monsters.

####+------------------------------------------------------------+
####+                        Modules                             +
####+------------------------------------------------------------+
+ Player - the character and their information.
+ Actions -  actions the player can take. (Not implemented)
+ Mob - enemies to fight, possibly allies or neutral characters in the future.
+ Room - create and manage rooms. Spawn mobs.
+ Items - Equipment for character, healing items, etc. (Not implemented)
+ Skills? - special skills for player. (Not implemented)
+ Combat - Mechanics for battle between player and mobs.
+ Mechanics - Misc game mechanics inherited by others. Base class.
+ Game - Ties all other modules together. Runs the game. 


#####+------------------------------------------------------------+
#####+                          Player                            +
#####+------------------------------------------------------------+
+ Imports random
+ Imported by game

+Notes:
- The players in-game avatar. Houses all player stats, skills etc.
- Would like to add classes and races in the future. These will give skills and stat modifications.
- Will house equipment once implemented.

+Attributes:
- strg (Strength): Determines how much damage player does with attacks.
- agi (Agility): Determines chance to hit, chance to dodge(NI), how often you attack. 
- end (Endurance): Determines base hit points and bonus armor. 
- lck (Luck): Influences dodge, loot and chance (Not Implemented).
- int (Intelligence): Influences exp gain (Not Implemented).
- hp (Hit points): Determines how much damage player can take. Based on endurance.
- chp (Current HP): Player's current hit points. If this reaches 0, you lose.
- arm (Armor): Decreases incoming damage. Mostly based on items(NI), with a bonus from agility.
- level (Not Implemented).
- exp (Experience): Allows player to level up. Gained by killing mobs.  (Not Implemented).
- name.
- ap (Action points): Used in combat to control turns. Influenced by agility. 
- roomCt (Room count): Number of rooms the player has entered this game. Used to to give a chance to find the end. Incremented in room.map.enter

#####+------------------------------------------------------------+
#####+                            Mob                             +
#####+------------------------------------------------------------+
+ Imported by room

+Notes:
- Mobs are currently generated only based on the difficulty result. Room Difficulty influences the roll table for mobs.PickMob. Within the roll table, there is a spawn roll and a might roll. For any given difficulty, there is a value above which a spawn roll must be to spawn a mob. Once that spawn roll check is passed, the might roll determines the actual difficulty of the mob to be spawned. The might roll will land within a difficulty bucket, and a monster of that difficulty will be spawned using mobs.mobLoader.
 - Mobs will be generated based on the might value rolled (currently in mobs.pickMob). There will be basic types of mobs (goblin, dragon, skeleton etc.), and titles that act as modifiers for those types (weak, sly, vicious, champion etc) which will provide various stat modifications. Types will be based on a certain base value, for instance goblins will have a base might of 5. The range for a type, based on titles, will be something like plus or minus 25, meaning a roll of anywhere between 0 and 30 can get you a goblin. A roll of 0 would get you a weak goblin: weak (-5 from base) and goblin (base might of 5). There will be overlaps between types, so a roll of 60 may be you a strong skeleton or a weak dragon. 
 - Mobs are generated when a room is entered.
 - Mobs are loaded from an external file, ./resources/mobs.json , and new mobs can be easily added there.

+Attributes:
- strg (Strength): Determines how much damage mob does with attacks.
- agi (Agility): Determines chance to hit, chance to dodge(NI), how often mob attacks. 
- end (Endurance): Determines base hit points and bonus armor. 
- hp (Hit points): Determines how much damage mob can take. Based on endurance.
- chp (Current HP): Mob's current hit points. If this reaches 0, the mob dies.
- mgt (might): !!!may remove this. Not currently used!!! 0 through 99. General rating of the monster's difficulty. Will be used to modify a base monster type's stats. For example, a base type of monster will be a goblin. A goblin with might 0 will be a Weak Goblin, and will have all stats slightly decreased. A goblin with might 10 might be a Champion Goblin, and have severely increased stats.
- Might of 0 through 19 will be considered easy monster, 20 through 39 as medium, 40 through 59 as hard, 60 through 79 as very hard, and 80 through 99 as god-like. 
- bdiff (base difficulty): used for mob selection when spawning. A general rating of the base monster type's difficulty. 
- Title: Added to name, based on Might. Modifies stats (Not Implemented)
- Desc (description): Short description of mob. Displayed when player enters a room with the mob. 


#####+------------------------------------------------------------+
#####+                           Room                             +
#####+------------------------------------------------------------+
+ Imports mechanics, mob, random
+ Imported by game

+Notes
- Generates monster.
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
- Generate Items (Not implemented)
- Generate and present choice for next room(s).
- Rooms will be linear. A character can choose which door they will progress through. Any door will have a given difficulty, indicated by the door's description. Once a door is chosen, the room will generate and the character will start a new encounter.
- Difficulty: Value 0 through 99. To begin with, these with break down into easy (0 - 24), medium (25 - 74), hard (75 - 89), and very hard (90 - 99).
- Chance: Value 0 through 99. Chance that a special event will occur in a room. Things such as free healing, automatic damage etc.
- Description: At first, description will randomly pull from a list of prewritten strings. May change this in the future to use an external flat file.
- The chance to enter the winning room will be based on the number of rooms the player has already entered. if player.roomCt + luck(not implemented) + roll20 > 40 ?
- roomCt will also influence the difficulty of next room options, constantly increasing it.


+Attributes:
- monCount (Monster Count) (int): Current number of monsters in the room.
- difficulty (int): Difficulty of current room. Used when spawning monsters.
- desc (Description) (str): Descritpion of the current room. Printed by the enter method.
- exits (int): Number of choices for next room 
- doorDiffs (Door difficulties) (list) = Difficulties corresponding to the exits for next rooms.

#####+------------------------------------------------------------+
#####+                          Items                             +
#####+------------------------------------------------------------+
(not implemented)
- Stats
- Location worn
- Use

#####+------------------------------------------------------------+
#####+                          Skills                            +
#####+------------------------------------------------------------+
(not implemented)
- Effect?

- flee: return to last room
- stomp: reduce mob's AP
- bide: save your AP
- kick: lower damage attack, uses less AP. Maybe reduce's mob's AP slightly
- 

#####+------------------------------------------------------------+
#####+                          Combat                            +
#####+------------------------------------------------------------+
+ Imports random, time
+ Imported by game 

+Notes:
- Combat is currently very simple. When a mob is encountered, you enter combat. Every half second both the player and the mob gain their agility in action points. When either reach 100 AP, they attack. If both reach 100 at once, whoever has the higher agility attacks first. If both have the same agility, one of the two is chosen at random. This makes agility very powerful.
- Combat continues until either the mob or player die.
- I plan to implement a prompt for the player once their AP reaches 100. This prompt will allow them to choose to attack, use a skill or use an item.

#####+------------------------------------------------------------+
#####+                          Mechanics                         +
#####+------------------------------------------------------------+
+ Imported by room

+ Base level class
+ Houses game mechanics used by other classes


- Rolls

#####+------------------------------------------------------------+
#####+                           Game                             +
#####+------------------------------------------------------------+
+ Imports room, player, combat, actions

+ Ties all others together and runs the game


+Notes:
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
            - Determine title of monster(Not Implemented)
        - Fight monster until either the monster of player's HP reaches < 1
        - Chance event, if any, takes place
        - Player selects next room
        
        
###### To do:
- Add skills
- Add classes
- Add races
- Add levels
- Add monster titles
- Add items and inventory
- Add weapons
- Increase difficulty based on roomCt
- Add difficulty option
- Move misc. room descriptions to an external file
- Add modifiers to rolls ex mechanics.roll20(1) would be the roll +1
- Add first play tutorial
- Add game saves
- Add merchant (after items and inventory)