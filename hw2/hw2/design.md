# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
A list of dictionaries makes it easy to keep multiple artworks in order, while each dictionary stores information about one artwork. A single dictionary could make looking up artworks by ID easier, but it would be less convenient to access them by position.

## 2. Which fields are sometimes missing? What should the app show when they are?
Some artworks may have missing artist information, such as artist_title being null. The app should show something like "Unknown artist" instead of crashing. For missing titles or images, it could show "Untitled" or "Image unavailable" if those fields are missing.