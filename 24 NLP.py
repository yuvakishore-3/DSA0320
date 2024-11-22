import nltk
dialog = "How are you? I am fine, thank you."
utterances = nltk.sent_tokenize(dialog)
acts = {"question": "?", "statement": "."}
for utterance in utterances:
    act = "question" if utterance.endswith("?") else "statement"
    print(f"'{utterance}' is a {act}")
