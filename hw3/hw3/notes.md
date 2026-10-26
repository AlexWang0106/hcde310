# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths
Artist: data["data"][0]["artist_title"]
Date: data["data"][0]["date_display"]
Medium: data["data"][0]["medium_display"]

## 3. Which fields are `null` for some works?
The artist_title field is null for the third artwork. The top-level preference field is also null.

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
I think the program will ask for a search term, but then fail because the URL is empty and the parameters are not set. The request won't be sent successfully, so it will raise an error instead of showing artworks.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
After I entered "cat", the program crashed with a MissingSchema error because the URL was empty and had no https:// scheme. The error occurred on line 16 of fetch.py, where requests.get(url, params=params) was called.
