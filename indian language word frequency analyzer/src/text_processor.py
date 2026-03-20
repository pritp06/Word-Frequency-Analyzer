# -*- coding: utf-8 -*-
"""Text processing module"""
import unicodedata
import re
from src.tokenizer import Tokenizer
from src.stopword_handler import StopwordHandler

class TextProcessor:
    """Handles text preprocessing"""
    
    def __init__(self, language='hindi'):
        self.language = language.lower()
        self.tokenizer = Tokenizer(language)
        self.stopword_handler = StopwordHandler(language)
    
    def normalize_text(self, text):
        """Normalize Unicode text"""
        if not isinstance(text, str):
            text = str(text)
        text = unicodedata.normalize('NFC', text)
        text = text.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def clean_text(self, text):
        """Clean text"""
        text = re.sub(r'http[s]?://\S+', '', text)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'#(\w+)', r'\1', text)
        return text
    
    def tokenize(self, text):
        """Tokenize text"""
        return self.tokenizer.tokenize(text)
    
    def remove_stopwords(self, tokens):
        """Remove stopwords"""
        return self.stopword_handler.remove_stopwords(tokens)