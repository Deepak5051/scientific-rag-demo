import arxiv
import json
import os

query ="cancer"
max_results = 100

search = arxiv.Search(
    query=query,
    max_results=max_results,
    sort_by=arxiv. SortCriterion.SubmittedDate
)

papers =[]

for result in search.results():
    papers.append({
        "title": result.title,
        "summary": result.summary,
        "published": str(result.published.date()),
        "url": result.entry_id
    })

    os.makedirs("data", exist_ok=True)
    with open("data/papers.json","w",encoding="utf-8") as f:
        json.dump(papers,f, indent=2)

        print(f"saved {len(papers)} papers")