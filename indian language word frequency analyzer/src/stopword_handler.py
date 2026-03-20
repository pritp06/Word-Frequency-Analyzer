# -*- coding: utf-8 -*-
"""
Stopword handling module
"""

from config.language_config import STOPWORDS


class StopwordHandler:
    """Handles stopword removal"""
    
    def __init__(self, language='hindi'):
        """Initialize stopword handler"""
        self.language = language.lower()
        self.stopwords = self._load_stopwords()
    
    def _load_stopwords(self):
        """Load stopwords"""
        stopwords_list = STOPWORDS.get(self.language, [])
        return set(stopwords_list)
    
    def remove_stopwords(self, tokens):
        """Remove stopwords from tokens"""
        return [token for token in tokens if token.lower() not in self.stopwords]
    
    def is_stopword(self, word):
        """Check if word is stopword"""
        return word.lower() in self.stopwords
    
    def add_stopword(self, word):
        """Add custom stopword"""
        self.stopwords.add(word.lower())
    
    def remove_stopword(self, word):
        """Remove stopword"""
        self.stopwords.discard(word.lower())
    
    def get_stopwords(self):
        """Get all stopwords"""
        return self.stopwords.copy()