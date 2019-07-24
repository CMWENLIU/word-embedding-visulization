import eutils
import pandas as pd
from metapub import PubMedFetcher
import time
fetch = PubMedFetcher()
import os
import glob



def preparing_pairs():
 path = '/home/bear/bigdata/'
 i = 1
 with open(os.path.join(path, "generifs_basic"), "r") as rf:
  with open(os.path.join(path, "generifs_pairs"), "w") as wf:
   for line in rf:
    #time.sleep(0.4)
    if "	" in line:
     contents = line.split("	")
     try:
      download = fetch.article_by_pmid(contents[2])
      if download.abstract and download.title:
       wf.write(download.title + '-!!-' + download.abstract.replace('\n',' ')  + '-##-' + contents[4].split('[')[0] + '\n')
       print('Finish: ' + ' | Abs: ' + str(i) + ' pmid: ' + contents[2])
       i += 1  
     except:
      print('download fail for: ' + ' | Abs: ' + str(i) + ' pmid: ' + contents[2])
      i += 1

if __name__ == '__main__':
 preparing_pairs()
