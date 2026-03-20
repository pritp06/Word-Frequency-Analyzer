# -*- coding: utf-8 -*-
"""File handling"""
import os

class FileHandler:
    """File I/O operations"""
    
    @staticmethod
    def read_file(file_path, encoding='utf-8'):
        """Read file"""
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
    
    @staticmethod
    def write_file(file_path, content, encoding='utf-8'):
        """Write file"""
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
    
    @staticmethod
    def file_exists(file_path):
        """Check if exists"""
        return os.path.isfile(file_path)