import tensorflow as tf
#import tensorflow_hub as hub
import numpy as np
import os
import re


def buildSentences(s):
  fs = line.split('-!!-')
  ss = fs[1].split('-##-')
  sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', ss[0])
  sentences.append(fs[0])
  summ = [ss[1]]*len(sentences)
  return sentences, summ

with open('/home/bear/bigdata/out20w.txt', 'r') as inputf:
  for line in inputf:
    text_a , text_b = buildSentences(line)
    print('-------------------')      
    print(text_a)
    print('-------------------')   
    print(text_b)
