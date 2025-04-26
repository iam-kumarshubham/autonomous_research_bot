from newspaper import Article
from typing import Optional

async def scrape_article(url: str) -> Optional[dict]:
    """
    Scrapes and extracts title + main text from a URL.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        return {
            "title": article.title,
            "content": article.text
        }
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return None

