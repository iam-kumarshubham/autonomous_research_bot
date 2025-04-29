from sqlmodel import SQLModel, Session, create_engine, select
from models import MCPContext
import json

# Create SQLite engine
DATABASE_URL = "sqlite:///./sessions.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def save_session(mcp_context: MCPContext):
    with Session(engine) as session:
        # Convert MCPContext to a dictionary and serialize HttpUrl fields as strings
        mcp_dict = json.loads(mcp_context.json())  # Use Pydantic's .json() method
        json_data = json.dumps(mcp_dict)

        # Create a new record
        session.add(SessionRecord(session_id=mcp_context.session_id, data=json_data))
        session.commit()

def load_session(session_id: str) -> MCPContext:
    with Session(engine) as session:
        statement = select(SessionRecord).where(SessionRecord.session_id == session_id)
        result = session.exec(statement).first()

        if result:
            mcp_dict = json.loads(result.data)
            return MCPContext(**mcp_dict)
        else:
            return None

from sqlmodel import Field

class SessionRecord(SQLModel, table=True):
    session_id: str = Field(primary_key=True)
    data: str
