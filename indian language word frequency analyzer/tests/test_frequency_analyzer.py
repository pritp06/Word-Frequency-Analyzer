# -*- coding: utf-8 -*-
"""Frequency analyzer tests"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.frequency_analyzer import FrequencyAnalyzer

def test_frequency():
    a = FrequencyAnalyzer()
    tokens = ['word', 'word', 'test', 'test', 'test']
    freq = a.calculate_frequency(tokens)
    assert freq['word']['count'] == 2
    assert freq['test']['count'] == 3

if __name__ == '__main__':
    test_frequency()
    print("Tests passed!")