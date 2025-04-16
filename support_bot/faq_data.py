from typing import List, Dict
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

load_dotenv()

# Sample FAQ data
SAMPLE_FAQS = [
    {
        "question": "How do I reset my password?",
        "answer": "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions sent to your email."
    },
    {
        "question": "What are your business hours?",
        "answer": "Our support team is available Monday to Friday, 9 AM to 5 PM EST."
    },
    {
        "question": "How can I contact customer support?",
        "answer": "You can reach our customer support team by email at support@example.com or by phone at 1-800-123-4567."
    }
]

def initialize_vector_store() -> Chroma:
    """Initialize and return the Chroma vector store with FAQ data."""
    embeddings = OpenAIEmbeddings()
    
    # Convert FAQ data to Document objects
    documents = [
        Document(
            page_content=f"Q: {faq['question']}\nA: {faq['answer']}",
            metadata={"source": "faq"}
        )
        for faq in SAMPLE_FAQS
    ]
    
    # Create or load the vector store
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=os.getenv("CHROMA_DB_PATH")
    )
    
    return vector_store

def get_faq_vector_store() -> Chroma:
    """Get the FAQ vector store, initializing it if it doesn't exist."""
    embeddings = OpenAIEmbeddings()
    return Chroma(
        persist_directory=os.getenv("CHROMA_DB_PATH"),
        embedding_function=embeddings
    )

# faq_data.py
faq_chunks = [
    {
        "question": "Do I need planning permission?",
        "answer": "No, planning permission is not usually required as our studios fall under permitted development."
    },
    {
        "question": "How long does installation take?",
        "answer": "Most studios are installed within 1–2 days depending on size and complexity."
    },
    {
        "question": "What foundations are needed?",
        "answer": "Booths Studios require a flat and solid base such as concrete or paving slabs."
    },
    # Add more real chunks here from the website
] 