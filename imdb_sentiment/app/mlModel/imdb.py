import numpy as np
import pickle
import regex as re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
sw = stopwords.words('english')
ps = PorterStemmer()


def imdbModel(X_test):
    with open('./app/mlModel/tf.pkl','rb') as file1:
        tf = pickle.load(file1)
    corpus = clean_doc([X_test])
    corpus = tf.transform(corpus)
    with open('./app/mlModel/imdb_lr (1).pkl','rb') as file2:
        model_lr=pickle.load(file2)
    y_pred = model_lr.predict(corpus)
    if y_pred[0]==1:
          y_pred="positive"
    else:
          y_pred="negetive"
    return y_pred




def clean_sents(sent):
  clean_sent = re.sub('[^a-zA-Z]',' ',sent)
  clean_sent = clean_sent.lower()
  clean_sent = clean_sent.split()
  clean_sent = [ps.stem(x) for x in clean_sent if x not in sw]
  clean_sent = ' '.join(clean_sent)
  return clean_sent

def clean_doc(doc):
  corpus = []
  for sent in doc:
    clean_sent = clean_sents(sent)
    corpus.append(clean_sent)
  return corpus

