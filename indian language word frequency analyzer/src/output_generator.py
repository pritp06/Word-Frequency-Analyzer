# -*- coding: utf-8 -*-
"""Output generation"""
import json
import csv
from datetime import datetime

class OutputGenerator:
    """Generates formatted output"""
    
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def display_frequency_table(self, frequency_data, top_n=20):
        """Display frequency table"""
        print(f"\n{'Rank':<6} {'Word':<20} {'Count':<10} {'Percentage':<12}")
        print("-" * 50)
        items = list(frequency_data.items())[:top_n]
        for idx, (word, data) in enumerate(items, 1):
            word_display = word[:20] if len(word) > 20 else word
            print(f"{idx:<6} {word_display:<20} {data['count']:<10} {data['percentage']:<12}%")
    
    def display_statistics(self, stats):
        """Display statistics"""
        for key, value in stats.items():
            formatted_key = key.replace('_', ' ').title()
            print(f"{formatted_key}: {value}")
    
    def export_to_json(self, frequency_data, stats, filename):
        """Export to JSON"""
        output = {'timestamp': self.timestamp, 'statistics': stats, 'word_frequencies': frequency_data}
        with open(f"{filename}.json", 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
    
    def export_to_csv(self, frequency_data, filename):
        """Export to CSV"""
        with open(f"{filename}.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Word', 'Count', 'Percentage'])
            for word, data in frequency_data.items():
                writer.writerow([word, data['count'], data['percentage']])