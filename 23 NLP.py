from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ["Cats are friendly animals", "Dogs are loyal pets"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
coherence_score = (X * X.T).A[0, 1]
print("Coherence Score:", coherence_score)
