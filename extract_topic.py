from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample dataset of questioning phrases
questioning_phrases = [
    "what is",
    "define",
    "explain",
    "can you explain",
    "describe",
    "how does",
    "what are",
    "tell me about",
    "what does",
    "is it true that",
    "can you tell me",
    "what's the meaning of",
    "what is the purpose of",
    "who is",
    "where is",
    "when is",
    "why is",
    "which is",
    "how do",
    "what can",
    "can you give me",
    "what would happen if",
    "what should I know about",
    "what's the difference between",
    "what is the significance of",
    "how important is",
    "what examples are there of",
    "what factors contribute to",
    "can you summarize",
    "what are the steps to",
    "what challenges are involved in",
    "how often",
    "what trends are seen in",
    "can you provide details on",
    "what influences"
]


# Labels for the dataset (1 = questioning phrase)
labels = [1] * len(questioning_phrases)

# Use a few non-questioning examples for the classifier
non_questioning_examples = [
    "AI is a technology.",
    "Python is a programming language.",
    "Artificial Intelligence can automate tasks.",
    "Linux is an open-source operating system.",
    "The human body has 206 bones.",
    "Cloud computing provides scalable resources.",
    "Photosynthesis is how plants make food."
]

# Combine and label non-questioning examples as 0
data = questioning_phrases + non_questioning_examples
labels += [0] * len(non_questioning_examples)

# Create a text classification pipeline using Naive Bayes
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(data, labels)

# Function to identify and remove questioning phrases
def process_questioning_query(query):
    query = query.lower()

    # Check each questioning phrase
    for phrase in questioning_phrases:
        if query.startswith(phrase):
            # Remove the identified questioning phrase
            return query[len(phrase):].strip()  # Return the rest of the query, stripped of whitespace

    return query.strip()  # Return the original query if no questioning phrase found


