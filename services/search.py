from duckduckgo_search import DDGS
from typing import List

async def search_web(query: str, max_results: int = 5) -> List[str]:
    """
    Search the web for a given query and return a list of URLs.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, region='wt-wt', safesearch='Moderate', max_results=max_results):
            if r.get('href'):
                results.append(r['href'])
    return results
