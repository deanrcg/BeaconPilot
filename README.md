# BeaconPilot

A smart support bot that uses AI to answer customer questions based on your FAQ data.

## Features

- Fast and accurate responses using GPT-4
- Easy integration with existing FAQ data
- Simple web interface for testing
- Vector-based search for relevant answers

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/deanrcg/BeaconPilot.git
cd BeaconPilot
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r support_bot/requirements.txt
```

3. Set up environment variables:
```bash
cp support_bot/.env.example support_bot/.env
# Edit .env with your OpenAI API key
```

4. Run the server:
```bash
cd support_bot
uvicorn main:app --reload
```

5. Open the frontend:
- Open `support_bot/frontend/index.html` in your browser
- Or access the API directly at `http://localhost:8000`

## API Endpoints

- `POST /ask`: Ask a question
  ```json
  {
    "query": "Your question here"
  }
  ```
  Response:
  ```json
  {
    "answer": "The bot's response"
  }
  ```

- `GET /health`: Health check endpoint
  ```json
  {
    "status": "healthy"
  }
  ```

## Environment Variables

See `.env.example` for required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `CHROMA_DB_PATH`: Path to store the vector database (default: ./db)

## Demo

![BeaconPilot Demo](demo.png)

## Tech Stack

- FastAPI for the backend
- LangChain for AI integration
- ChromaDB for vector storage
- GPT-4 for question answering
- Simple HTML/CSS frontend

## Contributing

Feel free to submit issues and enhancement requests! 