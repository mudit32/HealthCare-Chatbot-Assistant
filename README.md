# Healthcare Assistant Chatbot

## Overview

The Healthcare Assistant Chatbot is an AI-powered application developed using Python, Streamlit, NLTK, and the DistilGPT-2 transformer model. The chatbot assists users by answering healthcare-related queries and generating context-aware responses using Natural Language Processing (NLP) techniques.

## Features

* Interactive web interface built with Streamlit
* AI-generated responses using DistilGPT-2
* Healthcare-specific query handling
* Natural Language Processing (NLP) using NLTK
* Real-time response generation
* User-friendly interface

## Technologies Used

* Python
* Streamlit
* Transformers (Hugging Face)
* DistilGPT-2
* NLTK
* TensorFlow
* tf-keras

## Project Structure

```text
Healthcare-Assistant-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Healthcare-Assistant-Chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Requirements

Create a requirements.txt file with:

```text
streamlit
transformers
tensorflow
nltk
tf-keras
```

## Running the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## How It Works

1. User enters a healthcare-related query.
2. Input text is processed using NLP techniques.
3. Predefined healthcare responses are returned for common queries.
4. For general questions, DistilGPT-2 generates a context-aware response.
5. The response is displayed through the Streamlit interface.

## NLP Concepts Used

* Text Preprocessing
* Tokenization
* Stop Word Handling
* Language Modeling
* Natural Language Understanding
* Context-Based Response Generation

## Sample Queries

* What are the symptoms of fever?
* Tell me about common medications.
* How can I book a doctor's appointment?
* What causes headaches?

## Future Enhancements

* Integration with medical databases
* Voice-based interaction
* Appointment scheduling system
* Multi-language support
* Medical report analysis

## Author

Mudit Chahar

B.Tech Computer Science & Engineering

Graphic Era Deemed To Be University
