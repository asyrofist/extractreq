import streamlit as st

# library untuk modul 1
import xml.etree.ElementTree as ET
import pandas as pd

# library untuk modul 2
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# library untuk modul 3
from nltk.tokenize import word_tokenize 
from pywsd import disambiguate
from pywsd.cosine import cosine_similarity

stemming = PorterStemmer()
stops = set(stopwords.words("english"))
lem = WordNetLemmatizer()

"""
Modul ini dibuat oleh Rakha Asyrofi / 05111950010038

Original file is located at
    https://colab.research.google.com/drive/1h6HKNeALV8bXjrxWB0Jn0ztHtLv2cXz8
"""


# template class xmlparser
class xmlParser:

    # inisialisasi
    def __init__(self, filename= 'IRCI_Researcher.xmi', 
                 tipe_xmi= '{http://schema.omg.org/spec/XMI/2.1}type',
                 id_xmi= '{http://schema.omg.org/spec/XMI/2.1}id'):
    	self.namaFile = filename
    	self.xmi_type = tipe_xmi
    	self.xmi_id = id_xmi

    def data_root(self):
        tree = ET.parse(self.namaFile)
        root = tree.getroot()
        return root

    def dataPaketElemen(self, category = 'packagedElement'):
      try:
        hasil = []
        berdasarkanPackagedELement = [packagedElement.attrib for packagedElement in 
        xmlParser.data_root(self).iter(category)]
        for num in berdasarkanPackagedELement:
          a1 = num[self.xmi_id]
          b1 = num['name']
          d1 = num[self.xmi_type]
          hasil.append([a1, b1, d1])

        paketElemen = pd.DataFrame(hasil, columns=['id', 'name', 'type'])
        return paketElemen

      except OSError as err:
        print("OS error: {0}".format(err))

    def dataExtend(self, category = 'extend'):
      try:
        hasil = []
        berdasarkanExtend = [packagedElement.attrib for packagedElement in 
        xmlParser.data_root(self).iter(category)]
        for num in berdasarkanExtend:
          a1 = num[self.xmi_id]
          b1 = num[self.xmi_type]
          c1 = num['extendedCase']
          d1 = paketElemen[paketElemen['id'] == c1].iloc[0]['name']
          e1 = num['extension']
          f1 = paketElemen[paketElemen['id'] == e1].iloc[0]['name']
          hasil.append([a1, b1, c1, d1, e1, f1])
          
        extendTable = pd.DataFrame(hasil, columns=['id', 'type', 'source', 
        'sourceName', 'destination', 'destinationName'])
        return extendTable
      except OSError as err:
        print("OS error: {0}".format(err))

    def dataInclude(self, category = 'include'):
      try:
        hasil = []
        byinclude = [packagedElement.attrib for packagedElement in xmlParser.data_root(self).iter(category)]
        for num in byinclude:
          a1 = num['{http://schema.omg.org/spec/XMI/2.1}id']
          b1 = num['{http://schema.omg.org/spec/XMI/2.1}type']
          c1 = num['includingCase']
          d1 = paketElemen[paketElemen['id'] == c1].iloc[0]['name']
          e1 = num['addition']
          f1 = paketElemen[paketElemen['id'] == e1].iloc[0]['name']
          hasil.append([a1, b1, c1, d1, e1, f1])
        includeTable = pd.DataFrame(hasil, columns= ['id', 'tipe', 'include', 
        'includeName', 'addition', 'additionName'])
        return includeTable        
      except OSError as err:
        print("OS error: {0}".format(err))

    def dataOwnedEnd(self, category = 'ownedEnd'):
      try:
        # berdasarkan ownedEnd
        hasil = []
        berdasarkanOwnedEnd = [packagedElement.attrib for packagedElement in 
        xmlParser.data_root(self).iter(category)]
        berdasarkanOwnedEnd
        for num in berdasarkanOwnedEnd:
          a1 = num['type']
          b1 = num[self.xmi_id]
          c1 = num[self.xmi_type]
          d1 = paketElemen[paketElemen['id'] == a1].iloc[0]['name']
          hasil.append([a1, b1, c1, d1])
          
        ownedEndTable = pd.DataFrame(hasil, columns=['id_data', 'id_property', 
        'type_property', 'id_name'])
        return ownedEndTable
      except OSError as err:
        print("OS error: {0}".format(err))


    def dataOwnedMember(self, category = 'ownedMember'):
      try:
        # berdasarkan UML Model
        hasilNum = []
        berdasarkanOwnedMember = [packagedElement for packagedElement in 
        xmlParser.data_root(self).iter(category)]
        for num in berdasarkanOwnedMember:
          a = num.attrib[self.xmi_id]
          b = num.attrib[self.xmi_type]
          for index, angka in enumerate(num.iter('ownedEnd')):
            if index == 0:
              c = paketElemen[paketElemen['id'] == angka.attrib['type']].iloc[0]['name']
            else:
              d = paketElemen[paketElemen['id'] == angka.attrib['type']].iloc[0]['name']
          hasilNum.append([a, b, c, d])

        ownedMemberTable = pd.DataFrame(hasilNum, columns=['id', 'type_property', 
        'actor', 'usecase'])
        return ownedMemberTable  
      except OSError as err:
        print("OS error: {0}".format(err))

    def __del__(self):
        print ('Destructor called.')    

