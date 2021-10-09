__copyright__ = "Copyright (c) 2021"
__author__ = "Rakha Asyrofi"
__date__ = "2021-10-08:18:07:39"

#@title Modul1: Ekstraksi Kebutuhan partOf { vertical-output: true }
url_param = "http://corenlp.run" #@param {type:"string"}
model_param = "/content/drive/MyDrive/stanford-corenlp-4.0.0" #@param {type:"string"}
spacy_param = "en_core_web_sm" #@param {type:"string"}
file_param = "/content/drive/MyDrive/dataset/dataset_2.xlsx" #@param {type:"string"}
dataFile = "/content/drive/MyDrive/dataset/dataset_2.xlsx" #@param {type:"string"}
grd_param = "/content/drive/MyDrive/dataset/dataset_2_split.xlsx" #@param {type:"string"}
save_param = "/content/drive/MyDrive/dataset/partOfAll/" #@param {type:"string"}
srs_param = "2005 - Grid 3D" #@param ["0000 - cctns", "0000 - gamma j", "0000 - Inventory", "1998 - themas", "1999 - dii", "1999 - multi-mahjong", "1999 - tcs", "2000 - nasa x38", "2001 - ctc network", "2001 - esa", "2001 - hats", "2001 -libra", "2001 - npac", "2001 - space fractions", "2002 - evia back", "2002 - evia corr", "2003 - agentmom", "2003 - pnnl", "2003 - qheadache", "2003 - Tachonet", "2004 - colorcast", "2004 - eprocurement", "2004 - grid bgc", "2004 - ijis", "2004 - Phillip", "2004 - rlcs", "2004 - sprat", "2005 - clarus high", "2005 - clarus low", "2005 - Grid 3D", "2005 - nenios", "2005 - phin", "2005 - pontis", "2005 - triangle", "2005 - znix", "2006 - stewards", "2007 - ertms", "2007 - estore", "2007 - nde", "2007 - get real 0.2", "2007 - mdot", "2007 - nlm", "2007 - puget sound", "2007 - water use", "2008 - caiso", "2008 - keepass", "2008 - peering", "2008 - viper", "2008 - virtual ed", "2008 - vub", "2009 - email", "2009 - gaia", "2009 - inventory 2.0", "2009 - library", "2009 - library2", "2009 - peazip", "2009 - video search", "2009 - warc III", "2010 - blit draft", "2010 - fishing", "2010 - gparted", "2010 - home", "2010 - mashboot", "2010 - split merge"]

data_simpan = save_param +"partOf{}".format(srs_param)
tab_param = "pertama" #@param ['pertama', 'kedua', 'ketiga', 'alternatif', 'stat']
mode_data = "manual" #@param ["manual", "stanford", "spacy", 'clausy']
col_param = "Requirement Statement"

# library yang digunakan 
import graphviz as gf, pandas as pd, xlsxwriter, re, spacy
from tabulate import tabulate
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report

