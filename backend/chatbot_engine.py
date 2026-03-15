import json

with open("data/knowledge_base.json") as f:
    knowledge = json.load(f)

def get_response(user_input):

    user_input = user_input.lower()

    for key in knowledge:
        if key in user_input:
            return knowledge[key]

    return "Sorry, I don't have information about that yet."