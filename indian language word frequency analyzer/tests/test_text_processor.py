# -*- coding: utf-8 -*-
"""Text processor tests"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.text_processor import TextProcessor

def test_normalize():
    p = TextProcessor('hindi')
    assert p.normalize_text("नमस्ते  दुनिया") == "नमस्ते दुनिया"

if __name__ == '__main__':
    test_normalize()
    print("Tests passed!")