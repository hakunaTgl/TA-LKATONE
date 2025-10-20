"""Tokenizer module for text processing."""

from typing import List, Optional
from transformers import AutoTokenizer


class Tokenizer:
    """Tokenizer wrapper for encoding and decoding text."""
    
    def __init__(self, model_name_or_path: str):
        """
        Initialize the tokenizer.
        
        Args:
            model_name_or_path: Path to model or HuggingFace model name
        """
        self.tokenizer = None
        self.model_name_or_path = model_name_or_path
        
    def load(self):
        """Load the tokenizer from the specified path or name."""
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path)
        except Exception as e:
            print(f"Error loading tokenizer: {e}")
            raise
    
    def encode(self, text: str, add_special_tokens: bool = True) -> List[int]:
        """
        Encode text to token IDs.
        
        Args:
            text: Text to encode
            add_special_tokens: Whether to add special tokens
            
        Returns:
            List of token IDs
        """
        if self.tokenizer is None:
            raise ValueError("Tokenizer not loaded. Call load() first.")
        return self.tokenizer.encode(text, add_special_tokens=add_special_tokens)
    
    def decode(self, token_ids: List[int], skip_special_tokens: bool = True) -> str:
        """
        Decode token IDs to text.
        
        Args:
            token_ids: List of token IDs
            skip_special_tokens: Whether to skip special tokens
            
        Returns:
            Decoded text string
        """
        if self.tokenizer is None:
            raise ValueError("Tokenizer not loaded. Call load() first.")
        return self.tokenizer.decode(token_ids, skip_special_tokens=skip_special_tokens)
    
    def get_vocab_size(self) -> int:
        """
        Get the vocabulary size of the tokenizer.
        
        Returns:
            Vocabulary size
        """
        if self.tokenizer is None:
            raise ValueError("Tokenizer not loaded. Call load() first.")
        return len(self.tokenizer)
