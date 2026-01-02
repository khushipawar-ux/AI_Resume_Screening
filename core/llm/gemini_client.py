"""
Google Gemini Client Module
"""
from typing import Optional
import google.generativeai as genai

class GeminiClient:
    """Client for Google Gemini API"""
    
    def __init__(self, api_key: str, model: str = "gemini-pro"):
        self.api_key = api_key
        self.model_name = model
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
    
    def generate(self, prompt: str, max_tokens: int = 500) -> Optional[str]:
        """
        Generate text using Gemini
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text
        """
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens,
                )
            )
            return response.text
        except Exception as e:
            print(f"Error generating content: {e}")
            return None
