# Simple Flask app for serving the frontend and exposing the NLP backend
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
from src.text_processor import TextProcessor
from src.frequency_analyzer import FrequencyAnalyzer

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app) # allow requests between localhost domains if needed

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    language = data.get('language', 'hindi')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        processor = TextProcessor(language=language)
        processed_text = processor.normalize_text(text)
        tokens = processor.tokenize(processed_text)
        filtered_tokens = processor.remove_stopwords(tokens)
        
        analyzer = FrequencyAnalyzer()
        frequency_data = analyzer.calculate_frequency(filtered_tokens)
        stats = analyzer.get_statistics(filtered_tokens)

        # structure the JSON to be consumed cleanly by JS
        sorted_words = []
        for word, value in frequency_data.items():
            sorted_words.append([word, value['count']])

        return jsonify({
            'words': sorted_words,
            'stats': {
                'total': stats['total_words'],
                'unique': stats['unique_words'],
                'avgFreq': stats['average_frequency'],
                'richness': stats['lexical_richness_percentage']
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
