import spacy
import json
from greeting import greeting_gen
from spacy.cli import download
from api import process_gemini_query
from fuzzywuzzy import process

#---------------------------------------------------------------------------------
# nlp setup
download("en_web_core_sm")
nlp = spacy.load("en_core_web_sm")


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
    words = ["hello", "hi", "hey", "hola", "greetings", "salutations", "howdy", "what's up", "yo", "sup", "wsg", "namaste", "weather", "forecast"]

    # Use fuzzy matching to find the closest greeting
    best_match, score = process.extractOne(user_input, words)

    if score >= 85:
        return best_match 
    return user_input 
    
# intent identification using NLP
def identify_intent(query):
    corrected_query = process_spell(query)
    doc = nlp(corrected_query)

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

def main_process(query):
    # Take user input
    user_input = query

    # Correct spelling
    corrected_input = process_spell(user_input)

    # Expand abbreviatives and identify intent
    expanded_sentence = expand_abbreviatives(corrected_input)
    intent = identify_intent(expanded_sentence)

    # Generate appropriate response based on intent
    if intent == "greeting":
        response = greeting_gen()
    else:
        response = process_query(expanded_sentence)

    return response 

#-------------------------------------------------------------------------