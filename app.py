import streamlit as str
from backend.rag_qa import ask_question

st.set_page_config(page_title="Scientific Research Assistant")

st.title("  Scientific Research RAG System")
st.write("Ask questions from real cancer research papers (arxiv)")

query = st.text_input("Enter your research question:")

if st.buttion("Search"):
    if query:
        with st.spinner("Searching scientific papers..."):
            result = ask_question(query)

        
        st.subheader("  Answer")
        st.write(result["result"])

        st.subheader("  Sources")
        for doc in result["source_documnents"]:
            st.markdown(f"- **{doc.metadata['title']}**")

            else:
                st.warning("Please Enter a Question")