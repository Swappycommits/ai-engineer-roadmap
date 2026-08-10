# Text Adventure Game Engine

A small interactive fiction engine built with Python and OOP — my first project using classes.

## Features
- Room-based navigation (rooms connected via exits)
- Inventory system (pick up items from rooms)
- Simple combat system with health, attack, and defeat detection
- Command-driven game loop (go, look, take, attack, quit)

## Usage

Run the game:
python game.py

Available commands:
go <direction>   - move to a connected room (e.g. go north)
look             - see the current room's description and items
take <item>      - pick up an item from the current room (e.g. take rusty key)
attack           - attack the enemy in the game
quit             - exit the game

## What I learned
- Classes, objects, and the __init__ constructor
- self and how objects hold their own independent state
- Objects referencing other objects (rooms pointing to other rooms, dictionary values that are whole objects)
- Methods that modify an object's own state (move) vs. methods that modify a different object's state (attack)
- Building a command-parsing game loop with input(), split(), and slicing/join() for multi-word arguments
- Defensive coding for missing/invalid input (IndexError from missing arguments, out-of-range checks)