from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

twenty_train = fetch_20newsgroups(subset='train',shuffle=True)
categories = twenty_train.target_names[:4]
twenty_train = fetch_20newsgroups(subset='train',categories=categories,shuffle=True)
twenty_test = fetch_20newsgroups(subset='test',categories=categories,shuffle=True)

tfidf_transformer = CountVectorizer()
X_train_tfidf = tfidf_transformer.fit_transform(twenty_train.data)

mod = MultinomialNB()
mod.fit(X_train_tfidf, twenty_train.target)

X_test_tfidf = tfidf_transformer.transform(twenty_test.data)
predicted = mod.predict(X_test_tfidf)

print("Accuracy:", accuracy_score(twenty_test.target, predicted)*100)
print(classification_report(twenty_test.target,predicted,target_names=twenty_test.target_names))
print("confusion matrix is \n",confusion_matrix(twenty_test.target, predicted))