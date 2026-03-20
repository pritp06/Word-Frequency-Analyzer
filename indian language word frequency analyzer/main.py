#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main entry point"""

import sys
from src.text_processor import TextProcessor
from src.frequency_analyzer import FrequencyAnalyzer
from src.output_generator import OutputGenerator
from utils.file_handler import FileHandler
from utils.validators import InputValidator

def display_menu():
    print("\n" + "="*60)
    print("Indian Language Word Frequency Analyzer")
    print("="*60)
    print("\nSelect input method:")
    print("1. Enter text directly")
    print("2. Load text from file")
    print("3. Exit")
    print("-"*60)

def select_language():
    print("\nAvailable Languages:")
    print("1. Hindi (हिन्दी)")
    print("2. Tamil (தமிழ்)")
    print("3. Gujarati (ગુજરાતી)")
    print("4. Marathi (मराठी)")
    print("-"*60)
    choice = input("Select language (1-4): ").strip()
    language_map = {'1': 'hindi', '2': 'tamil', '3': 'gujarati', '4': 'marathi'}
    return language_map.get(choice, 'hindi')

def get_text_input():
    print("\nEnter your text (press Enter twice to finish):")
    print("-"*60)
    lines = []
    empty_count = 0
    try:
        while True:
            line = input()
            if line:
                lines.append(line)
                empty_count = 0
            else:
                empty_count += 1
                if empty_count >= 2:
                    break
    except EOFError:
        pass
    return '\n'.join(lines)

def get_file_input():
    file_path = input("Enter file path: ").strip()
    if not InputValidator.validate_file_path(file_path):
        print("Error: File not found!")
        return None
    return FileHandler.read_file(file_path)

def analyze_and_display(text, language):
    if not InputValidator.validate_text(text):
        print("Error: Text is empty!")
        return
    print("\n" + "="*60)
    print("Processing text...")
    print("="*60)
    try:
        processor = TextProcessor(language=language)
        processed_text = processor.normalize_text(text)
        tokens = processor.tokenize(processed_text)
        print(f"✓ Tokenized into {len(tokens)} tokens")
        filtered_tokens = processor.remove_stopwords(tokens)
        print(f"✓ Removed stopwords ({len(tokens) - len(filtered_tokens)} removed)")
        analyzer = FrequencyAnalyzer()
        frequency_data = analyzer.calculate_frequency(filtered_tokens)
        print(f"✓ Analyzed {len(frequency_data)} unique words")
        output_gen = OutputGenerator()
        print("\n" + "="*60)
        print("WORD FREQUENCY ANALYSIS RESULTS")
        print("="*60)
        output_gen.display_frequency_table(frequency_data, top_n=20)
        print("\n" + "="*60)
        print("STATISTICS")
        print("="*60)
        stats = analyzer.get_statistics(filtered_tokens)
        output_gen.display_statistics(stats)
        export_choice = input("\nExport results? (y/n): ").strip().lower()
        if export_choice == 'y':
            export_format = input("Format (1=JSON, 2=CSV): ").strip()
            output_file = input("Filename (no extension): ").strip()
            if export_format == '1':
                output_gen.export_to_json(frequency_data, stats, output_file)
                print(f"✓ Exported to {output_file}.json")
            elif export_format == '2':
                output_gen.export_to_csv(frequency_data, output_file)
                print(f"✓ Exported to {output_file}.csv")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    try:
        while True:
            display_menu()
            choice = input("Enter choice (1-3): ").strip()
            if choice == '1':
                text = get_text_input()
                if text:
                    language = select_language()
                    analyze_and_display(text, language)
            elif choice == '2':
                text = get_file_input()
                if text:
                    language = select_language()
                    analyze_and_display(text, language)
            elif choice == '3':
                print("\nThank you! Exiting...")
                break
            else:
                print("Invalid choice!")
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()