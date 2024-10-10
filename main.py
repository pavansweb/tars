import spacy
import wikipedia
from greeting import greeting_gen

#---------------------------------------------------------------------------------
# nlp setup
nlp = spacy.load("en_core_web_sm")

#--------------------------------------------------------------------------------

# function to expand abbreviatives
def expand_abbreviatives(query):
    abbreviatives = {
        "hi": "hello",
        "hey": "hello",
        "hola": "hello",
        "greetings": "hello",
        "salutations": "hello",
        "howdy": "hello",
        "what's up": "hello",
        "yo": "hello",
        "sup": "hello",
        "ahoy": "hello",
        "bonjour": "hello",
        "ciao": "hello",
        "namaste": "hello",
    }

    sentence = query.split()
    expanded_sentence = [abbreviatives.get(word, word) for word in sentence]
    return " ".join(expanded_sentence)

#-------------------------------------------------------------------------------

# identify intent
def identify_intent(query):
    doc = nlp(query)

    wikipedia_keywords = [
        "what", "define", "explain", "tell", "describe", 
        "information", "details", "overview", "history", 
        "facts", "summary", "how", "purpose", 
        "significance", "features", "benefits", 
        "consequences", "origins", "examples", 
        "differences", "comparisons", "who", 
        "where", "when", "why", "which", 
        "can", "could", "would", "should", 
        "is", "are", "do", "does", 
        "did", "have", "has", "might", 
        "may"
    ]

    if any(token.lemma_ == "hello" for token in doc):
        return "greeting"
    elif any(token.lemma_ in wikipedia_keywords for token in doc):
        return "wikipedia"
    else:
        return None

#--------------------------Functions------------------------------------

# wikipedia search function
def process_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result

    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

    except Exception as e:
        return f"An error occurred: {str(e)}"

#---------------------------The main loop--------------------------------

while True:
    # take user input
    user_input = input("User:")
    query = user_input.lower()

    expanded_sentence = expand_abbreviatives(query)
    intent = identify_intent(expanded_sentence)

    if intent == "greeting":
        response = greeting_gen()
    elif intent == "wikipedia":
        response = process_wikipedia(query)
    else:
        response = "I'm sorry, I didn't understand your input."

    print(f"Tars: {response}")
