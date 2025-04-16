from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.chains import RetrievalQA

from faq_data import faq_chunks

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Embed and store FAQ data
embedding_model = OpenAIEmbeddings()

docs = [Document(page_content=f"{item['question']} {item['answer']}") for item in faq_chunks]

vector_db = Chroma.from_documents(docs, embedding=embedding_model, persist_directory="./db")
vector_db.persist()

# Setup QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4", temperature=0),
    retriever=vector_db.as_retriever()
)

# Request schema
class Question(BaseModel):
    query: str

# Route to ask questions
@app.post("/ask")
async def ask_question(q: Question):
    try:
        response = qa_chain.run(q.query)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 