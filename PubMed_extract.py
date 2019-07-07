import eutils
import pandas as pd
from metapub import PubMedFetcher
import time
fetch = PubMedFetcher()

df = pd.read_excel('Journals_PMID.xlsx', dtype=str)
with open('pmlist.txt' , 'w') as wrtf:
  for i, column in enumerate(df):
    pmids = df[column].tolist()
    for j, pmid in enumerate(pmids):
      if str(pmid) != 'nan':
        wrtf.write(str(pmid) + '\n')
        print ('Journal: ' + str(i) + ' | Abs: ' + str(j))



with open('abs.txt' , 'w') as wrtf:
  pmids = [line.rstrip('\n') for line in open('pmlist.txt')]
  print('Totaly: ' + str(len(pmids)) + ' papers')
  for j, pmid in enumerate(pmids):
      try:
        download = fetch.article_by_pmid(pmid)
        if download.abstract and download.journal and download.year:
          wrtf.write(download.journal + '-!!-' + str(download.year) + '-##-' + download.abstract + '\n')
          print (' | Abs: ' + str(j) + ' downloaded for: ' + pmid)
      except:
        print('download fail for: ' + ' | Abs: ' + str(j) + ' pmid: ' + pmid)
'''

df = pd.read_excel('Journals_PMID.xlsx', dtype=str)
with open('abs.txt' , 'w') as wrtf:
  for i, column in enumerate(df):
    pmids = df[column].tolist()
    for j, pmid in enumerate(pmids):
      if pmid:
        try:
          download = fetch.article_by_pmid(pmid)
          if download.abstract and download.journal and download.year:
            wrtf.write(download.journal + '-!!-' + str(download.year) + '-##-' + download.abstract + '\n')
            print ('Journal: ' + str(i) + ' | Abs: ' + str(j))
        except:
          print('download fail for: ' + str(pmid) + '||' + 'Journal: ' + str(i) + ' | Abs: ' + str(j))
'''


# get the first 1000 pmids matching "breast neoplasm" keyword search
#pmids = fetch.pmids_for_query('breast neoplasm', retmax=100)
#pmids = fetch.pmids_for_clinical_query('category'='therapy', 'scope'='broad', retmax=30)

#pmids_from_citation('year': 2017, 'volume':10,  'journal':'ENVIRONMENTAL HEALTH PERSPECTIVES')

# get abstract for each article:
'''
keywords = [line.rstrip('\n') for line in open('search_list.txt')]
with open('abs.txt' , 'w') as wrtf:
  for index, keyword in enumerate(keywords):
    pmids = fetch.pmids_for_query(keyword, retmax=300)
    for j, pmid in enumerate(pmids):
      try:
        download = fetch.article_by_pmid(pmid)
        #time.sleep(2)
        if download.abstract and download.journal and download.year:
          wrtf.write(download.journal + '-!!-' + str(download.year) + '-##-' + download.abstract + '\n')
          print ('Keyword:' + str(index) + ' | Abs: ' + str(j))
      except:
        print('download fail for: ' + str(pmid))

objs = {}
for pmid in pmids:
    download = fetch.article_by_pmid(pmid)
    objs['abs'] = download.abstract
    objs['jour'] = download.journal
    print('------------------------------')
    print (objs['abs'])

    print('!!!!This is journal name:   ' + objs['jour'])
'''
