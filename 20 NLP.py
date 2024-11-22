from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ["The car is driven on the road", "The truck is driven on the highway"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print("TF-IDF Matrix:\n", X.toarray())
print("Feature Names:", vectorizer.get_feature_names_out())
 
