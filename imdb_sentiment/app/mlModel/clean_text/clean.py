import numpy as np
import regex as re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
sw = stopwords.words('english')
ps = PorterStemmer()

def clean_sents(sent):
  clean_sent = re.sub('[^a-zA-Z]',' ',sent)
  clean_sent = clean_sent.lower()
  clean_sent = clean_sent.split()
  clean_sent =[ps.stem(str(x)) for x in clean_sent if x not in sw]
  clean_sent =' '.join(clean_sent)
  return clean_sent

def clean_doc(doc):
  corpus=[]
  for sents in doc:
    clean_sent = clean_sents(sents)
    corpus.append(clean_sent)
  return corpus