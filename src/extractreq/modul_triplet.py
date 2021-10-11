__copyright__ = "Copyright (c) 2021"
__author__ = "Rakha Asyrofi"
__date__ = "2021-10-08:18:07:39"

#@title Modul2c: Triplet NLTK-Stanford Triplet Parameter { vertical-output: true }
url_param = "http://corenlp.run/" #@param {type:"string"}
dataFile = "/content/drive/MyDrive/dataset/dataset_2.xlsx" #@param {type:"string"}
srs_param = "2003 - Tachonet" #@param ["0000 - cctns", "0000 - gamma j", "0000 - Inventory", "1998 - themas", "1999 - dii", "1999 - multi-mahjong", "1999 - tcs", "2000 - nasa x38", "2001 - ctc network", "2001 - esa", "2001 - hats", "2001 -libra", "2001 - npac", "2001 - space fractions", "2002 - evia back", "2002 - evia corr", "2003 - agentmom", "2003 - pnnl", "2003 - qheadache", "2003 - Tachonet", "2004 - colorcast", "2004 - eprocurement", "2004 - grid bgc", "2004 - ijis", "2004 - Phillip", "2004 - rlcs", "2004 - sprat", "2005 - clarus high", "2005 - clarus low", "2005 - Grid 3D", "2005 - nenios", "2005 - phin", "2005 - pontis", "2005 - triangle", "2005 - znix", "2006 - stewards", "2007 - ertms", "2007 - estore", "2007 - nde", "2007 - get real 0.2", "2007 - mdot", "2007 - nlm", "2007 - puget sound", "2007 - water use", "2008 - caiso", "2008 - keepass", "2008 - peering", "2008 - viper", "2008 - virtual ed", "2008 - vub", "2009 - email", "2009 - gaia", "2009 - inventory 2.0", "2009 - library", "2009 - library2", "2009 - peazip", "2009 - video search", "2009 - warc III", "2010 - blit draft", "2010 - fishing", "2010 - gparted", "2010 - home", "2010 - mashboot", "2010 - split merge"]
id_param = "ID" #@param ["ID"]
col_param = "Requirement Statement" #@param ["Requirement Statement", "req"]
mode_param = "parse_tree" #@param ["parse_tree", "spo", "result"]

import nltk, pandas as pd, numpy as np
from nltk.tag.stanford import CoreNLPPOSTagger
from nltk.tree import ParentedTree
from tabulate import tabulate

