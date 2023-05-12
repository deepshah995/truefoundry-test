""" Simple Module with Simple FastAPI Functions
"""
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> Dict[str, str]:
    """ Root route

    Returns:
        Dict[str, str]: Return simple hello world message
    """
    return {"message": "Hello World"}


@app.get("/how/{name}")
async def how_are_you(name: str) -> str:
    """ Route to How are you

    Returns:
        str: Return a simple "How are you?" question
    """
    return f"How are you, {name.title()}?"
    
