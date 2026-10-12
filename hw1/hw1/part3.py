# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"
for title, year in zip(titles, years):
    if year >= cutoff:
        print(title)

print() 

old_count = 0
modern_count = 0

for title, year in zip(titles, years):
    if year < cutoff:
        label = "old"
        old_count += 1
    else:
        label = "modern"
        modern_count += 1
    print(f"{title}: {label}")

print() 

print(f"Old: {old_count}")
print(f"Modern: {modern_count}")
