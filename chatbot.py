"""
Chatbot Core Logic
Handles conversation logic and AI responses
"""

import os
from typing import List, Dict

class Chatbot:
    def __init__(self, model_type: str = 'simple'):
        """
        Initialize the chatbot
        
        Args:
            model_type: Type of model to use ('simple', 'openai', etc.)
        """
        self.model_type = model_type
        self.conversation_history: List[Dict[str, str]] = []
        self.max_history = 10
        
        # Initialize based on model type
        if model_type == 'openai':
            self._init_openai()
    
    def _init_openai(self):
        """Initialize OpenAI API if using OpenAI model"""
        try:
            import openai
            openai.api_key = os.getenv('OPENAI_API_KEY')
            self.openai = openai
        except ImportError:
            print("Warning: OpenAI library not installed. Install with: pip install openai")
    
    def get_response(self, user_message: str) -> str:
        """
        Get a response from the chatbot
        
        Args:
            user_message: The user's input message
            
        Returns:
            The bot's response
        """
        # Add to history
        self.conversation_history.append({
            'role': 'user',
            'content': user_message
        })
        
        # Keep history size manageable
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
        
        # Get response based on model type
        if self.model_type == 'openai':
            response = self._get_openai_response()
        else:
            response = self._get_simple_response(user_message)
        
        # Add bot response to history
        self.conversation_history.append({
            'role': 'assistant',
            'content': response
        })
        
        return response
    
    def _get_simple_response(self, user_message: str) -> str:
        """
        Simple rule-based response for demo purposes
        Replace with your own logic or connect to an actual AI model
        """
        message_lower = user_message.lower()
        
        # Simple rule-based responses
        greetings = ['hello', 'hi', 'hey', 'greetings']
        if any(greeting in message_lower for greeting in greetings):
            return "Hello! I'm an AI chatbot. How can I help you today?"
        
        if 'how are you' in message_lower:
            return "I'm doing great! Thanks for asking. How can I assist you?"
        
        if 'what is your name' in message_lower:
            return "I'm an AI Chatbot created to assist you. What would you like to know?"
        
        if 'bye' in message_lower or 'goodbye' in message_lower:
            return "Goodbye! It was nice chatting with you. Have a great day!"
        
        # Default response
        return f"I received your message: '{user_message}'. This is a demo chatbot. To enable AI responses, configure an AI model (like OpenAI) in the settings."
    
    def _get_openai_response(self) -> str:
        """
        Get response from OpenAI API
        """
        try:
            response = self.openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=150
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Error getting response from OpenAI: {str(e)}"
    
    def reset_history(self):
        """Reset conversation history"""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get conversation history"""
        return self.conversation_history.copy()
