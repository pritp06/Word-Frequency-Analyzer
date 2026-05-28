# Indian Language Word Frequency Analyzer

## Overview

The Indian Language Word Frequency Analyzer is a Python-based application developed for analyzing textual data in multiple Indian languages, including Hindi, Tamil, Gujarati, and Marathi. The system processes Unicode text inputs, applies natural language processing techniques, and generates statistical insights related to word usage and distribution.

The application is designed to support both command-line and web-based interactions, providing flexibility for different usage environments.

---

## Features

* Unicode support for multiple Indian language scripts
* Word frequency analysis and ranking
* Text preprocessing and stopword removal
* Lexical statistics and frequency distribution analysis
* Command Line Interface (CLI) support
* Web-based interface using Flask
* Export functionality in JSON and CSV formats
* Modular and scalable project architecture

---

## Technologies Used

| Technology  | Purpose                               |
| ----------- | ------------------------------------- |
| Python 3.6+ | Core programming language             |
| Flask       | Web framework for backend services    |
| Flask-CORS  | Cross-Origin Resource Sharing support |
| NLTK        | Tokenization and NLP processing       |
| NumPy       | Data handling and processing          |
| JSON / CSV  | Data export and storage formats       |

---

## Supported Languages

The application currently supports the following Indian languages:

* Hindi (हिन्दी)
* Tamil (தமிழ்)
* Gujarati (ગુજરાતી)
* Marathi (मराठी)

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd indian-language-word-frequency-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Option 1: Command Line Interface (CLI)

Run the CLI application using:

```bash
python main.py
```

The CLI allows users to:

* Enter text manually
* Upload text files
* Select the target language
* View analysis results
* Export processed data

---

### Option 2: Flask Web Application

Run the Flask application using:

```bash
python app.py
```

Access the application in a web browser at:

```text
http://127.0.0.1:5000
```

---

## Output

The system generates the following outputs:

* Word frequency counts
* Percentage-based frequency distribution
* Ranked word lists based on occurrence frequency

Supported export formats include:

* `output.json`
* `output.csv`

---

## Project Structure

```text
project-root/

├── main.py
├── app.py
├── requirements.txt

├── src/
│   ├── tokenizer.py
│   ├── frequency.py
│   ├── preprocessing.py

├── config/
├── utils/
├── tests/
```

### Directory Description

| Directory/File | Description                        |
| -------------- | ---------------------------------- |
| `main.py`      | Command Line Interface application |
| `app.py`       | Flask-based web backend            |
| `src/`         | Core text processing modules       |
| `config/`      | Language-specific configurations   |
| `utils/`       | Utility and helper functions       |
| `tests/`       | Unit testing modules               |

---

## Methodology

The system follows the workflow below:

1. Input text acquisition through manual entry or file upload
2. Text preprocessing and normalization
3. Tokenization of textual content
4. Stopword identification and removal
5. Word frequency computation
6. Statistical analysis generation
7. Output presentation and export

---

## Limitations

* The system does not perform semantic analysis of text
* Stopword coverage is limited for certain languages
* Advanced NLP functionalities such as stemming, lemmatization, and part-of-speech tagging are not currently implemented

---

## Future Enhancements

Potential future improvements include:

* Integration of stemming and lemmatization techniques
* Expansion of multilingual support
* Addition of graphical visualizations and word clouds
* Integration of machine learning-based text analysis models
* Deployment as a fully hosted web application

---

## License

MIT License

Copyright (c) 2026 Patel Prit

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to use, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to proper attribution to the original author.

The software is provided "as is", without warranty of any kind, express or implied.
