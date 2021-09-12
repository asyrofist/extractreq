# -*- coding: utf-8 -*-
"""modul_relasi.ipynb
Author Rakha Asyrofi / 05111950010038

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h6HKNeALV8bXjrxWB0Jn0ztHtLv2cXz8
"""

"""# Modul3: pencarian relasi"""

# !pip install -U pywsd
# !pip install -U wn==0.0.23

from os import name
import pandas as pd
from nltk.tokenize import word_tokenize 
from pywsd import disambiguate
from pywsd.cosine import cosine_similarity
from tabulate import tabulate

# template class ucdReq
class ucdReq:

  #inicsialisasi
  def __init__(self, data_aksi_aktor, tabel_usecase):
    self.aksi_aktor = data_aksi_aktor
    self.dt_usecase = tabel_usecase

  def fulldataset(self, inputData):
      xl = pd.ExcelFile(self.aksi_aktor)
      dfs = {sh:xl.parse(sh) for sh in xl.sheet_names}
      kalimat = dfs[inputData]
      kalimat_semua = kalimat.head(len(kalimat))
      return kalimat_semua

  def fulldataset_xmi(self, inputXMI):
      xl = pd.ExcelFile(self.dt_usecase)
      dfs = {sh:xl.parse(sh) for sh in xl.sheet_names}
      kalimat = dfs[inputXMI]
      kalimat_semua = kalimat.head(len(kalimat))
      return kalimat_semua

  def preprocessing(self):
    xl = pd.ExcelFile(self.aksi_aktor)
    for sh in xl.sheet_names:
      df = xl.parse(sh)
      print('Processing: [{}] ...'.format(sh))
      print(df.head())

  def useCaseWSDStopwords(self, keyword, id_keyword):
    word_stopwords = [disambiguate(x) for x in keyword]
    b = [len(word_tokenize(num)) for num in keyword]
    c = max(b)
    list_kolom = ["data{}".format(x) for x in range(0,c)]
    word_synset_stopwords = [[n[1] for n in y] for y in word_stopwords]
    hasilUcd_stopwords = pd.DataFrame(word_synset_stopwords, index= id_keyword, columns= list_kolom)
    return hasilUcd_stopwords

  #PengukuranUCD
  def useCaseMeasurement(self, keyword1, keyword2, id1, id2):
    hasil_wsd = []
    for num in keyword1:
      text = [cosine_similarity(num, angka) for angka in keyword2]
      hasil_wsd.append(text)
    df = pd.DataFrame(hasil_wsd, index= id1, columns= id2)
    return df

  def change_case(self, word):
      return ''.join([' '+i.lower() if i.isupper()
          else i for i in word]).lstrip(' ')


  def __del__(self):
    print ('Destructor called.')

