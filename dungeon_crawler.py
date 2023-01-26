import random

# Create a list of rooms
rooms = ["Treasure Room", "Monster Room", "Puzzle Room", "Empty Room"]

# Create a list of monsters
monsters = ["Skeleton", "Zombie", "Dragon", "Giant Spider"]

# Create a list of puzzles
puzzles = ["Maze", "Riddle", "Sudoku", "Word Scramble"]

# Create a list of treasures
treasures = ["Gold", "Jewels", "Magic Sword", "Enchanted Shield"]

# Set the number of rooms in the dungeon
num_rooms = 10

print("Welcome to the Dungeon Crawler Game!")

# Create the dungeon
dungeon = []
for i in range(num_rooms):
    room_type = random.choice(rooms)
    if room_type == "Treasure Room":
        dungeon.append({"type": room_type, "treasure": random.choice(treasures)})
    elif room_type == "Monster Room":
        dungeon.append({"type": room_type, "monster": random.choice(monsters)})
    elif room_type == "Puzzle Room":
        dungeon.append({"type": room_type, "puzzle": random.choice(puzzles)})
    else:
        dungeon.append({"type": room_type})

# Start the game
current_room = 0
while current_room < num_rooms:
    print(f"You are in a {dungeon[current_room]['type']}.")
    if dungeon[current_room]['type'] == "Treasure Room":
        print(f"You found a {dungeon[current_room]['treasure']}!")
    elif dungeon[current_room]['type'] == "Monster Room":
        print(f"A {dungeon[current_room]['monster']} attacks you!")
    elif dungeon[current_room]['type'] == "Puzzle Room":
        print(f"You must solve a {dungeon[current_room]['puzzle']} to continue.")
    choice = input("Do you want to move to the next room? (y/n)")
    if choice == "y":
        current_room += 1
    else:
        print("Thanks for playing!")
        break

print("Congratulations! You have successfully completed the dungeon.")
