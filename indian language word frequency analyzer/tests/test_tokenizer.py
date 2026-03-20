# -*- coding: utf-8 -*-
"""Tokenizer tests"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tokenizer import Tokenizer

def test_tokenize():
    t = Tokenizer('hindi')
    tokens = t.tokenize("नमस्ते दुनिया")
    assert isinstance(tokens, list)
    assert len(tokens) > 0

if __name__ == '__main__':
    test_tokenize()
    print("Tests passed!")