class partOf: #template class partOf

  def __init__(self, inputData  = file_param): 
      """ parameter inisialisasi, data yang digunakan pertama kali 
      untuk contruct data
      """
      self.__data = inputData # data inisiliasi file parameter

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

  def visualisasiGraph(self, source_data, part_data, srs_param):
      """ fungsi ini digunakan untuk memvisualisasikan dalam bentuk graf.
      data diambil berdasarkan referensi dari source data untuk parent node.
      part_data untuk node child, dan indeks yang digunakan sesuai data srs yang digunakan
      partOf().visualisasiGraph(source_data, part_data, srs_param)
      """
      f = gf.Digraph('finite_state_machine', filename='partOf.gv', 
                       engine= 'neato')
      f.attr(rankdir='LR', size='8,5')

      f.attr('node', shape='doublecircle') # node
      for angka in source_data.ID:
          f.node(angka)
      f.attr(kw= 'node', shape='circle') # edge
      for idx, num in zip(part_data.label, part_data.ID):
          f.edge(idx, num, label='partOf')

      f.attr(overlap='false')
      f.attr(label=r'Visulasisasi relasi partOf {}\n'.format(srs_param))
      f.attr(fontsize='20')
      f.view(data_simpan)
      print("Gambar disimpan ke {}".format(data_simpan))
      return f

  def evaluasi_data(self, data1, data2):
      """ fungsi ini digunakan untuk mengevaluasi data. nilai evaluasi meliputi
      nilai akurasi, recall, presisi dengan mengubah datanya menjadi int terlebih dahulu.
      cara menggunakan syntax ini yaitu melalui
      partOf().evaluasi_data(data1, data2)
      """
      y_actual = data1.values.astype(int) #define array of actual values
      y_predicted = data2.values.astype(int) #define array of predicted values
      nilai_akurasi = accuracy_score(y_actual, y_predicted, normalize=True)
      nilai_recall = recall_score(y_actual, y_predicted, average= 'macro')
      nilai_presisi = precision_score(y_actual, y_predicted, average= 'macro')
      print("akurasi {}\n recall {}\n presisi {}\n".format(nilai_akurasi, nilai_recall, nilai_presisi))
      print(classification_report(y_actual, y_predicted))

  def simpan_excel(self, data1, data2, data3, data4):
      """ fungsi ini digunakan untuk menyimpanda data. data yang digunakan meliputi
      tabel kebutuhan, partOf, relasi, dan nilai data secara statistik.
      cara menggunakan syntax ini yaitu melalui
      partOf().simpan_excel(data1, data2, data3, data4)
      """
      dfs  = { # save file
                'tabel_kebutuhan' : data1, 
                'tabel_partOf' : data2,
                'tabel_relasi' : data3,
                'tabel_statistika' : data4,
              } 
      writer = pd.ExcelWriter(data_simpan+ '.xlsx')
      for name,dataframe in dfs.items():
          dataframe.to_excel(writer,name,index=False)
      writer.save()
      print("data excel disimpan di {}".format(data_simpan+ '.xlsx'))

  # def tabulasi_filter(self, data, mode_data= ['manual', 'triplet']): # tabulasi_filter
  def tabulasi_filter(self, data): # tabulasi_filter
      """ fungsi ini digunakan untuk memfilter data berdasarkan mode yang digunakan.
      mode ini terdiri atas 4 macam mode yaitu manual, triplet, spacy, dan stanford.
      sesuai dengan namanya. maka fungsi ini menunjukkan hasil berbeda sesuai dengan fungsinya.
      cara menggunakan syntax ini yaitu melalui
      partOf().tabulasi_filter(hasil_req)
      """
      hasil_srs = []
      for idx, num in zip(data['ID'], data['Requirement Statement'].fillna("empty")):
          data = [x10 for x1 in num.split(".") for x2 in x1.split(" that ")  
                      for x3 in x2.split("/") for x4 in x3.split(" so ")  
                      for x5 in x4.split(",") for x6 in x5.split(" and ")
                      for x7 in x6.split(" i.e.") for x8 in x7.split(" or ")
                      for x9 in x8.split(" if ")  for x10 in x9.split(" ; ")]

          conv = lambda i : i or None
          res = [conv(i) for i in data]
          hasil_srs.append([idx, res])
      a_df = pd.DataFrame(hasil_srs, columns = ['ID', 'data'])
      return a_df

  def tabulasi_pertama(self, data, dataReq): # tabulasi_pertama
      """ fungsi ini digunakan untuk mengubah data tabulasi filter menjadi
      data atomik dan non atomik, dari banyak kalimat yang digunakan.
      jika terdiri atas satu kalimat maka disebut sebagai atomik. 
      namun sebaliknya jika lebih dari satu kalimat maka disebut non atomik. 
      partOf().tabulasi_pertama(hasil_filter, hasil_req)
      """
      c_df = data.copy()
      data_df = pd.DataFrame([sh for sh in c_df.data], index= dataReq.ID)
      list_column = ["data{}".format(num) for num in range(data_df.columns.stop)]
      data_df.columns = list_column

      b_df = []
      b_df_jumlah = []
      for num in c_df.data: # menentukan data atomik dan 
        if len(num) > 1: # non atomik berdasarkan jumlah
          b_df.append('non_atomik')
          b_df_jumlah.append(len(num))
        elif len(num) == 1:
          b_df.append('atomik')
          b_df_jumlah.append(len(num))
      c_df['label'] = b_df
      c_df['jumlah'] = b_df_jumlah
      return c_df

  def tabulasi_kedua(self, data): # tabulasi kedua
      """ fungsi ini digunakan untuk mengubah data tabulasi pertama menjadi
      dari non atomik menjadi p#, sehingga hasilnya cukup detail menunjukkan 
      setiap non atomik memiliki kebergantungan partOf didalamnya.
      partOf().tabulasi_kedua(hasil_pertama)
      """
      c_df = data.copy()
      na_data = c_df.loc[c_df['label'] == 'non_atomik']
      data_na = [([na_data.ID[num], index, 'p{}'.format(idx)]) 
      for idx, num in enumerate(na_data.index) 
      for index in na_data.data[num] if index is not None]
      na_df = pd.DataFrame(data_na, columns= ['ID', 'req', 'label'])
      a_data = c_df.loc[c_df['label'] == 'atomik']
      data_a = [([a_data.ID[num], index, 'atomik']) for num in a_data.index 
                for idx, index in enumerate(a_data.data[num]) 
                if index is not None]
      a_df = pd.DataFrame(data_a, columns= ['ID', 'req', 'label'])
      part_df = pd.concat([a_df, na_df], ignore_index= True)
      part_srt = part_df.sort_values(by='ID', ignore_index= True).drop_duplicates()
      return part_srt

  def tabulasi_ketiga(self, data, data_index): # tabulasi ketiga
      """ fungsi ini digunakan untuk mengubah data data tabulasi kedua menjadi
      sebuah matriks indeks dan kolom yang saling berelasi satu sama lain.
      sehingga dengan cara ini, dapat terlihat relasi atomik, p# dalam sebuah kebutuhan
      partOf().tabulasi_ketiga(hasil_kedua, hasil_req)
      """
      part_srt = data.copy()
      list_data = [part_srt.loc[part_srt.ID == num].label 
                   for num in data_index.ID]
      tb_part = pd.DataFrame(list_data).fillna(0)
      tb_part.columns = part_srt.ID
      tb_part.index = data_index.ID
      return tb_part.reset_index()

  def tabulasi_alternatifernatif(self, data): # Alternatif
      """ fungsi ini digunakan untuk tabulasi ketiga alternatif.
      untuk memodifikasi kolom yang semula hanya memiliki p# saja, namun dengan 
      fungsi ini dapat melihat jenis non_atomik dalam sebuah kebutuhan.
      Berikut ini syntax yang digunakan.
      partOf().tabulasi_alternatifernatif(data)
      """
      d_df = data.copy()
      na_data = d_df.loc[d_df['label'] == 'non_atomik']
      data_na = [([na_data.ID[num], index, 'p{}'.format(idx)]) 
                    for idx, num in enumerate(na_data.index) 
                    for index in na_data.data[num] if index is not None]
      na_df = pd.DataFrame(data_na, columns= ['ID', 'data', 'label'])
      a_data = d_df.loc[d_df['label'] == 'atomik']
      dt = pd.concat([a_data, na_data, na_df], ignore_index= True)
      part_br = dt.sort_values(by='ID', ignore_index= True)
      list_data = [part_br.loc[part_br.ID == num].label for num in data.ID]
      dt_part = pd.DataFrame(list_data).fillna(0)

      # rename data
      data_part = [(['{}_{}'.format(na_data.ID[num], idy), index, 'p{}'.format(idx)]) 
                  for idx, num in enumerate(na_data.index) 
                  for idy, index in enumerate(na_data.data[num]) if index is not None]
      part_na = pd.DataFrame(data_part, columns= ['ID', 'req', 'label'])
      dt_rename = pd.concat([a_data, na_data, part_na], ignore_index= True)
      sort_rename = dt_rename.sort_values(by='ID')
      dt_part.columns= sort_rename.ID
      dt_part.index = data.ID
      return dt_part.reset_index()

  def tabulasi_visual(self, data): # visualisasi
      """ fungsi ini digunakan untuk melihat data secara visual, 
      fungsi efektif untuk merubah indeks data yang sama, mememiliki urutan
      sehingga penggunaan ini cocok untuk digunakan untuk proses selanjutnya 
      yaitu visual data 
      partOf().tabulasi_visual(data)
      """
      c_df = data.copy()
      na_data = c_df.loc[c_df['label'] == 'non_atomik']
      part_list = [([na_data.ID[num], index, 'p{}_{}'.format(idx, idy)]) 
      for idx, num in enumerate(na_data.index) 
      for idy, index in enumerate(na_data.data[num]) if index is not None]
      part_visual = pd.DataFrame(part_list, columns= ['ID', 'req', 'label'])
      return partOf.visualisasiGraph(self, data, part_visual, srs_param)

  def nilai_stat(self, data1, data2): # fungsi menentukan nilai statistik
      """ fungsi ini digunakan untuk melihat data statistik test, 
      fungsi efektif untuk melihat statistik secara keseluruhan, yang meliputi
      jumlah kebutuhan, atomik, nonatomik, klausa, maksimum kalimat, minimum kalimat
      cara menggunakan syntax ini adalah dengan cara 
      partOf().stat_stat(data1, data2)
      """
      jml_kebutuhan = len(data1)
      jml_minimum = data1.jumlah.min()
      jml_maksimum = data1.jumlah.max()
      jml_atomik = len(data1.loc[data1['label'] == 'atomik'])
      jml_nonatomik = len(data1.loc[data1['label'] == 'non_atomik'])
      jml_klausa =len(data2.loc[data2['label'] != 'atomik'])
      jml_df = pd.DataFrame([jml_kebutuhan,jml_atomik, jml_nonatomik, 
                             jml_minimum, jml_maksimum])
      jml_df.index = ['jumlah_kebtuhan', 'jumlah_atomik', 'jumlah_nonatomik', 
                      'minimum_jumlah_kalimat', 'maksimum_jumlah_kalimat']
      jml_df.columns = ['statistik_test']
      return jml_df.reset_index()

  def stat_grountruth(self, data):
      """ fungsi ini digunakan untuk melihat data statistik groundtruth, 
      fungsi efektif untuk melihat statistik secara keseluruhan, yang meliputi
      jumlah kebutuhan, atomik, nonatomik, klausa, maksimum kalimat, minimum kalimat
      cara menggunakan syntax ini adalah dengan cara 
      partOf().stat_grountruth(data)
      """
      df_part = data.copy()
      nlp = spacy.load('en_core_web_sm')
      jml_atomik = df_part.loc[df_part['Sentence'] == 'a'].Sentence.count()
      jml_nonAtomik = df_part.loc[df_part['Sentence'] != 'a'].drop_duplicates(subset='Sentence').Sentence.count()
      jml_klausa = df_part.loc[df_part['Sentence'] != 'a'].Sentence.count()
      jml_kebutuhan = jml_atomik + jml_nonAtomik
      jml_data = [len([idx for idx in nlp(num).sents])for num in df_part['Requirement Statement']]
      jml_a = [num for num in df_part.Sentence.value_counts().astype(int)]
      jml_min = min(jml_data)
      try:
        jml_maks = max(jml_a[1:])
      except:
        jml_maks = max(jml_data)

      jml_df = pd.DataFrame([jml_kebutuhan,jml_atomik, jml_nonAtomik, 
                              jml_min, jml_maks])
      jml_df.index = ['jumlah_kebtuhan', 'jumlah_atomik', 'jumlah_nonatomik', 
                      'minimum_jumlah_kalimat', 'maksimum_jumlah_kalimat']
      jml_df.columns = ['statistik_groundtruth']
      return jml_df.reset_index()

  def __del__(self):
      """ fungsi ini digunakan untuk mendestruksi, 
      cara meggunakan panggil fungsi dengan syntax berikut ini:
      partOf().__del__()
      """
      pass

  def extractPart(self, grd_param, file_param, srs_param, output= tab_param):
      """ fungsi ini digunakan untuk mengekstraksi secara lengkap data yang digunakan.
      fungsi ini menunjukkan data ekstraksi yang digunakan meliputi
      - part1: data filtrasi, data pertama, data kedua, data ketiga/alternatif, 
        data visual, data statistik, dan simpan
      - par2; data groundtruth beserta nilai statistiknya
      partOf().extractPart(grd_param, file_param, srs_param, 
      output= ['pertama', 'kedua', 'ketiga', 'alternatif', 'stat'])
      """
      part2 = partOf(grd_param)
      part_grd = part2.fulldataset(srs_param)
      data_grountruth = part2.stat_grountruth(part_grd)
      part2.__del__()

      part1 = partOf(file_param)
      dataReq = part1.fulldataset(srs_param)
      data_filtrasi = part1.tabulasi_filter(dataReq)
      data_pertama = part1.tabulasi_pertama(data_filtrasi, dataReq)
      data_kedua = part1.tabulasi_kedua(data_pertama)
      data_ketiga = part1.tabulasi_ketiga(data_kedua, data_pertama)
      alternatif = part1.tabulasi_alternatifernatif(data_pertama)
      data_visual = part1.tabulasi_visual(data_pertama)
      data_stat = part1.nilai_stat(data_pertama, data_kedua)
      part1.simpan_excel(data_pertama, data_kedua, data_ketiga, data_stat)
      part1.__del__() 

      if 'pertama' in output:
        print("\nTabulasi Pertama {}".format(srs_param))
        print(tabulate(data_pertama, headers = 'keys', tablefmt = 'psql'))

      elif 'kedua' in output:
        print("\nTabulasi Kedua {}".format(srs_param))
        print(tabulate(data_kedua, headers = 'keys', tablefmt = 'psql'))

      elif 'ketiga' in output:
        print("\nTabulasi Ketiga  {}".format(srs_param))
        print(tabulate(data_ketiga, headers = 'keys', tablefmt = 'psql'))

      elif 'alternatif' in output:
        print("\nTabulasi Ketiga Alternatif  {}".format(srs_param))
        print(tabulate(alternatif, headers = 'keys', tablefmt = 'psql'))

      elif 'stat' in output:
        print("\nTabulasi Statistik  {}".format(srs_param))
        print(tabulate(data_grountruth, headers = 'keys', tablefmt = 'psql'))
        print(tabulate(data_stat, headers = 'keys', tablefmt = 'psql'))
        part2.evaluasi_data(data_stat.drop('index', axis= 1), data_grountruth.drop('index', axis= 1))

if __name__ == "__main__":
  try:
    partOf().extractPart(tab_param)

  except OSError as err:
    print("OS error: {0}".format(err))