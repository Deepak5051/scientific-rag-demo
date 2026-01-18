from langchain_commnuity.document_loaders import PypDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_commnuity.vectorstores import FAISS
from langchain_commnuity.embeddings import HuggingFaceEmbeddings

DATA_PATH ="data/papers"
INDEX_PATH ="index/faiss_index"

def ingest():
    loader = PypDFDirectoryLoader(DATA_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks =splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(INDEX_PATH)

    print("ingestion completed. FAISS index created.")

if __name__ == "__main__":
    ingest()
