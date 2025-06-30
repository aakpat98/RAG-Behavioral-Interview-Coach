# RAG Tool For Recalling STAR stories


## Description

This repository contains a Retrieval-Augmented Generation (RAG) powered behavioral interview coach. The tool helps you prepare for behavioral interviews by retrieving relevant incidents and stories from your own personal and professional experiences and generating polished answers in the STAR (Situation, Task, Action, Result) format using Gemini LLM.

You can update your corpus of stories anytime by adding new PDF files and rerunning the embedding script. The interactive Streamlit dashboard provides an intuitive interface to generate and review answers.


## Features

* Upload your personal/professional experience stories as PDFs.
* Embed and index your stories using FAISS and `sentence-transformers`.
* Retrieve top relevant incidents from your corpus in response to any behavioral question.
* Get the best incident structured in STAR format with potential follow-up questions, tone, and delivery tips from Gemini LLM.
* User-friendly Streamlit interface.
* Refresh your index anytime by adding new stories and rerunning the data loader script.


## 📁 Repository Structure

```
behavioral-interview-coach-rag/
│
├── Behavioral_Coach.py         # Streamlit app to interact with the system
├── Data_Loader.py              # Script to process PDFs and build FAISS index
├── faiss_index.index           # Generated FAISS index (not included in repo)
├── documents.pkl               # Pickled documents (not included in repo)
├── documents/                  # Folder where you put your PDF story files
│   ├── story1.pdf
│   ├── story2.pdf
│   └── ...
│
├── README.md                   # This file
│
└── requirements.txt            # Python dependencies (necessary packages mentioned below)
```


## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/behavioral-interview-coach-rag.git
cd behavioral-interview-coach-rag
```

2. **Set up a Python environment**

We recommend using Python 3.9 or newer with `venv`:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```


## Usage

Update ```Data_Loader.py```: Update your folder directory path.

Update ```Behavioral_Coach.py```: Enter your Google Gemini API Key. This project uses the Gemini 2.5 Flash model, which can also be changed in the same file.

### Prepare Your Documents

* Place all your PDF files (containing your stories, projects, or incidents) in the `documents/` folder.
* Each PDF should ideally represent one or more incidents you want the system to retrieve and present in STAR format.

### Build FAISS Index

Run:

```bash
python Data_Loader.py
```

This script will:

* Read all PDFs in `documents/`
* Create normalized embeddings using `sentence-transformers`
* Build and save a FAISS index (`faiss_index.index`) and a pickled documents file (`documents.pkl`)

You can update your corpus anytime by adding new PDFs and rerunning this script.

### Launch the Streamlit App

Run:

```bash
streamlit run Behavioral_Coach.py
```

You will see an interface where you can:

* Enter any behavioral interview question
* Retrieve relevant incidents
* View the Gemini-generated answer in STAR format along with follow-up questions and delivery tips


## Screenshots

**Dashboard View**

<img width="1417" alt="Screenshot 2025-06-29 at 7 13 57 PM" src="https://github.com/user-attachments/assets/3c0f6ee1-d1a6-495b-911d-79c8d890d38b" />

**Generated STAR Answer Example**

<img width="1298" alt="Screenshot 2025-06-29 at 7 15 50 PM" src="https://github.com/user-attachments/assets/243bd34a-0057-4a1e-9759-f3a2bca231eb" />


## Motivation

I built this tool because I often struggled to remember the right stories to match a behavioral interview question. This tool helps me retrieve the best story quickly, ensuring my responses are structured, relevant, and impactful.


## Future Work

* Support richer metadata tagging (skills, industries, themes)
* Integrate feedback loop to improve retrieval quality
* Support exporting answers to PDF/Markdown
* Enhance UI theming and layout


## Requirements

Add these to `requirements.txt`:

```
streamlit
faiss-cpu
sentence-transformers
PyPDF2
google-generativeai
```


## Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss your ideas or improvements.


## License

[MIT](LICENSE)

