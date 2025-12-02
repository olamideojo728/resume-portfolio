import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    # Get raw HTML from the page
    html = requests.get(url).text
    
    # Parse HTML into a structured object
    soup = BeautifulSoup(html, "html.parser")
    
    # Extract all <h2> headings
    titles = [h.get_text() for h in soup.find_all("h2")]
    return titles

if __name__ == "__main__":
    site = "https://olamidefiction.com"
    print("Scraping titles from:", site)
    for t in scrape_titles(site):
        print("-", t)
