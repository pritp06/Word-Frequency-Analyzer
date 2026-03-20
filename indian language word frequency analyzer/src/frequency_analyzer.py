# -*- coding: utf-8 -*-
"""Frequency analysis module"""
from collections import Counter
import math

class FrequencyAnalyzer:
    """Analyzes word frequency"""
    
    def __init__(self):
        self.frequency_data = None
        self.total_words = 0
        self.unique_words = 0
    
    def calculate_frequency(self, tokens):
        """Calculate word frequencies"""
        if not tokens:
            return {}
        self.total_words = len(tokens)
        counter = Counter(tokens)
        self.unique_words = len(counter)
        sorted_freq = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        
        freq_with_percentage = {}
        for word, count in sorted_freq.items():
            percentage = (count / self.total_words) * 100
            freq_with_percentage[word] = {'count': count, 'percentage': round(percentage, 2)}
        self.frequency_data = freq_with_percentage
        return freq_with_percentage
    
    def get_statistics(self, tokens):
        """Calculate statistics"""
        if not tokens:
            return {}
        counter = Counter(tokens)
        frequencies = list(counter.values())
        total = len(tokens)
        unique = len(counter)
        avg_freq = total / unique if unique > 0 else 0
        max_freq = max(frequencies) if frequencies else 0
        min_freq = min(frequencies) if frequencies else 0
        
        variance = sum((x - avg_freq) ** 2 for x in frequencies) / len(frequencies) if frequencies else 0
        std_dev = math.sqrt(variance)
        lexical_diversity = unique / total if total > 0 else 0
        
        return {
            'total_words': total,
            'unique_words': unique,
            'average_frequency': round(avg_freq, 2),
            'max_frequency': max_freq,
            'min_frequency': min_freq,
            'standard_deviation': round(std_dev, 2),
            'lexical_diversity': round(lexical_diversity, 4),
            'lexical_richness_percentage': round(lexical_diversity * 100, 2)
        }
    
    def get_top_words(self, n=10):
        """Get top N words"""
        if not self.frequency_data:
            return {}
        return dict(list(self.frequency_data.items())[:n])
    
    def filter_by_frequency(self, min_freq=2):
        """Filter by frequency"""
        if not self.frequency_data:
            return {}
        return {w: d for w, d in self.frequency_data.items() if d['count'] >= min_freq}