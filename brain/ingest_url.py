import requests
import trafilatura
from bs4 import BeautifulSoup
from brain.capture import capture


def ingest_url(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=15)
    except Exception as e:
        print("Failed to fetch:", e)
        return

    html = r.text

    # ===== 第一層：trafilatura =====
    text = trafilatura.extract(html)

    # ===== 第二層 fallback =====
    if not text:
        soup = BeautifulSoup(html, "html.parser")

        article = soup.find("article")

        if article:
            text = article.get_text(separator="\n")
        else:
            paragraphs = soup.find_all("p")
            text = "\n".join(p.get_text() for p in paragraphs)

    text = (text or "").strip()

    if not text:
        print("⚠️ Unable to extract article text")
        return

    print("\nPreview:\n")
    print(text[:400])
    print("\n---\n")

    capture(f"""
    URL: {url}

    {text}
    """)

    print("Captured:", url)