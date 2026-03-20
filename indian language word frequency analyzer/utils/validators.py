# -*- coding: utf-8 -*-
"""Input validation"""
import os

class InputValidator:
    """Validates inputs"""
    
    @staticmethod
    def validate_text(text):
        """Validate text"""
        if not text or not isinstance(text, str):
            return False
        return len(text.strip()) >= 3
    
    @staticmethod
    def validate_file_path(file_path):
        """Validate file path"""
        if not file_path or not isinstance(file_path, str):
            return False
        return os.path.isfile(file_path)
    
    @staticmethod
    def validate_language(language):
        """Validate language"""
        return language.lower() in ['hindi', 'tamil', 'gujarati', 'marathi']