# -*- coding: utf-8 -*-
"""modul_partof_(ekspart).ipynb

Author Rakha Asyrofi / 0511195001038

Original file is located at
    https://colab.research.google.com/drive/1cRCUN0tsJGjcOOjI8igSOCKK9s8_h6eK
"""

"""#modul 1: parsing kebutuhan partOf"""

# function
import pandas as pd
from tabulate import tabulate
from stanfordcorenlp import StanfordCoreNLP
from nltk.parse.corenlp import CoreNLPParser

class partOf: #template

  def __init__(self, inputData  = r'data/dataset_2.xlsx', 
               dataStanford     = r'https://drive.google.com/drive/folders/1_CdTdX8H-HWcqkN5_6Q-AFd_KH2Rk11P?usp=sharing',
               urlStanford      = 'http://corenlp.run/'):
    self.data         = inputData
    self.dataTag      = dataStanford
    self.stanford_url = urlStanford

  def fulldataset(self, inputSRS):
    xl = pd.ExcelFile(self.data)
    dfs = {sh:xl.parse(sh) for sh in xl.sheet_names}
    kalimat = dfs[inputSRS]
    kalimat_semua = kalimat.head(len(kalimat))
    return kalimat_semua

  def preprocessing(self):
    xl = pd.ExcelFile(self.data)
    for sh in xl.sheet_names:
      df = xl.parse(sh)
      print('Processing: [{}] ...'.format(sh))
      print(df.head())

  # nltk stanford
  def parsing(self, data):
      parser = CoreNLPParser(url=self.stanford_url)
      next(parser.raw_parse(data)).pretty_print()

  # stanford library
  def stanfordConstituencyparsing(self, sentence):
      nlp = StanfordCoreNLP(self.dataTag)
      print (nlp.parse(sentence))
      nlp.close() # Do not forget to close! The backend server will consume a lot memery.

if __name__ == "__main__":
  try:
    myPartOf = partOf()    # myPartOf.preprocessing()
    hasil_srs = []
    dataSRS = '2005 - Grid 3D'
    a = myPartOf.fulldataset(dataSRS)
    for idx, num in zip(a['ID'], a['Requirement Statement']):
        data = [x8 for x in num.split("(i.e., black on white background)") 
                    for x1 in x.split(":\n") for x2 in x1.split("(") 
                    for x3 in x2.split(".)") for x4 in x3.split(")") 
                    for x5 in x4.split(".")for x6 in x5.split(", so")  
                    for x7 in x6.split(",") for x8 in x7.split("and") ]
        hasil_srs.append([idx, data])
    a_df = pd.DataFrame(hasil_srs, columns = ['ID', 'Data'])
    print("data {}".format(dataSRS))
    print(tabulate(a_df, headers = 'keys', tablefmt = 'psql'))

    # detailing
    idx = 7
    idy = 1
    hasil_split = hasil_srs[idx][idy]
    x = hasil_split[3].replace("move", "")
    hasil_splita = hasil_split[1] + x
    hasil_splitb = hasil_split[2] + x
    hasil_splitc = hasil_split[3]
    myTuple = [hasil_split[0], hasil_splita, hasil_splitb, hasil_splitc]
    hasil_join = ",".join(myTuple)

    print("data dari {}".format(hasil_srs[idx][0]))
    for xi in hasil_join.split(","): 
      print("\n{}".format(xi))
      # myPartOf.stanfordConstituencyparsing(xi) #drive parsing
      myPartOf.parsing(xi) #online parsing

  except OSError as err:
    print("OS error: {0}".format(err))

