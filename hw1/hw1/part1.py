# HW1 Part 1: Strings
# Run it:  python3 part1.py
# Your output must match expected/part1.txt exactly.

from artworks import titles, years, artists
print(f"{titles[0]} ({years[0]}) by {artists[0]}")
print(titles[0].upper(), len(titles[0]))
print("Bedroom" in titles[0])