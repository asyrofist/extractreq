__copyright__ = "Copyright (c) 2021"
__author__ = "Rakha Asyrofi"
__date__ = "2021-10-08:18:07:39"

#@title Modul: spacySent { vertical-output: true }
spacy_param = 'en_core_web_sm' #@param {type:"string"}
dataFile = "/content/drive/MyDrive/dataset/dataset_2.xlsx" #@param {type:"string"}
srs_param = "2005 - Grid 3D" #@param ["0000 - cctns", "0000 - gamma j", "0000 - Inventory", "1998 - themas", "1999 - dii", "1999 - multi-mahjong", "1999 - tcs", "2000 - nasa x38", "2001 - ctc network", "2001 - esa", "2001 - hats", "2001 -libra", "2001 - npac", "2001 - space fractions", "2002 - evia back", "2002 - evia corr", "2003 - agentmom", "2003 - pnnl", "2003 - qheadache", "2003 - Tachonet", "2004 - colorcast", "2004 - eprocurement", "2004 - grid bgc", "2004 - ijis", "2004 - Phillip", "2004 - rlcs", "2004 - sprat", "2005 - clarus high", "2005 - clarus low", "2005 - Grid 3D", "2005 - nenios", "2005 - phin", "2005 - pontis", "2005 - triangle", "2005 - znix", "2006 - stewards", "2007 - ertms", "2007 - estore", "2007 - nde", "2007 - get real 0.2", "2007 - mdot", "2007 - nlm", "2007 - puget sound", "2007 - water use", "2008 - caiso", "2008 - keepass", "2008 - peering", "2008 - viper", "2008 - virtual ed", "2008 - vub", "2009 - email", "2009 - gaia", "2009 - inventory 2.0", "2009 - library", "2009 - library2", "2009 - peazip", "2009 - video search", "2009 - warc III", "2010 - blit draft", "2010 - fishing", "2010 - gparted", "2010 - home", "2010 - mashboot", "2010 - split merge"]

# dataFile = "/content/drive/MyDrive/dataset/visualPartOf/partOf2005 - Grid 3D.xlsx" #@param {type:"string"}
# srs_param = "tabel_partOf" #@param {type:"string"}
col_param = "Requirement Statement" #@param ["Requirement Statement", "req"]
id_param = "ID" #@param ["ID"]

import pandas as pd, spacy
from tabulate import tabulate

class spacyClause:
  def __init__(self, fileName= dataFile):
      """ parameter inisialisasi, data yang digunakan pertama kali 
      untuk contruct data
      """
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

  def find_root_of_sentence(self, doc):
      root_token = None
      for token in doc:
          if (token.dep_ == "ROOT"):
              root_token = token
      return root_token

  def find_other_verbs(self, doc, root_token):
      other_verbs = []
      for token in doc:
          ancestors = list(token.ancestors)
          if (token.pos_ == "VERB" and len(ancestors) == 1\
              and ancestors[0] == root_token):
              other_verbs.append(token)
      return other_verbs    

  def get_clause_token_span_for_verb(self, verb, doc, all_verbs):
      first_token_index = len(doc)
      last_token_index = 0
      this_verb_children = list(verb.children)
      for child in this_verb_children:
          if (child not in all_verbs):
              if (child.i < first_token_index):
                  first_token_index = child.i
              if (child.i > last_token_index):
                  last_token_index = child.i
      return first_token_index, last_token_index

  def extractData(self, doc):
      root_token = spacyClause.find_root_of_sentence(self, doc)
      other_verbs = spacyClause.find_other_verbs(self, doc, root_token)
      all_verbs = [root_token] + other_verbs
      token_spans = [spacyClause.get_clause_token_span_for_verb(self, other_verb, doc, all_verbs) for other_verb in all_verbs]   
      sentence_clauses = [doc[token_span[0]:token_span[1]] for token_span in token_spans if (token_span[0] < token_span[1])]
      sentence_clauses = sorted(sentence_clauses, key=lambda tup: tup[0])    
      clauses_text = [clause.text for clause in sentence_clauses]
      return clauses_text  

  def main(self, srs_param, id_param, col_param):
      id_req = spacyClause.fulldataset(self, srs_param)[id_param]
      req = spacyClause.fulldataset(self, srs_param)[col_param]
      dataSpacy = []
      nlp = spacy.load(spacy_param)
      for id, num in zip(id_req, req):
          doc = nlp(num)
          myClause = spacyClause.extractData(self, doc)
          jml_clausa = len(myClause)
          label_df = []
          if jml_clausa > 1: # non atomik berdasarkan jumlah
               label_df.append('non_atomik')
          elif jml_clausa == 1:
               label_df.append('atomik')
          else:
               label_df.append('unknown')
          dataSpacy.append([id, num, myClause, label_df[0], jml_clausa])
      spacy_df = pd.DataFrame(dataSpacy, columns = ['ID', 'req', 'data', 'label', 'jumlah'])
      return spacy_df

if __name__ == "__main__":
  try:
    dataSpacy = spacyClause(dataFile).main(srs_param, id_param, col_param)
    print(tabulate(dataSpacy, headers = 'keys', tablefmt = 'psql'))

  except OSError as err:
    print("OS error: {0}".format(err))