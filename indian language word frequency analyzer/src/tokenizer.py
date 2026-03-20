# -*- coding: utf-8 -*-
"""Tokenizer module"""
import re

class Tokenizer:
    """Language-aware tokenizer"""
    
    def __init__(self, language='hindi'):
        self.language = language.lower()
    
    def tokenize(self, text):
        """Tokenize text into words"""
        if not text:
            return []
        tokens = re.findall(r'\S+', text)
        processed = []
        for token in tokens:
            cleaned = re.sub(r'^[^\u0900-\u097F\u0B80-\u0BFF\u0C00-\u0C7F\u0A80-\u0AFF\w]+', '', token)
            cleaned = re.sub(r'[^\u0900-\u097F\u0B80-\u0BFF\u0C00-\u0C7F\u0A80-\u0AFF\w]+$', '', cleaned)
            if cleaned:
                processed.append(cleaned)
        return processed
    
    def sentence_tokenize(self, text):
        """Tokenize sentences"""
        sentences = re.split(r'[।!?\.]+', text)
        return [s.strip() for s in sentences if s.strip()]