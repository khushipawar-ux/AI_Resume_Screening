"""
LLM Utilities Module
"""
from typing import Optional
from .gemini_client import GeminiClient
from .ollama_client import OllamaClient

def get_llm_client(provider: str = "gemini", **kwargs):
    """
    Get LLM client based on provider
    
    Args:
        provider: LLM provider ('gemini' or 'ollama')
        **kwargs: Additional arguments for client initialization
        
    Returns:
        LLM client instance
    """
    if provider == "gemini":
        return GeminiClient(**kwargs)
    elif provider == "ollama":
        return OllamaClient(**kwargs)
    else:
        raise ValueError(f"Unknown provider: {provider}")
