# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks
counts = {}
for artwork in artworks:
    artist = artwork.get("artist", "Unknown")
    counts[artist] = counts.get(artist, 0) + 1
print(counts)  
most_artist = ""
most_count = 0
for artist, count in counts.items():
    if count > most_count:
        most_artist = artist
        most_count = count
print(f"Most works: {most_artist} ({most_count})")