import numpy as np
import pickle
from ..clean_text import clean


def imdbModel(X_test):
    if X_test=="":
      return "empty"
    
    with open('./app/mlModel/imdb/tf.pkl','rb') as file1:
        tf = pickle.load(file1)

    corpus = clean.clean_doc([X_test])
    corpus = tf.transform(corpus)

    with open('./app/mlModel/imdb/imdb_lr.pkl','rb') as file2:
        model_lr=pickle.load(file2)

    y_pred = model_lr.predict(corpus)
    if y_pred[0]==1:
          y_pred="positive"
    else:
          y_pred="negetive"
    return y_pred



