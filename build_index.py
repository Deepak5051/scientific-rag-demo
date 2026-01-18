import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

with open("data/papers.json","r",encoding="utf-8") as f:
    papers = json.load(f)

    texts =[]
    metadata =[]

    for paper in papers:
        texts.append(paper["summary"])
        metadata.app({
            "title": paper["title"],
            "url": paper["url"]
        })


    spliter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = spliter.create_documents(texts, metadata)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    db = FAISS.from_documents(docs, embeddings)
    db.save_local("faiss_index")

    print("FAISS index created")