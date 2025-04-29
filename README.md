
# Autonomous Research Bot

The **Autonomous Research Bot** is a FastAPI-based application designed to assist users in conducting research by searching the web, scraping articles, and summarizing content using OpenAI's GPT API.

## Features

- **Start Research**: Initiates a research session by searching for articles, scraping their content, and summarizing them.
- **Continue Research**: Allows users to continue an existing research session by fetching and summarizing additional articles.
- **Web Search**: Uses DuckDuckGo to search for relevant articles.
- **Article Scraping**: Extracts article content and metadata using `newspaper3k`.
- **Text Summarization**: Summarizes article content using OpenAI's GPT API.
- **Session Management**: Saves and loads research sessions using SQLite.

## Requirements

- Python 3.10 or higher
- An OpenAI API key for text summarization

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/autonomous_research_bot.git
   cd autonomous_research_bot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `.env` file:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

3. Use the `/start-research/` endpoint to start a new research session:
   - Provide `user_id`, `research_goal`, and optionally `max_articles`.

4. Use the `/continue-research/` endpoint to continue an existing session:
   - Provide `session_id` and optionally `max_articles`.

## Project Structure

```
autonomous_research_bot/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── models.py        # Pydantic models for data validation
│   ├── db.py            # Database operations using SQLModel
│   └── services/
│       ├── search.py    # Web search functionality
│       ├── scraper.py   # Article scraping functionality
│       └── summarizer.py# Text summarization functionality
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (API keys)
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

## Dependencies

- **FastAPI**: Web framework for building APIs.
- **Uvicorn**: ASGI server for running the FastAPI app.
- **Pydantic**: Data validation and settings management.
- **DuckDuckGo-Search**: For web search functionality.
- **Newspaper3k**: For scraping article content.
- **Httpx**: For making asynchronous HTTP requests.
- **Python-Dotenv**: For managing environment variables.
- **Lxml**: For HTML parsing.
- **SQLModel**: For database operations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)
- [Newspaper3k](https://newspaper.readthedocs.io/)
- [OpenAI GPT API](https://platform.openai.com/docs/)
