import streamlit as st
import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# library untuk modul 1
import pandas as pd
from stanfordcorenlp import StanfordCoreNLP
from nltk.parse.corenlp import CoreNLPParser

#library untuk modul 2
import pandas as pd
import numpy as np
from pywsd.cosine import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn import metrics
from sklearn.metrics import confusion_matrix

stops = set(stopwords.words("english"))
lem = WordNetLemmatizer()

# -*- coding: utf-8 -*-
"""modul_partof_(ekspart)

Author Rakha Asyrofi / 0511195001038

Original file is located at
    https://colab.research.google.com/drive/1cRCUN0tsJGjcOOjI8igSOCKK9s8_h6eK
"""

class partOf: #template

  def __init__(self, inputData  = r'https://docs.google.com/spreadsheets/d/1Xkvdqfaxc_r0C0ipuJ3viGYfYj6Vd94H/edit?usp=sharing&ouid=114591885211797833190&rtpof=true&sd=true', 
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
      st.write('Processing: [{}] ...'.format(sh))
      st.write(df.head())

  # nltk stanford
  def parsing(self, data):
      parser = CoreNLPParser(url=self.stanford_url)
      next(parser.raw_parse(data)).pretty_print()

  # stanford library
  def stanfordConstituencyparsing(self, sentence):
      nlp = StanfordCoreNLP(self.dataTag)
      st.write(nlp.parse(sentence))
      nlp.close() # Do not forget to close! The backend server will consume a lot memery.
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
      st.write('Processing: [{}] ...'.format(sh))
      st.write(df.head())

  # cleaning text
  def apply_cleaning_function_to_list(self, X):
      cleaned_X = []
      for element in X:
          cleaned_X.append(wsd_partof.clean_text(self, raw_text= element))
      return cleaned_X

  def clean_text(self, raw_text):
      text = raw_text.lower()
      tokens = word_tokenize(text)
      token_words = [w for w in tokens if w.isalpha()]
      lemma_words = [lem.lemmatize(w) for w in token_words]
      meaningful_words = [w for w in lemma_words if not w in stops]
      joined_words = ( " ".join(meaningful_words))
      return joined_words    
      

if __name__ == "__main__":
    data_1 = st.sidebar.file_uploader("Choose a file", key= 'filePertama')
    if data_1 is not None:
        file1 = data_1
    data_2 = st.sidebar.file_uploader("Choose a file", key= 'fileKedua')
    if data_2 is not None:
        file2 = data_2
    data_3 = st.sidebar.file_uploader("Choose a file", key= 'fileKetiga')
    if data_3 is not None:
        file3 = data_3

        add_selectbox = st.sidebar.selectbox(
        'Pilih modul yang anda inginkan?',
        ('modul1', 'modul2'))
        if(add_selectbox == 'modul2'):
            """#modul 2: pencarian relasi melalui ukur wsd"""

            myWsd_partof = wsd_partof()
            # myWsd_partof.preprocessing(dataFile= r'../dataset_2_split.xlsx')

            # file1 = r'../dataset_2.xlsx'
            # file2 = r'../dataset_2_split.xlsx'
            # file3 = r'../wsd_groundtruth.xlsx'
            xl = pd.ExcelFile(file1)
            a = [sh for sh in xl.sheet_names]
            pilih_data = st.sidebar.selectbox(
            'Pilih file Test', a)
            xl2 = pd.ExcelFile(file3)
            b = [sh for sh in xl2.sheet_names]
            pilihan = st.sidebar.selectbox(
            'Pilih file Groundtruth', b)
            slider_value = st.sidebar.slider('Threhold', 0.2, 1.0, 0.3)


            dataSRS =  pilih_data

            a = myWsd_partof.fulldataset(dataFile= file1, inputSRS= dataSRS)
            list_req1 = list(a['Requirement Statement'])
            id_req1 = list(a['ID'])
            cleaned1 = myWsd_partof.apply_cleaning_function_to_list(X= list_req1)

            b = myWsd_partof.fulldataset(dataFile= file2, inputSRS= dataSRS)
            list_req2 = list(b['Requirement Statement'])
            id_req2 = list(b['ID'])
            cleaned2 = myWsd_partof.apply_cleaning_function_to_list(X= list_req2)

            hasil_wsd = []
            for num in cleaned1:
                text = [cosine_similarity(num, angka) for angka in cleaned2]
                hasil_wsd.append(text)

            data_raw = pd.DataFrame(hasil_wsd, index= id_req1, columns= id_req2)
            st.write("Hasil pengukuran semantik antar kebutuhan atomik dan non atomik {}".format(dataSRS))
            st.table(data_raw)

            # thresholding
            threshold = slider_value
            d = data_raw.values >= threshold
            d1 = pd.DataFrame(d, index= id_req1, columns= id_req2)
            mask = d1.isin([True])
            d2 = d1.where(mask, other= 0)
            mask2 = d1.isin([False])
            d3 = d2.where(mask2, other= 1)
            st.write("\nHasil ukur semantik diatas threshold {}".format(threshold))
            st.table(d3)


            dataGT =  pilihan
            # dataGT = 'grid3d_eval'
            b3 = myWsd_partof.fulldataset(dataFile= file3, inputSRS= dataGT)
            b3 = b3.drop(['Index'], axis= 1)
            b3.index= d3.index
            st.write("\nData Hasil Ground Truth {}".format(dataGT))
            st.table(b3)


            y_actual = d3.values.astype(int)
            y_predicted = b3.values.astype(int)
            st.write("akurasi", metrics.accuracy_score(y_true= y_actual, y_pred= y_predicted))
            st.write("presion", metrics.precision_score(y_true= y_actual, y_pred= y_predicted, average= 'macro'))
            st.write("recall", metrics.recall_score(y_true= y_actual, y_pred= y_predicted, average= 'macro'))
            st.write("metrics {}".format(metrics.classification_report(y_true= y_actual, y_pred= y_predicted)))

        elif(add_selectbox == 'modul1'):
            """#modul 1: parsing kebutuhan partOf"""
            myPartOf = partOf()    # myPartOf.preprocessing()
            hasil_srs = []

            xl = pd.ExcelFile(r'../dataset_2.xlsx')
            dt_sheet = [sh for sh in xl.sheet_names]
            pilih_data = st.sidebar.selectbox(
            'Pilih file', dt_sheet)

            # dataSRS = '2005 - Grid 3D'
            dataSRS = pilih_data
            a = myPartOf.fulldataset(dataSRS)
            for idx, num in zip(a['ID'], a['Requirement Statement']):
                data = [x8 for x in num.split("(i.e., black on white background)") 
                            for x1 in x.split(":\n") for x2 in x1.split("(") 
                            for x3 in x2.split(".)") for x4 in x3.split(")") 
                            for x5 in x4.split(".")for x6 in x5.split(", so")  
                            for x7 in x6.split(",") for x8 in x7.split("and") ]
                hasil_srs.append([idx, data])
            a_df = pd.DataFrame(hasil_srs, columns = ['ID', 'Data'])
            """## Dataset partOf"""
            st.write("data {}".format(dataSRS))
            st.table(a_df)

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

            st.write("data dari {}".format(hasil_srs[idx][0]))
            for xi in hasil_join.split(","): 
                st.write("\n{}".format(xi))
                # myPartOf.stanfordConstituencyparsing(xi) #drive parsing
                # myPartOf.parsing(xi) #online parsing
