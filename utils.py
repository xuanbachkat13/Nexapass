import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def normalize_url(url):
    if not url.startswith("http"):
        return "https://" + url
    return url

def follow_redirect(url):
    r = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=10)
    return r.url

def extract_meta_refresh(html, base):
    soup = BeautifulSoup(html, "html.parser")
    meta = soup.find("meta", attrs={"http-equiv": "refresh"})
    if meta:
        content = meta.get("content", "")
        if "url=" in content.lower():
            return urljoin(base, content.split("=", 1)[1])
