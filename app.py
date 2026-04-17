import spacy
import random
import streamlit as st

st.title("Fun Word Game!")

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

text = st.text_input("Please paste some text")

# text = ("Schuyler is a small, white cat. She loves to purr loudly. Schuyler lives in Minnesota. Her favorite activities are sleeping, playing, and sitting on people's laps. She is 14 years old - Wow! When she was a kitten, she meowed a lot and ran quickly.")
if text:
    doc = nlp(text)


    # Analyze syntax
    for token in doc:
        print(token.text, token.pos_, token.tag_)

    COLOR = {"pink", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple",
            "brown", "black", "white", "vermillion", "scarlet", "tan", "beige", "silver", "off-white",
            "gold", "magenta", "chartreuse", "cyan", "cerulean", "gray", "grey", "auburn", "blonde"}


    # Name parts of speech
    # Create a dictionary of lists
    results = {
    "proper noun": [],
    "noun singular": [],
    "noun plural": [],
    "adjective": [],
    "verb": [],
    "verb past tense": [],
    "verb ending in -ing": [],
    "adverb": [],
    "number": [],
    "interjection": [],
    "color": []
}

    # Add parts of speach to grouped lists
    for token in doc:
        if token.tag_ == "NNP":
            results["proper noun"].append(token.text)
        elif token.tag_ == "NN":
            results["noun singular"].append(token.text)
        elif token.tag_ == "NNS":
            results["noun plural"].append(token.text)
        elif token.text.lower() in COLOR:
            results["color"].append(token.text)
        elif token.pos_ == "ADJ":
            results["adjective"].append(token.text)
        elif token.tag_ == "VB":
            results["verb"].append(token.text)
        elif token.tag_ == "VBD":
            results["verb past tense"].append(token.text)
        elif token.tag_ == "VBG":
            results["verb ending in -ing"].append(token.text)
        elif token.pos_ == "ADV":
            results["adverb"].append(token.text)
        elif token.pos_ == "NUM":
            results["number"].append(token.text)
        elif token.pos_ == "INTJ":
            results["interjection"].append(token.text)

# for category, words in results.items():
#     print(f"{category.title()}: {words}")

    # For each list, remove a random amount of items, but always leave at least 1
    for category, items in results.items():
        if len(items) > 1:
            max_number = len(items)
            random_number = random.randrange(1, max_number)

            to_remove = random.sample(items, random_number)
            print("Items to remove:", f"{category.title()}:", to_remove)

            for item in to_remove:
                items.remove(item)


    for category, words in results.items():
        print("After removal:", f"{category.title()}: {words}")

    # Convert lists to a dictionary lookup table for ease in searching
    word_to_category = {}

    for category, words in results.items():
        for word in words:
            word_to_category[word.lower()] = category

    # Now replace words with categories
    new_text = []

    for token in doc:
        replacement = token.text
        if token.text.lower() in word_to_category:
            # Replace word with category title
            replacement = word_to_category[token.text.lower()].title()
            
        new_text.append(replacement)

    print("New text:", " ".join(new_text))

    st.write("The new text with category name substitutions is:")
    st.write(f"{" ".join(new_text)}")


# for token in doc:
#     if token.tag_ == "NNP":
#         new_text.append("PROPER NOUN")
#     elif token.tag_ == "NN":
#         new_text.append("NOUN SINGULAR")
#     elif token.tag_ == "NNS":
#         new_text.append("NOUN PLURAL")
#     elif token.text.lower() in COLOR:
#         new_text.append("COLOR")
#     elif token.pos_ == "ADJ":
#         new_text.append("ADJECTIVE")
#     elif token.tag_ == "VB":
#         new_text.append("VERB")
#     elif token.tag_ == "VBD":
#         new_text.append("VERB PAST TENSE")
#     elif token.tag_ == "VBG":
#         new_text.append("VERB ENDING IN -ING")
#     elif token.pos_ == "ADV":
#         new_text.append("ADVERB")
#     elif token.pos_ == "NUM":
#         new_text.append("NUMBER")
#     elif token.pos_ == "INTJ":
#         new_text.append("INTERJECTION")
#     else:
#         new_text.append(token.text)

# new_text_result = " ".join(new_text)

# print(new_text_result)