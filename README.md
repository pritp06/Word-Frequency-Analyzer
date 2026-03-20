Indian Language Word Frequency Analyzer

A Python-based application for analyzing word frequency in Indian languages such as Hindi, Tamil, Gujarati, and Marathi. The system processes Unicode text, applies NLP techniques, and generates meaningful statistical insights.

---

 📌 Overview

This project is designed to perform text analysis on Indian language inputs. It processes raw text, removes noise, tokenizes words, and calculates frequency distribution along with useful metrics.

The system supports both:

* Command Line Interface (CLI)
* Web-based interface using Flask

---

🚀 Features

* Unicode support for multiple Indian scripts
* Word frequency calculation and ranking
* Stopword removal and text preprocessing
* Lexical statistics (frequency %, diversity)
* CLI-based interaction
* Flask-based web application
* Export results in JSON and CSV formats
* Modular and scalable architecture

---

 🛠️ Technologies Used

* Python 3.6+ – Core programming language
* Flask & Flask-CORS – Backend API and web interface
* NLTK – Tokenization and NLP support
* NumPy – Data processing
* JSON / CSV – Data storage and export

---

🌐 Supported Languages

* Hindi (हिन्दी)
* Tamil (தமிழ்)
* Gujarati (ગુજરાતી)
* Marathi (मराठी)

---

⚙️ Installation Guide

1. Clone the Repository

```bash
git clone <your-repository-link>
cd indian-language-word-frequency-analyzer
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

▶️ How to Run

Option 1: Command Line Interface (CLI)

```bash
python main.py
```

You can:

* Enter text manually
* Upload a text file
* Select language
* View analysis results
* Export results

---

Option 2: Web Application (Flask)

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

📊 Output

The system provides:

* Word frequency count
* Percentage distribution
* Sorted word ranking

Export files:

* output.json
* output.csv

---

📁 Project Structure

```
project-root/

├── main.py              # CLI application
├── app.py               # Flask backend
├── requirements.txt     # Dependencies

├── src/                 # Core processing logic
│   ├── tokenizer.py
│   ├── frequency.py
│   ├── preprocessing.py

├── config/              # Language configurations
├── utils/               # Helper functions
├── tests/               # Unit testing
```

---

🧠 Methodology (Short)

1. Input text (manual/file)
2. Text preprocessing (cleaning, normalization)
3. Tokenization
4. Stopword removal
5. Frequency calculation
6. Statistical analysis
7. Output display and export

---

⚠️ Limitations

* No semantic understanding of text
* Limited stopword coverage per language
* No advanced NLP features like stemming or POS tagging

---

🔮 Future Improvements

* Add stemming and lemmatization
* Improve multilingual support
* Add data visualization (graphs, word clouds)
* Integrate machine learning models
* Deploy as a full web application

---

📄 License
MIT License

Copyright (c) 2026 Patel Prit

Free to use, modify, and distribute this software with proper credit to the author.

This software is provided "as is", without warranty of any kind.
