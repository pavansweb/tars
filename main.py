import spacy
import json
from greeting import greeting_gen
from extract_topic import process_questioning_query
from test import process_gemini_query
from fuzzywuzzy import process
from spellchecker import SpellChecker

#---------------------------------------------------------------------------------
# nlp setup
nlp = spacy.load("en_core_web_sm")

#spell checker setup
spell = SpellChecker()

#dataset setup
try:
    with open('tars_dataset.json', 'r') as f:
        data = json.load(f)
    question_answers = data['questions_answers']
except FileNotFoundError:
    print("Error: Dataset file not found.")
    question_answers = []

#--------------------------------------------------------------------------------

# function to expand abbreviatives
def expand_abbreviatives(query):
    abbreviatives = {
        "ai": "Artificial intelligence"
    }

    sentence = query.split()
    expanded_sentence = [abbreviatives.get(word, word) for word in sentence]
    return " ".join(expanded_sentence)

#-------------------------------------------------------------------------------

# spell correction
def process_spell(user_input):
    # Define common greeting words
    words = ["hello", "hi", "hey", "hola", "greetings", "salutations", "howdy", "what's up", "yo", "sup", "wsg", "namaste", "weather", "forecast"]

    # Use fuzzy matching to find the closest greeting
    best_match, score = process.extractOne(user_input, words)

    # Set a threshold for acceptable match quality
    if score >= 85:
        return best_match  # Return the corrected greeting
    return user_input 
    
# intent identification using NLP
def identify_intent(query):
    corrected-query = process_spell(query)
    doc = nlp(correct_spelling)

    if any(token.lemma_ in ["hello", "hi", "hey", "hola", "greetings", "salutations", "howdy", "what's up", "yo", "sup", "wsg", "namaste"] for token in doc):
        return "greeting"
    elif any(token.lemma_ in ["weather", "forecast"] for token in doc):
        return "weather"
    else:
        return None

#--------------------------Functions------------------------------------
def process_query(query):
    
    questions = [qa['question'] for qa in question_answers]
    best_match, score = process.extractOne(query, questions)    

    if score >= 85:
        for qa in question_answers:
            if qa['question'] == best_match:
                return qa['answer']
    else:
        return process_gemini_query(query)

#---------------------------The main loop--------------------------------

def run_bot():
    while True:
        # Take user input
        user_input = input("User: ").lower()

        # Correct spelling
        corrected_input = process_spelling(user_input)

        # Expand abbreviatives and identify intent
        expanded_sentence = expand_abbreviatives(corrected_input)
        intent = identify_intent(expanded_sentence)

        # Generate appropriate response based on intent
        if intent == "greeting":
            response = greeting_gen()
        else:
            response = process_query(expanded_sentence)

        print(f"Tars: {response}")

#-------------------------------------------------------------------------
if __name__ == "__main__":
    run_bot()