from fastapi import FastAPI, HTTPException
from models import MCPContext, HistoryItem, Document, Summary
from services.search import search_web
from services.scraper import scrape_article
from services.summarizer import summarize_text
from typing import Optional
import uuid

app = FastAPI()

# In-memory storage (for now)
SESSIONS = {}

@app.post("/start-research/", response_model=MCPContext)
async def start_research(user_id: str, research_goal: str, max_articles: Optional[int] = 3):
    """
    Starts a new research session by searching, scraping, and summarizing articles.
    """
    session_id = str(uuid.uuid4())
    mcp_context = MCPContext(
        user_id=user_id,
        session_id=session_id,
        research_goal=research_goal,
        history=[HistoryItem(role="user", content=research_goal)],
        visited_urls=[],
        extracted_documents=[],
        summaries=[]
    )

    try:
        urls = await search_web(research_goal, max_results=max_articles)
        for url in urls:
            if url not in mcp_context.visited_urls:
                article_data = await scrape_article(url)
                if article_data and article_data.get("content"):
                    mcp_context.visited_urls.append(url)
                    mcp_context.extracted_documents.append(Document(
                        url=url,
                        title=article_data.get("title"),
                        content=article_data.get("content")
                    ))
                    # Summarize the document
                    summary_text = await summarize_text(article_data.get("content"))
                    mcp_context.summaries.append(Summary(
                        url=url,
                        summary=summary_text
                    ))
        
        # Save session
        SESSIONS[session_id] = mcp_context
        return mcp_context

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/continue-research/", response_model=MCPContext)
async def continue_research(session_id: str, max_articles: Optional[int] = 2):
    """
    Continues an existing research session.
    """
    mcp_context = SESSIONS.get(session_id)
    if not mcp_context:
        raise HTTPException(status_code=404, detail="Session not found.")

    try:
        urls = await search_web(mcp_context.research_goal, max_results=max_articles)
        for url in urls:
            if url not in mcp_context.visited_urls:
                article_data = await scrape_article(url)
                if article_data and article_data.get("content"):
                    mcp_context.visited_urls.append(url)
                    mcp_context.extracted_documents.append(Document(
                        url=url,
                        title=article_data.get("title"),
                        content=article_data.get("content")
                    ))
                    summary_text = await summarize_text(article_data.get("content"))
                    mcp_context.summaries.append(Summary(
                        url=url,
                        summary=summary_text
                    ))
        
        return mcp_context

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