if __name__ == "__main__":
  try:
      # data dari txt
      MyucdReq = ucdReq(data_aksi_aktor= r'data_aksi_aktor.xlsx', tabel_usecase= r'data_xmi.xlsx')
      tabel_freq =  'tabel_freqs'
      freqs = MyucdReq.fulldataset(inputData= tabel_freq)
      tabel_ucd1 =  'tabel_ucd1'
      ucd1 = MyucdReq.fulldataset(inputData= tabel_ucd1)
      tabel_ucd2 =  'tabel_ucd2'
      ucd2 = MyucdReq.fulldataset(inputData= tabel_ucd2)

      tbl_1 = MyucdReq.useCaseMeasurement(keyword1= freqs.aksi, keyword2=ucd1.aksi , id1= freqs.id, id2= ucd1.usecase)
      tbl_1.rename(columns = {'insertMetadata':'UC01', 'searchArticle':'UC03', 'viewNextResult':'UC04'}, inplace = True)
      print("\nData Pengukuran antara functional dan ucd1")
      print(tabulate(tbl_1, headers = 'keys', tablefmt = 'psql'))

      ucd2= ucd2.dropna()
      tbl_2 = MyucdReq.useCaseMeasurement(keyword1= freqs.aksi, keyword2=ucd2.aksi , id1= freqs.id, id2= ucd2.usecase)
      tbl_2.rename(columns = {'searchResearcher':'UC02', 'orderByRelevancy':'UC05', 'orderByScore':'UC06', 
                              'viewDetailResearcher':'UC07', 'removeArticle':'UC09', 'editProfile':'UC08' }, inplace = True)
      print("\nData Pengukuran antara functional dan ucd2")
      print(tabulate(tbl_2, headers = 'keys', tablefmt = 'psql'))

      tbl_3 = pd.concat([tbl_1, tbl_2], axis= 1)
      print("\nData Pengukuran Gabungan")
      print(tabulate(tbl_3, headers = 'keys', tablefmt = 'psql'))

      tbl_3['uc01'] = tbl_3.UC01.values.max(1)
      tbl_3['uc02'] = tbl_3.UC02.values.max(1)
      tbl_3['uc03'] = tbl_3.UC03.values.max(1)
      tbl_3['uc04'] = tbl_3.UC04.values.max(1)
      tbl_3['uc05'] = tbl_3.UC05.values.max(1)
      tbl_3['uc06'] = tbl_3.UC06.values.max(1)
      tbl_3['uc07'] = tbl_3.UC07.values.max(1)
      tbl_3['uc08'] = tbl_3.UC08.values.max(1)
      tbl_3['uc09'] = tbl_3.UC09.values.max(1)
      df_filter = tbl_3.drop(['UC01','UC02', 'UC03', 'UC04', 'UC05', 'UC06', 'UC07', 'UC08', 'UC09'], axis= 1)
      print("\nData filter maksmimum")
      print(tabulate(df_filter, headers = 'keys', tablefmt = 'psql'))

      threshold = 0.3
      d = df_filter.values >= threshold
      d1 = pd.DataFrame(d, index= df_filter.index, columns= df_filter.columns)
      mask = d1.isin([True])
      d2 = d1.where(mask, other= 0)
      mask2 = d1.isin([False])
      d3 = d2.where(mask2, other= "1")
      tbl_4 = d3
      print("\nData hasil relasi antara kebutuhan dan kasus penggunaan")
      print(tabulate(tbl_4, headers = 'keys', tablefmt = 'psql'))

      # data dari xmi
      namaUsecase =  'tabel_usecase'
      useCaseTable  = MyucdReq.fulldataset_xmi(inputXMI= namaUsecase)
      data_ucd = []
      for num in useCaseTable.name:
        data_ucd.append(MyucdReq.change_case(num))
      tbl_1x = MyucdReq.useCaseMeasurement(keyword1= freqs.aksi, keyword2=data_ucd , id1= freqs.id, id2= useCaseTable.name)
      tbl_1x.rename(columns = {'insertMetadata':'uc01', 'searchArticle':'uc03', 'viewNextResult':'uc04', 
                               'searchResearcher':'uc02', 'orderByRelevancy':'uc05', 'orderByScore':'uc06', 
                              'viewDetailOfResearcher':'uc07', 'removeArticle':'uc09', 'editProfile':'uc08' }, inplace = True)
      print("\nData hasil relasi antara kebutuhan dan kasus penggunaan (xmi)")
      print(tabulate(tbl_1x, headers = 'keys', tablefmt = 'psql'))

      threshold_kedua = 0.6
      dt = tbl_1x.values >= threshold_kedua
      dt1 = pd.DataFrame(dt, index= tbl_1x.index, columns= tbl_1x.columns)
      mask = dt1.isin([True])
      dt2 = dt1.where(mask, other= 0)
      mask2 = dt2.isin([False])
      tbl_5 = dt2.where(mask2, other= 1)
      print("\nData hasil relasi antara kebutuhan dan kasus penggunaan (xmi)")
      print(tabulate(tbl_5, headers = 'keys', tablefmt = 'psql'))

      list_usecase = ['uc01', 'uc02', 'uc03', 'uc04', 'uc05', 'uc06', 'uc07', 'uc08', 'uc09']
      # tbl_6 = tbl_4.merge(tbl_5, how= 'inner', left_index= True, right_index= True, on= list_usecase)
      tbl_6 = tbl_4.merge(tbl_5, how= 'inner', left_index= True, right_index= True)
      print("\nData hasil join relasi antara kebutuhan dan kasus penggunaan (txt dan xmi)")
      print(tabulate(tbl_6, headers = 'keys', tablefmt = 'psql'))

      MyucdReq.__del__()

  except OSError as err:
      print("OS error: {0}".format(err))