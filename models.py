from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict

class HistoryItem(BaseModel):
    role: str  # 'user' | 'bot'
    content: str

class Document(BaseModel):
    url: HttpUrl
    title: Optional[str]
    content: Optional[str]

class Summary(BaseModel):
    url: HttpUrl
    summary: str

class MCPContext(BaseModel):
    user_id: str
    session_id: str
    research_goal: str
    history: List[HistoryItem]
    visited_urls: List[HttpUrl] = []
    extracted_documents: List[Document] = []
    summaries: List[Summary] = []
