import requests
from bs4 import BeautifulSoup

BASE_URL = "https://jobseden.com"

PAGES = [
    "/",
    "/about",
    "/team",
    "/careers",
]

for page in PAGES:
    url = BASE_URL + page

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True)

        print(f"\nURL: {url}")
        print(text)

    except requests.RequestException:
        print(f"Failed to load {url}")