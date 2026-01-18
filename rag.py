import json
from pathlib import Path

DATA_PATH = Path("../data/papers.json")

def search(query: str):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        papers = json.load(f)

    results = []
    for paper in papers:
        text = (paper["title"] + " " + paper["abstract"]).lower()
        if query.lower() in text:
            results.append(paper)

    return results