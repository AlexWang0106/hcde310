# HW4 Plan

## 1. Screen Sketches

### Search Page
![Search Page](search-sketch.png)

### Results Page
![Results Page](results-sketch.png)

## 2. Data Fields
FIELDS = "id,title,artist_title,artist_display,date_display,medium_display,image_id"

## 3. Specifications and Checks

### 1. Home Route (/)

Input:
The user opens the homepage.

Output:
A search page with a keyword input field and a search button.

Checks:
1. Opening the homepage displays the search box and button.
2. The user can enter a search keyword.
3. The search box and button can be accessed using the Tab key.

### 2. Results Route (/results)

Input:
A search keyword submitted by the user.

Output:
A page displaying matching artworks with images, titles, artists, and dates, or a helpful error message.

Checks:
1. Searching "monet" displays matching artworks.
2. Submitting an empty search shows a message asking the user to enter a keyword.
3. Searching for something with no results shows a helpful message instead of an empty page.

### 3. API Function (search_art)

Input:
A keyword entered by the user.

Output:
A list of artwork dictionaries from the Art Institute of Chicago API, or an error indicator if the request fails.

Checks:
1. A valid keyword returns artwork data.
2. An API error is handled without crashing the application.
3. Missing fields, such as artist names or image IDs, do not cause the application to crash.