# template class parsingRequirement
class parsingRequirement:

    # inisialisasi
    def __init__(self, filename):
    	self.namaFile = filename
      
    #fungsi parse tree elemen
    def membacaCSV(self):
      try: 
        modul_pembacaan = pd.read_csv(self.namaFile, delimiter= ',')
        return modul_pembacaan
      except OSError as err:
        print("OS error: {0}".format(err))

    # cleaning text
    def apply_cleaning_function_to_list(self, X):
      try:
        cleaned_X = []
        for element in X:
            cleaned_X.append(parsingRequirement.clean_text(self, raw_text= element))
        return cleaned_X
      except OSError as err:
        print("OS error: {0}".format(err))

    def clean_text(self, raw_text):
      try:
        text = raw_text.lower()
        tokens = word_tokenize(text)
        token_words = [w for w in tokens if w.isalpha()]
        lemma_words = [lem.lemmatize(w) for w in token_words]
        meaningful_words = [w for w in lemma_words if not w in stops]
        joined_words = ( " ".join(meaningful_words))
        return joined_words
      except OSError as err:
        print("OS error: {0}".format(err))


    def __del__(self):
        print ('Destructor called.')

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
    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'Pilih modul yang anda inginkan?',
        ('modul1', 'modul2', 'modul3')
    )

    if(add_selectbox == 'modul1'):
      """# Modul1: xmlparser"""
      pilih_data = st.sidebar.selectbox(
        'Pilih file',
        ('IRCI_Researcher.xmi', 'IRCI_Topic.xmi', 'rAnalyzerUC.xmi')
      )
      if (pilih_data == 'IRCI_Researcher.xmi'):
          myXmlParser = xmlParser(filename= 'IRCI_Researcher.xmi')
          paketElemen = myXmlParser.dataPaketElemen()
          extendTable = myXmlParser.dataExtend()
          ownedEndTable = myXmlParser.dataOwnedEnd()
          ownedMemberTable = myXmlParser.dataOwnedMember()
          
          """
          Berikut ini penjelasan singkat Parsing file xmi menjadi tabel2 (daftar aktor, daftar use case, dan relasi antara actor use case dan antar use case)
          """
          """## Membaca data actor"""
          actorTable = paketElemen[paketElemen['type'] == 'uml:Actor']
          st.table(actorTable)
          """## Membaca data kasus pengguna"""
          useCaseTable = paketElemen[paketElemen['type'] == 'uml:UseCase']
          st.table(useCaseTable)
          """## Membaca relasi antar kasus pengguna"""
          st.table(extendTable)
          """## Membaca relasi asosiasi"""
          st.table(ownedMemberTable)
          """## Membaca relasi property"""
          st.table(ownedEndTable)

          hasilAktor = []
          hasilDestinasi = []

          for idx, num in enumerate(extendTable.sourceName):
            c = ownedMemberTable[ownedMemberTable['usecase'] == extendTable.sourceName[idx]]
            if len(c) > 0:
              for aktor in c.actor:
                hasilAktor.append(aktor)
                hasilDestinasi.append(extendTable.destinationName[idx])
            else:
              temp = 1
              d = ownedMemberTable[ownedMemberTable['usecase'] == extendTable.sourceName[idx-temp]]
              for dAktor in d.actor:
                hasilAktor.append(dAktor)
                hasilDestinasi.append(extendTable.destinationName[idx])

          df_a = pd.DataFrame([hasilAktor, hasilDestinasi], index= ['actor', 'action']).T
          df_a['actor'] = df_a.groupby(['action'])['actor'].transform(lambda x: ';'.join(x))
          df_a = df_a[['action','actor']].drop_duplicates()
          df_a['actor'][2] = set(df_a['actor'][2].split(";")) # fungsi ini digunakan untuk menyempurnakan format
          df_a['actor'][2] = ";".join(df_a['actor'][2])
          """## Membaca relasi aktor dan kasus pengguna"""
          st.table(df_a)

          myXmlParser.__del__()
      elif (pilih_data == 'IRCI_Topic.xmi'):
          myXmlParser = xmlParser(filename= 'IRCI_Topic.xmi')
          paketElemen = myXmlParser.dataPaketElemen()
          extendTable = myXmlParser.dataExtend()
          ownedEndTable = myXmlParser.dataOwnedEnd()
          ownedMemberTable = myXmlParser.dataOwnedMember()
          
          """
          Berikut ini penjelasan singkat Parsing file xmi menjadi tabel2 (daftar aktor, daftar use case, dan relasi antara actor use case dan antar use case)
          """
          """## Membaca data actor"""
          actorTable = paketElemen[paketElemen['type'] == 'uml:Actor']
          st.table(actorTable)
          """## Membaca data kasus pengguna"""
          useCaseTable = paketElemen[paketElemen['type'] == 'uml:UseCase']
          st.table(useCaseTable)
          """## Membaca relasi antar kasus pengguna"""
          st.table(extendTable)
          """## Membaca relasi asosiasi"""
          st.table(ownedMemberTable)
          """## Membaca relasi property"""
          st.table(ownedEndTable)

          hasilAktor = []
          hasilDestinasi = []

          for idx, num in enumerate(extendTable.sourceName):
            c = ownedMemberTable[ownedMemberTable['usecase'] == extendTable.sourceName[idx]]
            if len(c) > 0:
              for aktor in c.actor:
                hasilAktor.append(aktor)
                hasilDestinasi.append(extendTable.destinationName[idx])
            else:
              temp = 1
              d = ownedMemberTable[ownedMemberTable['usecase'] == extendTable.sourceName[idx-temp]]
              for dAktor in d.actor:
                hasilAktor.append(dAktor)
                hasilDestinasi.append(extendTable.destinationName[idx])

          df_a = pd.DataFrame([hasilAktor, hasilDestinasi], index= ['actor', 'action']).T
          df_a['actor'] = df_a.groupby(['action'])['actor'].transform(lambda x: ';'.join(x))
          df_a = df_a[['action','actor']].drop_duplicates()
          df_a['actor'][2] = set(df_a['actor'][2].split(";")) # fungsi ini digunakan untuk menyempurnakan format
          df_a['actor'][2] = ";".join(df_a['actor'][2])
          """## Membaca relasi aktor dan kasus pengguna"""
          st.table(df_a)

          myXmlParser.__del__()
      elif (pilih_data == 'rAnalyzerUC.xmi'):
          myXmlParser = xmlParser(filename= 'rAnalyzerUC.xmi')
          paketElemen = myXmlParser.dataPaketElemen()
          extendTable = myXmlParser.dataExtend()
          includeTable = myXmlParser.dataInclude()
          ownedMemberTable = myXmlParser.dataOwnedMember()
          ownedEndTable = myXmlParser.dataOwnedEnd()
          ownedMemberTable = myXmlParser.dataOwnedMember()
          
          """
          Berikut ini penjelasan singkat Parsing file xmi menjadi tabel2 (daftar aktor, daftar use case, dan relasi antara actor use case dan antar use case)
          """
          """## Membaca data actor"""
          actorTable = paketElemen[paketElemen['type'] == 'uml:Actor']
          st.table(actorTable)
          """## Membaca data kasus pengguna"""
          useCaseTable = paketElemen[paketElemen['type'] == 'uml:UseCase']
          st.table(useCaseTable)
          """## Membaca relasi antar kasus pengguna"""
          st.table(extendTable)
          """## Membaca relasi asosiasi"""
          st.table(ownedMemberTable)
          """## Membaca relasi property"""
          st.table(ownedEndTable)
          """## Membaca relasi include"""
          st.table(includeTable)

          # untuk include  data ranalyzer
          hasilAktor = []
          hasilDestinasi = []
          for idy, angka in enumerate(includeTable.includeName):
            f = ownedMemberTable[ownedMemberTable.usecase == includeTable.includeName[idy]]
            if len(f) > 0:
              for aktor in f.actor:
                hasilAktor.append(aktor)
                hasilDestinasi.append(includeTable.additionName[idy])
            else:
              tempY = 2
              g = ownedMemberTable[ownedMemberTable.usecase == includeTable.includeName[idy-tempY]]
              for dAktor in g.actor:
                hasilAktor.append(dAktor)
                hasilDestinasi.append(includeTable.additionName[idy])

          df_a = pd.DataFrame([hasilAktor, hasilDestinasi], index= ['actor', 'action']).T
          df_a['actor'] = df_a.groupby(['action'])['actor'].transform(lambda x: ';'.join(x))
          df_a = df_a[['action','actor']].drop_duplicates()
          df_a['actor'][0] = set(df_a['actor'][0].split(";")) # fungsi ini digunakan untuk menyempurnakan format
          df_a['actor'][0] = ";".join(df_a['actor'][0])
          ownedMemberTable.rename(columns = {'usecase':'action'}, inplace = True)
          dt_b = pd.concat([df_a, ownedMemberTable])
          dt_actor_action = dt_b.drop(['id', 'type_property'], axis= 1)
          """## Membaca relasi aktor dan kasus pengguna"""
          st.table(dt_actor_action)

          myXmlParser.__del__()

    elif(add_selectbox == 'modul2'):
        """# Modul2: build action and actor"""
        pilih_data = st.sidebar.selectbox(
          'Pilih file',
          ('freqs_researcher.txt', 'researcher_insert_metadata.txt', 'researcher_search_researcher.txt')
        )
        if (pilih_data == 'freqs_researcher.txt'):
            # parsing functional
            MyParsingRequirement = parsingRequirement(filename= "freqs_researcher.txt")
            freqs = MyParsingRequirement.membacaCSV()

            # pembersihan data
            freq_requirement = freqs.requirement
            id_freq_requirement = freqs.id
            text_to_clean_freq = list(freq_requirement)
            cleaned_freq = MyParsingRequirement.apply_cleaning_function_to_list(text_to_clean_freq)

            data_aktor = []
            data_aksi = []
            for num in cleaned_freq:
              a = (word_tokenize(num))
              b = [x for x in a if x == 'submitter' or x == 'system']  
              b1 = " ".join(b)
              data_aktor.append(b1)
              c = [x for x in a if x != 'submitter' and x != 'system']  
              c1 = " ".join(c)
              data_aksi.append(c1)

            freqs['aksi'] = data_aksi
            freqs['aktor'] = data_aktor
            """## Membaca kebutuhan fungsional"""
            st.table(freqs)

        elif (pilih_data == 'researcher_insert_metadata.txt'):
            # parsing ucd1
            MyParsingRequirement = parsingRequirement(filename= "researcher_insert_metadata.txt")
            ucd1 = MyParsingRequirement.membacaCSV()
            data_ucd1 = []
            for num in ucd1.flowOfEvents.fillna("empty"):
              for num1 in num.split(";"):
                for num2 in num1.split("."):
                  if 'Submitter' in num2:
                    data_ucd1.append(num2)
                  elif 'system' in num2:
                    data_ucd1.append(num2)
                  elif 'empty' in num2:
                    data_ucd1.append(num2)

            list_index= [("data{}".format(idx)) for idx, num in enumerate(data_ucd1)]
            data_list = pd.DataFrame(data_ucd1, index= list_index)
            data_list = data_list.drop(index= "data5").reset_index().drop(labels= ['index'], axis= 1)
            ucd1['aksi'] = data_list

            ucd1_req = ucd1.aksi
            id_ucd1_req = ucd1.id
            text_to_clean_freq = list(ucd1_req)
            cleaned1_ucd = MyParsingRequirement.apply_cleaning_function_to_list(text_to_clean_freq)

            data_aktor = []
            data_aksi = []
            for num in cleaned1_ucd:
              a = (word_tokenize(num))
              b = [x for x in a if x == 'submitter' or x == 'system']  
              b1 = " ".join(b)
              data_aktor.append(b1)
              c = [x for x in a if x != 'submitter' and x != 'system']  
              c1 = " ".join(c)
              data_aksi.append(c1)

            ucd1['aksi'] = data_aksi
            ucd1['aktor'] = data_aktor
            """## Membaca kasus penggunaan (UCD1)"""
            st.table(ucd1)

        elif (pilih_data == 'researcher_search_researcher.txt'):
            # parsing ucd2
            MyParsingRequirement = parsingRequirement(filename= "researcher_search_researcher.txt")
            ucd2 = MyParsingRequirement.membacaCSV()

            #variable
            data_ucd2 = []
            for num in ucd2.flowOfEvents.fillna("empty"):
              for num1 in num.split(";"):
                for num2 in num1.split("."):
                  if 'Submitter' in num2:
                    data_ucd2.append(num2)
                  elif 'system' in num2:
                    data_ucd2.append(num2)
                  elif 'actor' in num2:
                    data_ucd2.append(num2)
                  elif 'empty' in num2:
                    data_ucd2.append(num2)

            list2_index= [("data{}".format(idx)) for idx, num in enumerate(data_ucd2)]
            data2_list = pd.DataFrame(data_ucd2, index= list2_index)
            data2_list = data2_list.reset_index().drop(labels= ['index'], axis= 1)
            ucd2['aksi'] = data2_list

            ucd2_req = ucd2.aksi
            id_ucd2_req = ucd2.id
            text_to_clean_freq = list(ucd2_req)
            cleaned2_ucd = MyParsingRequirement.apply_cleaning_function_to_list(text_to_clean_freq)

            data2_aktor = []
            data2_aksi = []
            for num in cleaned2_ucd:
              a = (word_tokenize(num))
              b = [x for x in a if x == 'submitter' or x == 'system' or x == 'actor']  
              b1 = " ".join(b)
              b1 = b1.replace("actor", "submitter; viewer")
              data2_aktor.append(b1)
              c = [x for x in a if x != 'submitter' and x != 'system' and x != 'actor']  
              c1 = " ".join(c)
              data2_aksi.append(c1)

            ucd2['aksi'] = data2_aksi
            ucd2['aktor'] = data2_aktor
            
            """## Membaca kasus penggunaan (UCD2)"""
            st.table(ucd2)

    elif(add_selectbox == 'modul3'):
      """# Modul3: pencarian relasi"""
      pilih_data = st.sidebar.selectbox(
      'Pilih file',
      ('freq_ucd1', 'freq_ucd1', 'all'))

      MyucdReq = ucdReq(data_aksi_aktor= r'data_aksi_aktor.xlsx', tabel_usecase= r'data_xmi.xlsx')
      tabel_freq =  'tabel_freqs'
      freqs = MyucdReq.fulldataset(inputData= tabel_freq)
      tabel_ucd1 =  'tabel_ucd1'
      ucd1 = MyucdReq.fulldataset(inputData= tabel_ucd1)
      tabel_ucd2 =  'tabel_ucd2'
      ucd2 = MyucdReq.fulldataset(inputData= tabel_ucd2)
      if (pilih_data == 'freq_ucd1'):
          ucd1= ucd1.dropna()
          tbl_1 = MyucdReq.useCaseMeasurement(keyword1= freqs.aksi, keyword2=ucd1.aksi , id1= freqs.id, id2= ucd1.usecase)
          """## Data Pengukuran antara functional dan ucd1"""
          st.table(tbl_1)

      elif (pilih_data == 'freq_ucd1'):
          ucd2= ucd2.dropna()
          tbl_2 = MyucdReq.useCaseMeasurement(keyword1= freqs.aksi, keyword2=ucd2.aksi , id1= freqs.id, id2= ucd2.usecase)
          """## Data Pengukuran antara functional dan ucd2"""
          st.table(tbl_2)

      elif (pilih_data == 'all'):
          ucd1= ucd1.dropna()
          tbl_1 = MyucdReq.useCaseMeasurement(keyword1= freqs.aksi, keyword2=ucd1.aksi , id1= freqs.id, id2= ucd1.usecase)
          ucd2= ucd2.dropna()
          tbl_2 = MyucdReq.useCaseMeasurement(keyword1= freqs.aksi, keyword2=ucd2.aksi , id1= freqs.id, id2= ucd2.usecase)
          tbl_3 = pd.concat([tbl_1, tbl_2], axis= 1)
          """## Data Pengukuran Gabungan kedua tabel"""
          st.table(tbl_3)
