import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define some predefined responses
responses = {
    "greet": ["hello", "hi", "hey"],
    "farewell": ["bye", "goodbye", "see you"],
    "name_query": ["what is your name", "who are you"],
    "thanks": ["thank you", "thanks"]
}

# Define the chatbot response function using spaCy
def chatbot_response(user_input):
    doc = nlp(user_input.lower())
    for token in doc:
        for intent, patterns in responses.items():
            if token.lemma_ in patterns:
                return generate_response(intent)
    return "Sorry, I don't understand that."

# Generate responses based on identified intent
def generate_response(intent):
    if intent == "greet":
        return "Hi there! How can I help you today?"
    elif intent == "farewell":
        return "Goodbye! Have a nice day!"
    elif intent == "name_query":
        return "I am a chatbot created to assist you."
    elif intent == "thanks":
        return "You're welcome!"
    else:
        return "I'm not sure how to respond to that."

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
