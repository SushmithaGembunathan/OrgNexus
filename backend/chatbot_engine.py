import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("data/knowledge_base.json") as f:
    knowledge = json.load(f)

def get_response(user_input):

    user_doc = nlp(user_input)

    best_match = None
    highest_similarity = 0

    for question in knowledge:

        question_doc = nlp(question)

        similarity = user_doc.similarity(question_doc)

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = question

    if highest_similarity > 0.5:
        return knowledge[best_match]

    return "Sorry, I couldn't understand that. Please rephrase your question."