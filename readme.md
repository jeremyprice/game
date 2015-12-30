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
