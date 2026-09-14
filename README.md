# AI Chatbot

A Flask-based AI chatbot application with support for multiple AI models.

## Features

- 🤖 Simple rule-based chatbot (demo)
- 🧠 OpenAI API integration support
- 💬 Conversation history management
- 🔄 Stateless API design
- 🛡️ CORS enabled for cross-origin requests
- 📝 Easy to extend with custom models

## Project Structure

```
ai-chatbot/
├── app.py                 # Main Flask application
├── chatbot.py             # Chatbot core logic
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/gitty1235/ai-chatbot.git
cd ai-chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the template:
```bash
cp .env.example .env
```

5. Configure your environment variables in `.env`

### Running the Application

```bash
python app.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### Health Check
```
GET /health
```
Returns the health status of the chatbot.

**Response:**
```json
{
  "status": "healthy",
  "message": "AI Chatbot is running"
}
```

### Chat Endpoint
```
POST /chat
```
Send a message to the chatbot and receive a response.

**Request:**
```json
{
  "message": "Hello, how are you?"
}
```

**Response:**
```json
{
  "user_message": "Hello, how are you?",
  "bot_response": "Hello! I'm an AI chatbot. How can I help you today?",
  "status": "success"
}
```

### Reset Conversation
```
POST /reset
```
Clear the conversation history.

**Response:**
```json
{
  "message": "Conversation history cleared",
  "status": "success"
}
```

## Configuration

### Model Types

The chatbot supports different models via the `MODEL_TYPE` environment variable:

- **`simple`** (default): Rule-based responses for demo purposes
- **`openai`**: Uses OpenAI's GPT-3.5-turbo API for intelligent responses

### Using OpenAI

1. Get an API key from [OpenAI](https://platform.openai.com/api-keys)
2. Set in `.env`:
```
MODEL_TYPE=openai
OPENAI_API_KEY=sk-your-key-here
```
3. Restart the application

## Example Usage

### Using cURL

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the weather like?"}'
```

### Using Python

```python
import requests

response = requests.post(
    'http://localhost:5000/chat',
    json={'message': 'Hello!'}
)
print(response.json())
```

### Using JavaScript

```javascript
fetch('http://localhost:5000/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'Hello, chatbot!'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Extending the Chatbot

### Adding Custom Response Logic

Edit `chatbot.py` to add your own response rules in the `_get_simple_response()` method or create a new method for your custom model.

### Adding a New AI Model

1. Create a new method like `_get_custom_model_response()`
2. Add the model type to initialization in `__init__`
3. Update the `get_response()` method to use your new model
4. Update `.env.example` with any required configuration

## Deployment

### Docker (Optional)

Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t ai-chatbot .
docker run -p 5000:5000 --env-file .env ai-chatbot
```

## Troubleshooting

### Port Already in Use
Change the PORT in `.env` to an available port.

### OpenAI API Errors
- Verify your API key is correct in `.env`
- Check your OpenAI account has available credits
- Ensure the API key has appropriate permissions

### CORS Issues
The application has CORS enabled. If you still have issues, verify the request headers.

## License

MIT License - feel free to use this project however you like.

## Contributing

Feel free to fork and submit pull requests for any improvements!

## Support

For issues or questions, please create an issue in the repository.
