import requests

URL = "https://api.artic.edu/api/v1/artworks/search"

FIELDS = "id,title,artist_title,date_display,medium_display,image_id"


def search_art(term):
    params = {"q": term, "fields": FIELDS}

    headers = {"AIC-User-Agent": "HCDE310 student project"}

    try:
        response = requests.get(
            URL,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print("Request failed:", response.status_code)
            return None

        data = response.json()

        return data.get("data", [])

    except (requests.RequestException, ValueError):
        return None