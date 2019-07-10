import string
import nltk
import os
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
set(stopwords.words('english'))

def remove_stopwords(s):  
  stop_words = set(stopwords.words('english'))   
  word_tokens = word_tokenize(s)  
  filtered_sentence = [w for w in word_tokens if not w in stop_words]   
  filtered_sentence = []
  for w in word_tokens: 
    if w not in stop_words: 
      filtered_sentence.append(w) 
  return ' '.join(filtered_sentence)
i = 1
with open(os.path.join('/home/bear/bigdata/', 'tox30000.txt'), 'w') as wf:
 with open('/home/bear/bigdata/tox_allinfor.txt', 'r') as rf:
  for line in rf:
   if '-##-' in line and i < 30000:
    s = line.split('-##-', 1)[1].replace('\n', '').lower()
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = remove_stopwords(s)
    wf.write(s)
    print(str(i) + 'finish')
   i += 1




