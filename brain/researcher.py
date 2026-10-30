# brain/researcher.py
import os
from tavily import TavilyClient

def fetch_live_documentation_fix(query_text):
    """Fetches real-time documentation and code migration advice via Tavily Search."""
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("[Tavily] ⚠️ TAVILY_API_KEY not found. Returning empty research context.")
        return "No external Tavily web context available."

    try:
        client = TavilyClient(api_key=api_key)
        response = client.search(
            query=f"fix migration documentation: {query_text}",
            search_depth="advanced",
            max_results=2
        )
        snippets = [f"Source ({res['url']}): {res['content']}" for res in response.get("results", [])]
        return "\n\n".join(snippets)
    except Exception as e:
        print(f"[Tavily Error]: {e}")
        return "Tavily web research failed."