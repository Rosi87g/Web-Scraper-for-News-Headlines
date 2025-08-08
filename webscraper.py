import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Configuration
URL = "https://www.hindustantimes.com"  
OUTPUT_FILE = "headlines.txt"
HEADLINE_TAGS = ["h1", "h2", "title"]

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_headlines(html, tags):
    soup = BeautifulSoup(html, "html.parser")
    headlines = set()

    for tag in tags:
        for element in soup.find_all(tag):
            text = element.get_text(strip=True)
            if len(text) > 10:
                headlines.add(text)

    return sorted(headlines)

def save_to_file(headlines, filename, source_url):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Automated Data Collection from Public News Website\n")
        f.write(f"Source: {source_url}\n")
        f.write(f"Scraped on: {datetime.now()}\n")
        f.write(f"Total Headlines Collected: {len(headlines)}\n")
        f.write("-" * 50 + "\n")
        for i, headline in enumerate(headlines, 1):
            f.write(f"{i}. {headline}\n")


def main():
    html = fetch_html(URL)
    headlines = extract_headlines(html, HEADLINE_TAGS)
    save_to_file(headlines, OUTPUT_FILE, URL)
    print("\nAutomated Data Collection from Public News Website")
    print(f"Source: {URL}")
    print(f"Scraped on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Headlines Collected: {len(headlines)}")
    print("-" * 50)
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")



if __name__ == "__main__":
    main()
