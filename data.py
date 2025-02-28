from flask import Flask, request, jsonify
import spacy
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
DOC_URLS = {
    "segment": "https://segment.com/docs/?ref=nav",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def fetch_documentation(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_information(cdp, task):
    url = DOC_URLS.get(cdp)
    if not url:
        return "CDP not recognized."
    
    soup = fetch_documentation(url)
    return f"Information about {task} in {cdp}."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    doc = nlp(question)
    cdp = None
    task = None
    
    # Simple entity recognition (placeholder implementation)
    for ent in doc.ents:
        if ent.label_ == "ORG":
            cdp = ent.text.lower()
        elif ent.label_ == "TASK":
            task = ent.text.lower()
    
    if not cdp or not task:
        return jsonify({"error": "Could not understand the question"}), 400
    
    answer = extract_information(cdp, task)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)