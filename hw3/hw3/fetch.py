# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,medium_display"
def count_by_artist(artworks):
    counts = {}

    for artwork in artworks:
        artist = artwork.get("artist_title") or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1

    return counts

def save_results(artworks, filename):
    with open(filename, "w") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Untitled"
            artist = artwork.get("artist_title") or "Unknown"
            date = artwork.get("date_display") or "Unknown date"
            medium = artwork.get("medium_display") or "Unknown medium"

            file.write(f"{title} - {artist} - {date} - {medium}\n")
# Functions go here (above the code that runs)

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {"q": term, "fields": FIELDS}   # TODO: q (the search term) and fields (FIELDS)
headers = {"AIC-User-Agent": "HCDE310 student project"}
response = requests.get(url, params=params, headers=headers)


# TODO step 3: check response.status_code before you use the data
if response.status_code != 200:
    print(f"Request failed: {response.status_code} {response.reason}")
else:
    data = response.json()# Request failed: 403 Forbidden
    artworks = data["data"]
    if not artworks:
        print("No artworks found.")
    else:
        for artwork in artworks:
            title = artwork.get("title") or "Untitled"
            artist = artwork.get("artist_title") or "Unknown artist"
            date = artwork.get("date_display") or "Unknown date"
            medium = artwork.get("medium_display") or "Unknown medium"
            print(f"{title} - {artist} ({date}) [{medium}]")
    counts = count_by_artist(artworks)
    print(counts)
    save_results(artworks, "results.txt")

# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results
