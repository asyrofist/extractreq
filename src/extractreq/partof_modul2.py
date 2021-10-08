__copyright__ = "Copyright (c) 2021"
__author__ = "Rakha Asyrofi"
__date__ = "2021-10-08:18:07:39"

import pandas as pd
import numpy as np
from tabulate import tabulate
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer
from pywsd.cosine import cosine_similarity
from sklearn import metrics
from sklearn.metrics import confusion_matrix

class wsd_partof:
  def __init__(self):
      pass

  def fulldataset(self, dataFile, inputSRS):
      xl = pd.ExcelFile(dataFile)
      dfs = {sh:xl.parse(sh) for sh in xl.sheet_names}
      kalimat = dfs[inputSRS]
      kalimat_semua = kalimat.head(len(kalimat))
      return kalimat_semua

  def preprocessing(self, dataFile):
    xl = pd.ExcelFile(dataFile)
    for sh in xl.sheet_names:
      df = xl.parse(sh)
      print('Processing: [{}] ...'.format(sh))
      print(df.head())

  # cleaning text
  def apply_cleaning_function_to_list(self, X):
      cleaned_X = []
      for element in X:
          cleaned_X.append(wsd_partof.clean_text(self, raw_text= element))
      return cleaned_X

  def clean_text(self, raw_text):
      nlp = English()
      tokenizer = Tokenizer(nlp.vocab)    
      tokens = tokenizer(raw_text)
      lemma_list = [token.lemma_.lower() for token in tokens if token.is_stop is False and token.is_punct is False and token.is_alpha is True]
      joined_words = ( " ".join(lemma_list))
      return joined_words  

  # thresholding
  def threshold_value(self, data, th, index1, index2):
      d = data.values >= th
      d1 = pd.DataFrame(d, index= index1, columns= index2)
      mask = d1.isin([True])
      d2 = d1.where(mask, other= 0)
      mask2 = d1.isin([False])
      d3 = d2.where(mask2, other= 1)
      return d3

if __name__ == "__main__":
  try:
      myWsd_partof = wsd_partof()
      a = myWsd_partof.fulldataset(dataFile, inputSRS)
      list_req1 = list(a['Requirement Statement'])
      id_req1 = list(a['ID'])
      cleaned1 = myWsd_partof.apply_cleaning_function_to_list(X= list_req1)

      b = myWsd_partof.fulldataset(dataFile, inputSRS)
      list_req2 = list(b['Requirement Statement'])
      id_req2 = list(b['ID'])
      cleaned2 = myWsd_partof.apply_cleaning_function_to_list(X= list_req2)

      hasil_wsd = []
      for num in cleaned1:
        text = [cosine_similarity(num, angka) for angka in cleaned2]
        hasil_wsd.append(text)

      data_raw = pd.DataFrame(hasil_wsd, index= id_req1, columns= id_req2)
      print("Hasil pengukuran semantik antar kebutuhan atomik dan non atomik {}".format(dataSRS))
      print(tabulate(data_raw, headers = 'keys', tablefmt = 'psql'))   

      # thresholding
      data_threshold = myWsd_partof.threshold_value(data_raw, th, id_req1, id_req2)
      print("\nHasil ukur semantik diatas threshold {}".format(th))
      print(tabulate(data_threshold, headers = 'keys', tablefmt = 'psql'))   

      b3 = myWsd_partof.fulldataset(dataFile, inputSRS)
      b3 = b3.drop(['Index'], axis= 1)
      b3.index= data_threshold.index
      print("\nData Hasil Ground Truth {}".format(dataGT))
      print(tabulate(b3, headers = 'keys', tablefmt = 'psql'))  

      y_actual = data_threshold.values.astype(int)
      y_predicted = b3.values.astype(int)
      print("akurasi", metrics.accuracy_score(y_true= y_actual, y_pred= y_predicted))
      print("presion", metrics.precision_score(y_true= y_actual, y_pred= y_predicted, average= 'macro'))
      print("recall", metrics.recall_score(y_true= y_actual, y_pred= y_predicted, average= 'macro'))
      print("metrics {}".format(metrics.classification_report(y_true= y_actual, y_pred= y_predicted)))       

  except OSError as err:
    print("OS error: {0}".format(err))
