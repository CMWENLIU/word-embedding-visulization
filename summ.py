#from summarizer import SingleModel
#from gensim.summarization.summarizer import summarize
from summa.summarizer import summarize
import os
import re
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
'''
module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/3" #@param ["https://tfhub.dev/google/universal-sentence-encoder/2", "https://tfhub.dev/google/universal-sentence-encoder-large/3"]
# Import the Universal Sentence Encoder's TF Hub module
embed = hub.Module(module_url)

sts_input1 = tf.placeholder(tf.string, shape=(None))
sts_input2 = tf.placeholder(tf.string, shape=(None))

# For evaluation we use exactly normalized rather than
# approximately normalized.
sts_encode1 = tf.nn.l2_normalize(embed(sts_input1), axis=1)
sts_encode2 = tf.nn.l2_normalize(embed(sts_input2), axis=1)
cosine_similarities = tf.reduce_sum(tf.multiply(sts_encode1, sts_encode2), axis=1)
clip_cosine_similarities = tf.clip_by_value(cosine_similarities, -1.0, 1.0)
sim_scores = 1.0 - tf.acos(clip_cosine_similarities)


'''
#model = SingleModel()
datapath = '/home/bear/bigdata/'


def summ(s):
 fs = s.split('-!!-')
 ss = fs[1].split('-##-')
 sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', ss[0])
 sentences.append(fs[0])
 body = ' '.join(sentences)
 summ = summarize(body, split=True)
 gt = [ss[1]]*len(summ)
 return summ, gt

  

def run_sts_benchmark(session):
  """Returns the similarity scores"""
  emba, embb, scores = session.run(
      [sts_encode1, sts_encode2, sim_scores],
      feed_dict={
          sts_input1: text_a,
          sts_input2: text_b
      })
  return scores



with open (os.path.join(datapath, 'filtered20w.txt')) as inputf:
 count, shot= 0, 0
 for line in inputf:
  fs = line.split('-!!-')
  ss = fs[1].split('-##-')
  sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', ss[0])
  sentences.append(fs[0])
  if len(sentences) > 2:
   scores = []
   text_a , text_b = summ(line)
   if len(text_a) > 1:
    for i in range(len(text_a)):
     scores.append(fuzz.partial_ratio(text_a[i], text_b[i]))
    count += 1
    if max(scores) > 60:
     shot += 1
    print(scores)
    print(shot/count)


'''
with open (os.path.join(datapath, 'filtered20w.txt')) as inputf:
 count, shot= 0, 0
 for line in inputf:
  fs = line.split('-!!-')
  ss = fs[1].split('-##-')
  sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', ss[0])
  sentences.append(fs[0])
  if len(sentences) > 2:
   text_a , text_b = summ(line)
   with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    session.run(tf.tables_initializer())
    scores = run_sts_benchmark(session)
    count += 1
    if max(scores) > 0.7:
     shot += 1
    print(scores)
    print(shot/count)
''' 
