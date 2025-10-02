from langchain_core.tools import tool
import os

@tool
def search_files(directory: str, pattern: str) -> list[str]:
    """Searches for files in a directory matching a pattern."""
    return [f for f in os.listdir(directory) if pattern in f]