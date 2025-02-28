 # CDP Chatbot

This project is a simple chatbot built using Flask and spaCy that can answer questions about various Customer Data Platforms (CDPs) by fetching and extracting information from their documentation.

## Setup

1. Create a new directory and navigate into it:
    ```sh
    mkdir cdp_chatbot
    cd cdp_chatbot
    ```

2. Set up a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install flask requests beautifulsoup4 spacy
    python -m spacy download en_core_web_sm
    ```

## Running the Application

1. Ensure you are in the project directory and the virtual environment is activated.

2. Run the Flask application:
    ```sh
    python data.py
    ```

3. The application will start and be accessible at `http://127.0.0.1:5000`.

## API Endpoint

### POST /ask

This endpoint accepts a JSON payload with a  field and returns an answer based on the recognized entities in the question.