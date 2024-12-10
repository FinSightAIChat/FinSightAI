import streamlit as st
from langchain_chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain import hub

import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = ''

os.environ['OPENAI_API_KEY'] = ''

# Initialize components
def load_retriever():
    # Specify the directory where the vector store is persisted
    embedding = OpenAIEmbeddings()

    # Load the vector store
    vector_store = Chroma(persist_directory="my_vector_store", embedding_function=embedding)

    # Convert the vector store to a retriever
    retriever = vector_store.as_retriever()
    return retriever

# Function to format documents into a readable string
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Build the RAG chain
def build_rag_chain(retriever):

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    prompt = hub.pull("rlm/rag-prompt")

    # Continue as before
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt  # directly pass prompt without using load_prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

# Main Streamlit app
def main():
    st.set_page_config(page_title="RAG Chatbot", layout="centered")

    # Load retriever and RAG chain
    retriever = load_retriever()
    rag_chain = build_rag_chain(retriever)

    st.title("SEC filing Chatbot")
    #st.write('Authors: Wuyang Gao, Joe Retuerto')
    st.write('Last Updated: Nov 25, 2024')
    st.write("Ask me any question about Apple, Amazon, Nvidia, Meta, Google, Tesla, Microsoft, and I’ll provide a contextual response using SEC filings and the latest company news!")

    # Input area
    user_question = st.text_input("Your Question:", placeholder="What are Apple's risks?")

    # Generate response
    if st.button("Submit") and user_question.strip():
        with st.spinner("Retrieving and generating response..."):
            try:
                # Ensure the question is passed correctly to the chain
                response = rag_chain.invoke(user_question)  # Make sure the input format is correct
                st.markdown("### Response")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Footer
    st.write("---")
    st.caption("Powered by RAG and LangChain")

# Run the app
if __name__ == "__main__":
    main()
