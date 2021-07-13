import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
import pickle
from ..clean_text import clean



def hateModel(X_test):
    if X_test =="":
      return "empty"

    sent_length=20
    model_check = load_model('./app/mlModel/hate_speech/hate_lstm_3.h5')
    with open('./app/mlModel/hate_speech/tokenizer.pkl','rb') as file1:
        tokenizer = pickle.load(file1)
    
    X_test =clean.clean_doc(X_test)
    one_hot_repr_test = tokenizer.texts_to_sequences(X_test)
    pad_sent_test = pad_sequences(one_hot_repr_test,maxlen=sent_length)
    y_pred=np.round(model_check.predict(pad_sent_test)).astype(int)

    if y_pred[0]==0:
          y_pred="positive"
    else:
          y_pred="negative"
    return y_pred
    
