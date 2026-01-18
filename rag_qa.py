from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embendding-001")

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserializetion=True

)

llm =ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.2)

qa= RetrievalQA.from_chain_type(
    llm=llm,
    retrieval=db.as_retrieval(search_kwargs={"k: 3"}),
    return_source_documents=True

)

def ask_question(query):
    result = qa(query)
    return result
    