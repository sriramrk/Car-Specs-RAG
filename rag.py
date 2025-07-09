# rag.py – Retrieval-Augmented Generation for Car Specs

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings

# Load environment variables
load_dotenv()

# ---- Load Vector Store ----
db_dir = "./car_vector_store"
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    persist_directory=db_dir,
    embedding_function=embedding_model
)

retriever = vector_store.as_retriever(search_kwargs={"k": 7})

# ---- Initialize LLM ----
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

# ---- Prompt Template ----
prompt_template = PromptTemplate.from_template(
    """
    You are an expert automotive assistant with deep technical knowledge of car specifications.
    Given a specific user question and a set of detailed car data context, respond with highly relevant,
    technical, and concise answers that cite specific car models, years, and attributes.

    Your goal is to provide:
    - accurate specifications (e.g., horsepower, torque, top speed, acceleration, etc.)
    - comparisons between models/years if asked
    - complete specification listings when requested
    - clear "not found" if data is not in context

    Think step-by-step when relevant and include values or ranges with units (e.g., mph, lb-ft).

    CONTEXT:
    --------
    {context}

    USER QUESTION:
    --------------
    {question}

    ANSWER:
    -------
    """
)

# ---- Create RetrievalQA Chain ----
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt_template},
    return_source_documents=True
)
