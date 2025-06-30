import os
import pickle
import faiss
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer

documents = []
directory = 'ENTER_YOUR_FILE_DIRECTORY' # Edit to the path of your files
for filename in os.listdir(directory):
    if filename.lower().endswith('.pdf'):
        full_path = os.path.join(directory, filename)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        documents.append(text)

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(documents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

with open('documents.pkl', 'wb') as f:
    pickle.dump(documents, f)
faiss.write_index(index, 'faiss_index.index')

print("FAISS index and documents saved from PDFs.")