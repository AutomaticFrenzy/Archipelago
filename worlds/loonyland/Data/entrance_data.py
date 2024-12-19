from typing import List
from worlds.loonyland.Entrances import LL_Entrance
from worlds.loonyland.Rules import have_light_source
def set_entrances(multiworld, world, player):
    loonyland_entrance_table: List[LL_Entrance] = [
        LL_Entrance("Menu", "Halloween Hill", False, lambda state: True),
        LL_Entrance("Menu", "Bowling", False, lambda state: True),
        LL_Entrance("Menu", "Survival", False, lambda state: True),
        LL_Entrance("Menu", "Boss Bash", False, lambda state: True),
        LL_Entrance("Menu", "Loony Ball", False, lambda state: True),
        LL_Entrance("Menu", "Remix", False, lambda state: True),
        LL_Entrance("Halloween Hill", "A Cabin Trees", True, lambda state: True),
        LL_Entrance("Halloween Hill", "The Witch's Cabin Front", True, lambda state: True),
        LL_Entrance("Halloween Hill", "Bonita's Cabin", True, lambda state: True),
        LL_Entrance("Halloween Hill", "Underground Tunnel Top", True, lambda state: True),
        LL_Entrance("Halloween Hill", "The Bog Pit", True, lambda state: True),
        LL_Entrance("Slurpy Swamp Mud", "Slurpy Swamp Mud East Warp", False, lambda state: True),
        LL_Entrance("Slurpy Swamp Mud East Warp", "Swamp Gas Cavern Front", True, lambda state: True),
        LL_Entrance("Slurpy Swamp Mud", "Slurpy Swamp Mud North Warp", False, lambda state: True),
        LL_Entrance("Slurpy Swamp Mud North Warp", "Swamp Gas Cavern Back", True, lambda state: True),
        LL_Entrance("Halloween Hill", "A Tiny Cabin", True, lambda state: state.has("Skull Key", player)),
        LL_Entrance("Halloween Hill", "The Witch's Cabin Back", True, lambda state: True),
        LL_Entrance("Zombiton", "A Cabin Seer", True, lambda state: True),
        LL_Entrance("Zombiton", "Benny's Cocktails", True, lambda state: True),
        LL_Entrance("Halloween Hill", "Dusty Crypt Entrance", True, lambda state: True),
        LL_Entrance("Zombiton", "Musty Crypt Entrance", True, lambda state: True),
        LL_Entrance("Zombiton", "A Messy Cabin", True, lambda state: True),
        LL_Entrance("Halloween Hill", "Rusty Crypt Entrance", True, lambda state: True),
        LL_Entrance("Halloween Hill", "Under The Lake Entrance", True, lambda state: state.has("Orb", player, 4)),
        LL_Entrance("Halloween Hill", "Haunted Tower", True, lambda state: state.has("Ghost Potion", player)),
        LL_Entrance("Rocky Cliffs", "Abandoned Mines Entrance", True, lambda state: True),
        LL_Entrance("Rocky Cliffs", "The Shrine Of Bombulus", True, lambda state: True),
        LL_Entrance("Rocky Cliffs", "A Gloomy Cavern Entrance", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Halloween Hill", "Happy Stick Woods", True, lambda state: state.has("Happy Stick", player)),
        LL_Entrance("Zombiton", "A Cabin Larry", True, lambda state: True),
        LL_Entrance("Halloween Hill", "The Wolf Den Entrance", True, lambda state: True),
        LL_Entrance("Rocky Cliffs", "Upper Creepy Caverns Left Warp", True, lambda state: state.has("Bombs", player)),
        LL_Entrance("Rocky Cliffs", "Creepy Caverns Left", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Vampy Land", "Castle Vampy", True, lambda state: True),
        LL_Entrance("Halloween Hill", "Cabin In The Woods", True, lambda state: True),
        LL_Entrance("Halloween Hill", "A Cabin Collector", True, lambda state: True),
        LL_Entrance("Halloween Hill", "A Hidey-Hole", True, lambda state: True),
        LL_Entrance("Vampy Land", "Creepy Caverns Right", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Halloween Hill", "Swampdog Lair", True, lambda state: True),
        LL_Entrance("A Cabin Trees", "Halloween Hill", True, lambda state: True),
        LL_Entrance("The Witch's Cabin Front", "Halloween Hill", True, lambda state: True),
        LL_Entrance("The Witch's Cabin Back", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Bonita's Cabin", "Halloween Hill", True, lambda state: True),
        LL_Entrance("The Bog Pit", "Halloween Hill", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Underground Tunnel Top", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Underground Tunnel Zombie", "Benny's Cocktails", True, lambda state: True),
        LL_Entrance("Swamp Gas Cavern Front", "Slurpy Swamp Mud North Warp", True, lambda state: True),
        LL_Entrance("Swamp Gas Cavern Back", "Slurpy Swamp Mud East Warp", True, lambda state: True),
        LL_Entrance("A Tiny Cabin", "Halloween Hill", True, lambda state: True),
        LL_Entrance("A Cabin Seer", "Zombiton", True, lambda state: True),
        LL_Entrance("Benny's Cocktails", "Zombiton", True, lambda state: True),
        LL_Entrance("Benny's Cocktails", "Underground Tunnel Zombie", True, lambda state: True),
        LL_Entrance("Dusty Crypt Entrance", "Dusty Crypt", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Dusty Crypt Entrance", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Dusty Crypt", "Dusty Crypt Entrance", True, lambda state: True),
        LL_Entrance("Musty Crypt Entrance", "Musty Crypt", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Musty Crypt Entrance", "Zombiton", True, lambda state: True),
        LL_Entrance("Musty Crypt", "Musty Crypt Entrance", True, lambda state: True),
        LL_Entrance("Rusty Crypt Entrance", "Rusty Crypt", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Rusty Crypt Entrance", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Rusty Crypt", "Rusty Crypt Entrance", True, lambda state: True),
        LL_Entrance("A Messy Cabin", "Zombiton", True, lambda state: True),
        LL_Entrance("Under The Lake Entrance", "Under The Lake", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Under The Lake Entrance", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Under The Lake", "Under The Lake Entrance", True, lambda state: True),
        LL_Entrance("Under The Lake", "Under The Lake Exit", True, lambda state: True),
        LL_Entrance("Under The Lake Exit", "Deeper Under The Lake", True, lambda state: True),
        LL_Entrance("Under The Lake Exit", "Under The Lake", True, lambda state: True),
        LL_Entrance("Deeper Under The Lake", "Under The Lake Exit", True, lambda state: True),
        LL_Entrance("Deeper Under The Lake", "Frankenjulie's Laboratory", True, lambda state: True),
        LL_Entrance("Frankenjulie's Laboratory", "Deeper Under The Lake", True, lambda state: True),
        LL_Entrance("Frankenjulie's Laboratory", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Haunted Basement", "Haunted Basement", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Haunted Tower", "Haunted Tower Floor 2", True, lambda state: state.has("Ghost Potion", player)),
        LL_Entrance("Haunted Tower", "Haunted Basement Entrance", True, lambda state: state.has("Bat Key", player) and state.has("Pumpkin Key", player) and state.has("Skull Key", player)),
        LL_Entrance("Haunted Tower Floor 2", "Haunted Tower", True, lambda state: True),
        LL_Entrance("Haunted Tower Floor 2", "Haunted Tower Floor 3", True, lambda state: state.has("Ghost Potion", player)),
        LL_Entrance("Haunted Tower Floor 3", "Haunted Tower Floor 2", True, lambda state: state.has("Ghost Potion", player)),
        LL_Entrance("Haunted Tower Floor 3", "Haunted Tower Roof", True, lambda state: state.has("Ghost Potion", player)),
        LL_Entrance("Haunted Tower Roof", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Haunted Tower Roof", "Haunted Tower Floor 3", True, lambda state: True),
        LL_Entrance("Haunted Basement Entrance", "Haunted Tower", True, lambda state: state.has("Bat Key", player) and state.has("Pumpkin Key", player) and state.has("Skull Key", player)),
        LL_Entrance("Haunted Basement Entrance", "Haunted Basement", True, lambda state: True),
        LL_Entrance("Haunted Basement", "Haunted Basement Entrance", True, lambda state: True),
        LL_Entrance("Abandoned Mines Entrance", "Abandoned Mines", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Abandoned Mines Entrance", "Rocky Cliffs", True, lambda state: True),
        LL_Entrance("Abandoned Mines", "Abandoned Mines Entrance", True, lambda state: True),
        LL_Entrance("The Shrine Of Bombulus", "Rocky Cliffs", True, lambda state: True),
        LL_Entrance("A Gloomy Cavern Entrance", "A Gloomy Cavern", True, lambda state: have_light_source(state, player)),
        LL_Entrance("A Gloomy Cavern Entrance", "Rocky Cliffs", True, lambda state: True),
        LL_Entrance("A Gloomy Cavern", "A Gloomy Cavern Entrance", True, lambda state: True),
        LL_Entrance("Happy Stick Woods", "Halloween Hill", True, lambda state: True),
        LL_Entrance("The Wolf Den Entrance", "The Wolf Den", True, lambda state: state.has("Silver Sling", player) and have_light_source(state, player)),
        LL_Entrance("The Wolf Den Entrance", "Halloween Hill", True, lambda state: True),
        LL_Entrance("The Wolf Den", "The Wolf Den Entrance", True, lambda state: True),
        LL_Entrance("The Wolf Den", "Larry's Lair", True, lambda state: state.has("Silver Sling", player)),
        LL_Entrance("A Cabin Larry", "Zombiton", True, lambda state: True),
        LL_Entrance("Upper Creepy Caverns Left Warp", "Rocky Cliffs", True, lambda state: state.has("Bombs", player)),
        LL_Entrance("Upper Creepy Caverns Left Warp", "Upper Creepy Caverns", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Upper Creepy Caverns", "Upper Creepy Caverns Left Warp", True, lambda state: True),
        LL_Entrance("Upper Creepy Caverns Middle Warp", "Creepy Caverns Left", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Upper Creepy Caverns Middle Warp", "Upper Creepy Caverns", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Upper Creepy Caverns", "Upper Creepy Caverns Middle Warp", True, lambda state: True),
        LL_Entrance("Upper Creepy Caverns Right Warp", "Creepy Caverns Middle", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Upper Creepy Caverns Right Warp", "Upper Creepy Caverns", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Upper Creepy Caverns", "Upper Creepy Caverns Right Warp", True, lambda state: True),
        LL_Entrance("Under The Ravine", "Creepy Caverns Middle", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Under The Ravine", "Creepy Caverns Right", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Creepy Caverns Left", "Rocky Cliffs", True, lambda state: True),
        LL_Entrance("Creepy Caverns Left", "Upper Creepy Caverns Middle Warp", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Creepy Caverns Middle", "Upper Creepy Caverns", True, lambda state: have_light_source(state, player)),
        LL_Entrance("Creepy Caverns Middle", "Under The Ravine", True, lambda state: True),
        LL_Entrance("Creepy Caverns Right", "Under The Ravine", True, lambda state: True),
        LL_Entrance("Creepy Caverns Right", "Vampy Land", True, lambda state: True),
        LL_Entrance("Castle Vampy", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Castle Vampy", "Castle Vampy Skull Jail", False, lambda state: state.has("Skull Key", player)),
        LL_Entrance("Castle Vampy Skull Jail", "Castle Vampy II Main", True, lambda state: state.has("Skull Key", player)),
        LL_Entrance("Castle Vampy", "Castle Vampy II NE", True, lambda state: state.has("Bat Statue", player, 4)),
        LL_Entrance("Castle Vampy", "Castle Vampy II SE", True, lambda state: state.has("Bat Statue", player, 4)),
        LL_Entrance("Castle Vampy", "Castle Vampy II SW", True, lambda state: state.has("Bat Statue", player, 4)),
        LL_Entrance("Castle Vampy", "Castle Vampy II NW", True, lambda state: state.has("Bat Statue", player, 4)),
        LL_Entrance("Castle Vampy II Main", "Castle Vampy Skull Jail", True, lambda state: True),
        LL_Entrance("Castle Vampy II Main", "Castle Vampy II Bat Jail", True, lambda state: state.has("Bat Key", player)),
        LL_Entrance("Castle Vampy II Bat Jail", "Castle Vampy III Main", True, lambda state: state.has("Bat Key", player)),
        LL_Entrance("Castle Vampy II NE", "Castle Vampy", True, lambda state: True),
        LL_Entrance("Castle Vampy II NE", "Castle Vampy III NE", True, lambda state: True),
        LL_Entrance("Castle Vampy II SE", "Castle Vampy", True, lambda state: True),
        LL_Entrance("Castle Vampy II SE", "Castle Vampy III SE", True, lambda state: True),
        LL_Entrance("Castle Vampy II SW", "Castle Vampy", True, lambda state: True),
        LL_Entrance("Castle Vampy II SW", "Castle Vampy III SW", True, lambda state: True),
        LL_Entrance("Castle Vampy II NW", "Castle Vampy", True, lambda state: True),
        LL_Entrance("Castle Vampy II NW", "Castle Vampy III NW", True, lambda state: True),
        LL_Entrance("Cabin In The Woods", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Castle Vampy III Main", "Castle Vampy II Bat Jail", True, lambda state: True),
        LL_Entrance("Castle Vampy III Main", "Castle Vampy III Pumpkin Jail", True, lambda state: state.has("Pumpkin Key", player)),
        LL_Entrance("Castle Vampy III Pumpkin Jail", "Castle Vampy IV Main", True, lambda state: state.has("Pumpkin Key", player)),
        LL_Entrance("Castle Vampy III NE", "Castle Vampy II NE", True, lambda state: True),
        LL_Entrance("Castle Vampy III NE", "Castle Vampy IV NE", True, lambda state: True),
        LL_Entrance("Castle Vampy III SE", "Castle Vampy II SE", True, lambda state: True),
        LL_Entrance("Castle Vampy III SE", "Castle Vampy IV SE", True, lambda state: True),
        LL_Entrance("Castle Vampy III SW", "Castle Vampy II SW", True, lambda state: True),
        LL_Entrance("Castle Vampy III SW", "Castle Vampy IV SW", True, lambda state: True),
        LL_Entrance("Castle Vampy III NW", "Castle Vampy II NW", True, lambda state: True),
        LL_Entrance("Castle Vampy III NW", "Castle Vampy IV NW", True, lambda state: True),
        LL_Entrance("Castle Vampy IV Main", "Castle Vampy III Pumpkin Jail", True, lambda state: True),
        LL_Entrance("Castle Vampy IV Main", "The Heart Of Terror", True, lambda state: state.has("Vampire Bust", player, 8)),
        LL_Entrance("Castle Vampy IV NE", "Castle Vampy III NE", True, lambda state: True),
        LL_Entrance("Castle Vampy IV NE", "Castle Vampy Roof NE", True, lambda state: True),
        LL_Entrance("Castle Vampy IV SE", "Castle Vampy III SE", True, lambda state: True),
        LL_Entrance("Castle Vampy IV SE", "Castle Vampy Roof SE", True, lambda state: True),
        LL_Entrance("Castle Vampy IV SW", "Castle Vampy III SW", True, lambda state: True),
        LL_Entrance("Castle Vampy IV SW", "Castle Vampy Roof SW", True, lambda state: True),
        LL_Entrance("Castle Vampy IV NW", "Castle Vampy III NW", True, lambda state: True),
        LL_Entrance("Castle Vampy IV NW", "Castle Vampy Roof NW", True, lambda state: True),
        LL_Entrance("A Cabin Collector", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Castle Vampy Roof NE", "Castle Vampy IV NE", True, lambda state: True),
        LL_Entrance("Castle Vampy Roof SE", "Castle Vampy IV SE", True, lambda state: True),
        LL_Entrance("Castle Vampy Roof SW", "Castle Vampy IV SW", True, lambda state: True),
        LL_Entrance("Castle Vampy Roof NW", "Castle Vampy IV NW", True, lambda state: True),
        LL_Entrance("The Evilizer", "Halloween Hill", True, lambda state: True),
        LL_Entrance("The Heart Of Terror", "The Evilizer", True, lambda state: True),
        LL_Entrance("The Heart Of Terror", "Empty Rooftop", True, lambda state: True),
        LL_Entrance("A Hidey-Hole", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Empty Rooftop", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Swampdog Lair", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Larry's Lair", "Halloween Hill", True, lambda state: True),
        LL_Entrance("Halloween Hill", "Slurpy Swamp Mud", False, lambda state: state.has("Boots", player)),
        LL_Entrance("Slurpy Swamp Mud", "Halloween Hill", False, lambda state: state.has("Boots", player)),
        LL_Entrance("Slurpy Swamp Mud North Warp", "Slurpy Swamp Mud", False, lambda state: state.has("Boots", player)),
        LL_Entrance("Slurpy Swamp Mud East Warp", "Slurpy Swamp Mud", False, lambda state: state.has("Boots", player)),
        LL_Entrance("Zombiton", "Halloween Hill", False, lambda state: True),
        LL_Entrance("Halloween Hill", "Rocky Cliffs", False, lambda state: state.has("Big Gem", player)),
        LL_Entrance("Rocky Cliffs", "Halloween Hill", False, lambda state: state.has("Big Gem", player)),
        LL_Entrance("Vampy Land", "Halloween Hill", False, lambda state: True),
        LL_Entrance("Underground Tunnel Top", "Underground Tunnel Mud", False, lambda state: state.has("Boots", player)),
        LL_Entrance("Underground Tunnel Mud", "Underground Tunnel Top", False, lambda state: state.has("Boots", player)),
        LL_Entrance("Underground Tunnel Mud", "Underground Tunnel Zombie", False, lambda state: state.has("Boots", player)),
        LL_Entrance("Swamp Gas Cavern Front", "Swamp Gas Cavern Back", False, lambda state: state.has("Boots", player)),
]
    for region in multiworld.get_regions(player):
        for entry in loonyland_entrance_table:
            if entry.source_region == region.name:
                region.connect(connecting_region=world.get_region(entry.target_region), rule=entry.rule)