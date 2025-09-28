from langchain_tavily import TavilySearch

def web_search(query: str):
    """
    """

    search_object = TavilySearch(max_results=3)

    try:
        get_data = search_object.invoke(query)
    except Exception as e:
        raise RuntimeError(f"TAVILY ERROR: {e}")

    search_results = get_data["results"][0]["content"]

    return search_results