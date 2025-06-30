import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import pickle
from google.generativeai import GenerativeModel
import google.generativeai as genai
import sys
import re

# ------------- Setup block -------------------

st.set_page_config(page_title="Behavioral Interview Coach", layout="wide")
st.markdown("""
    <style>
        .big-title { font-size: 36px; font-weight: bold; }
        .response-box { background-color: #000000; padding: 20px; border-radius: 8px; }
        .footer { font-size: 12px; color: gray; margin-top: 50px; text-align: center; }
    </style>
""", unsafe_allow_html=True)


# Load FAISS index
index = faiss.read_index('faiss_index.index')

# Load documents (your life/work stories)
with open('documents.pkl', 'rb') as f:
    raw_documents = pickle.load(f)

# Normalize and preprocess documents
documents = [re.sub(r'[^\w\s]', '', doc.lower()) for doc in raw_documents]

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize Gemini with error handling
try:
    genai.configure(api_key="ENTER_YOUR_GEMINI_API_KEY")
except Exception as e:
    st.error("Error configuring Gemini API: " + str(e))
    st.stop()

gemini_model = GenerativeModel('gemini-2.5-flash')

# ------------- Retrieval and prompting block -------------------
def retrieve_stories(question, top_k=5):
    clean_question = re.sub(r'[^\w\s]', '', question.lower())
    query_embedding = model.encode([clean_question])
    D, I = index.search(query_embedding, top_k)
    return [raw_documents[i] for i in I[0]]

def build_gemini_prompt(question, retrieved_stories):
    prompt = f"""
You are an expert interview coach.

Given the following behavioral interview question: "{question}"

And the following incidents and stories from my professional and personal background:

{chr(10).join(retrieved_stories)}

Select the most relevant incidents or stories I can talk about in response to the question. List all possible stories/incidents.
If you do not find any relevant stories or incidents, explicitly mention that and help me understand where I can look to remember any possible stories.

For the best recommended story, structure it in STAR format:
- Situation: set the context clearly
- Task: what was the task or challenge
- Action: what did I specifically do
- Result: the outcome, ideally with measurable or concrete results

Additionally, suggest potential follow-up questions the interviewer might ask for the best story, and provide tips on tone, delivery, and points to emphasize to make the answer impactful.

Provide the final answer in polished interview language, ready for me to use and talk. Omit out the start and end comments that you give.

Also, explain why you picked these stories and how they align with the question requirements.
"""
    return prompt

# ------------- Streamlit UI block -------------------
st.markdown('<div class="big-title">Behavioral Interview Answer Generator</div>', unsafe_allow_html=True)

st.write("Enter your behavioral interview question below. Our AI coach will find the best stories from your background and craft an answer in STAR format.")

question = st.text_area("Your Question:")

if st.button("Generate Answer") and question.strip():
    snippets = retrieve_stories(question)
    prompt = build_gemini_prompt(question, snippets)
    with st.spinner("Generating your answer..."):
        response = gemini_model.generate_content(prompt)
    st.subheader("Generated Answer")
    st.markdown(f'<div class="response-box">{response.text}</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Behavioral Interview Coach - powered by Gemini</div>', unsafe_allow_html=True)