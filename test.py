import spacy
import wikipedia
from wikipedia.exceptions import WikipediaException

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract the main topic from the query
def extract_main_topic(query):
    doc = nlp(query)

    # Find all proper nouns (which might be the main topic)
    for token in doc:
        if token.pos_ == "PROPN":  # Proper noun (e.g. AI, Python, Linux)
            return token.text

    # If no proper noun is found, return the most significant noun
    for token in doc:
        if token.pos_ == "NOUN":  # Nouns (e.g. technology, system)
            return token.text

    return None  # If no noun found, return None

# Wikipedia search function
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except WikipediaException:
        return "Sorry, I couldn't find any information on that topic."

# Main processing function
def process_query(query):
    main_topic = extract_main_topic(query)

    if main_topic:
        response = search_wikipedia(main_topic)
        return response
    else:
        return "I'm sorry, I couldn't understand your query."

# Main loop to get user input
while True:
    user_query = input("User: ")
    if user_query.lower() == "exit":
        break
    response = process_query(user_query)
    print(f"TARS: {response}")
