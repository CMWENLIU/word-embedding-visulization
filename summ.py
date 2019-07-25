from summarizer import SingleModel
import os
import re

#model = SingleModel()
datapath = '/home/bear/bigdata/'

with open (os.path.join(datapath, 'filtered20w.txt')) as inputf:
 for line in inputf:
  fs = line.split('-!!-')
  ss = fs[1].split('-##-')
  sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', ss[0])
  sentences.append(fs[0])
  body = ' '.join(sentences)
  summ = ss[1]
  #return sentences, summ
  model = SingleModel()
  result = model(body, ratio=0.2)
  full = ''.join(result)
  print('Following is summarized result:-----------')
  print(full)
  print('Ground truth:-----------------------------')
  print(summ)
  