class extractNlp:
  def __init__(self, coreUrl = url_param, fileName= dataFile):
      self.__pos_tagger = CoreNLPPOSTagger(url= coreUrl)
      self.__data = fileName

  def fulldataset(self, inputSRS): # function membuat dataset
      """ fungsi ini digunakan untuk menentukand dataset yang digunakan
      berdasarkan indeks srs yang dipilih, maka dari itu hal ini penting untuk
      menyiapkan data selanjutnya.
      partOf().fulldataset(inputSRS)
      """
      xl = pd.ExcelFile(self.__data)
      dfs = {sh:xl.parse(sh) for sh in xl.sheet_names}[inputSRS]
      return dfs

  def preprocessing(self): # function melihat struktur dataset di excel
      """ fungsi ini digunakan untuk preprocessing untuk melihat dataset excel yang digunakan
      fungsi ini dapat melihat struktur dataset yang diuji, sebab memperlihatkan
      data excel beseerta tab yang digunakan.
      partOf().preprocssing()
      """
      xl = pd.ExcelFile(self.__data)
      for sh in xl.sheet_names:
        df = xl.parse(sh)
        print('Processing: [{}] ...'.format(sh))
        print(df.head())

  def triplet_extraction (self, input_sent, output=['parse_tree','spo','result']):
      parse_tree, = ParentedTree.convert(list(self.__pos_tagger.parse(input_sent.split()))[0])

      # Extract subject, predicate and object
      subject = extractNlp.extract_subject(self, parse_tree)
      predicate = extractNlp.extract_predicate(self, parse_tree)
      objects = extractNlp.extract_object(self, parse_tree)
      if 'parse_tree' in output:
          print('---Parse Tree---')
          parse_tree.pretty_print()
      elif 'spo' in output:
          return ("subject:\t{}\npredicate:\t{}\nobject:\t{}".format(subject, predicate, objects))
      elif 'result' in output:
          return (' '.join([subject[0], predicate[0], objects[0]]))

  def extract_subject (self, parse_tree):
      # Extract the first noun found in NP_subtree
      subject = []
      for s in parse_tree.subtrees(lambda x: x.label() == 'NP'):
          for t in s.subtrees(lambda y: y.label().startswith('NN')):
              output = [t[0], extractNlp.extract_attr(self, t)]
              # Avoid empty or repeated values
              if output != [] and output not in subject:
                  subject.append(output) 
      if len(subject) != 0: return subject[0] 
      else: return ['']

  def extract_predicate (self, parse_tree):
      # Extract the deepest(last) verb foybd ub VP_subtree
      output, predicate = [],[]
      for s in parse_tree.subtrees(lambda x: x.label() == 'VP'):
          for t in s.subtrees(lambda y: y.label().startswith('VB')):
              output = [t[0], extractNlp.extract_attr(self, t)]
              if output != [] and output not in predicate:    
                  predicate.append(output)
      if len(predicate) != 0: return predicate[-1]
      else: return ['']

  def extract_object (self, parse_tree):
      # Extract the first noun or first adjective in NP, PP, ADP siblings of VP_subtree
      objects, output, word = [],[],[]
      for s in parse_tree.subtrees(lambda x: x.label() == 'VP'):
          for t in s.subtrees(lambda y: y.label() in ['NP','PP','ADP']):
              if t.label() in ['NP','PP']:
                  for u in t.subtrees(lambda z: z.label().startswith('NN')):
                      word = u          
              else:
                  for u in t.subtrees(lambda z: z.label().startswith('JJ')):
                      word = u
              if len(word) != 0:
                  output = [word[0], extractNlp.extract_attr(self, word)]
              if output != [] and output not in objects:
                  objects.append(output)
      if len(objects) != 0: return objects[0]
      else: return ['']

  def extract_attr (self, word):
      attrs = []     
      # Search among the word's siblings
      if word.label().startswith('JJ'):
          for p in word.parent(): 
              if p.label() == 'RB':
                  attrs.append(p[0])
      elif word.label().startswith('NN'):
          for p in word.parent():
              if p.label() in ['DT','PRP$','POS','JJ','CD','ADJP','QP','NP']:
                  attrs.append(p[0])
      elif word.label().startswith('VB'):
          for p in word.parent():
              if p.label() == 'ADVP':
                  attrs.append(p[0])
      # Search among the word's uncles
      if word.label().startswith('NN') or word.label().startswith('JJ'):
          for p in word.parent().parent():
              if p.label() == 'PP' and p != word.parent():
                  attrs.append(' '.join(p.flatten()))
      elif word.label().startswith('VB'):
          for p in word.parent().parent():
              if p.label().startswith('VB') and p != word.parent():
                  attrs.append(' '.join(p.flatten()))
      return attrs
  
  def __del__(self):
      print("destructed")

  def main(self, srs_param, id_param, col_param, output= mode_param):
      id_req = extractNlp.fulldataset(self, srs_param)[id_param]
      data_num = extractNlp.fulldataset(self, srs_param)[col_param]
      data_triplet = [extractNlp.triplet_extraction(self, num, output) 
                      for num in extractNlp.fulldataset(self, srs_param)[col_param]]
      triplet_df = pd.DataFrame([data_num, data_triplet], index= ['origin', 'triplet'], columns= id_req).T
      extractNlp.__del__(self)
      return triplet_df

if __name__ == "__main__":
  try:
    triplet_data = extractNlp(dataFile).main(srs_param, id_param, col_param, mode_param)
    print(tabulate(triplet_data, headers = 'keys', tablefmt = 'psql'))

  except OSError as err:
    print("OS error: {0}".format(err))