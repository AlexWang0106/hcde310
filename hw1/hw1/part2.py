# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles

for i, title in enumerate(titles, start=1):
    print(f"{i}. {title}")

print(f"Titles: {len(titles)}")

titles_with_a = sum(1 for title in titles if "a" in title.lower())
print(f'Titles with an "a": {titles_with_a}')

longest_title = max(titles, key=len)
print(f"Longest: {longest_title}")
