import pandas as pd
from tabulate import tabulate
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English



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
        nlp = English()
        tokenizer = Tokenizer(nlp.vocab)
        tokens = tokenizer(raw_text)
        lemma_list = [token.lemma_.lower() for token in tokens if token.is_stop is False and token.is_punct is False and token.is_alpha is True]
        joined_words = ( " ".join(lemma_list))
        return joined_words

      except OSError as err:
        print("OS error: {0}".format(err))


    def data_raw(self, data_raw): # get data raw
        data_num2 = []
        for num in data_raw.fillna("empty"):
          for num1 in num.split(";"):
            for num2 in num1.split("."):
              if 'Submitter' in num2:
                data_num2.append(num2)
              if 'Viewer' in num2:
                data_num2.append(num2)
              elif 'system' in num2:
                data_num2.append(num2)
              elif 'actor' in num2:
                data_num2.append(num2)
              elif 'empty' in num2:
                data_num2.append(num2)
        return data_num2        

    def aksi_aktor(self, data): # get data aksi dan aktor
      try:
        nlp = English()
        tokenizer = Tokenizer(nlp.vocab)
        tokens = tokenizer(data)
        a = [token.text for token in tokens]
        b = [x for x in a if x == 'submitter' or x == 'viewer' or x == 'system' or x == 'actor']  
        b1 = ";".join(b)
        b1 = b1.replace("actor", "submitter; viewer")
        c = [x for x in a if x != 'submitter' and x != 'viewer' and x != 'system' and x != 'actor']  
        c1 = " ".join(c)
        return b1, c1        
      except OSError as err:
        print("OS error: {0}".format(err))


    def __del__(self):
        print ('Destructor called.')

if __name__ == "__main__":
  try:

    # parsing functional
    MyParsingRequirement = parsingRequirement(filename)
    freqs = MyParsingRequirement.membacaCSV()
    data_freqs = MyParsingRequirement.data_raw(freqs.requirement)

    # pembersihan data
    freq_requirement = freqs.requirement
    id_freq_requirement = freqs.id
    text_to_clean_freq = list(freq_requirement)
    cleaned_freq = MyParsingRequirement.apply_cleaning_function_to_list(text_to_clean_freq)

    data_aktor = []
    data_aksi = []
    for num in cleaned_freq:
      dt_aksi_aktor = MyParsingRequirement.aksi_aktor(num)
      data_aktor.append(dt_aksi_aktor[0])
      data_aksi.append(dt_aksi_aktor[1])

    freqs['aksi'] = data_aksi
    freqs['aktor'] = data_aktor
    print("\nfreqs")
    print(tabulate(freqs, headers = 'keys', tablefmt = 'psql'))

    # parsing ucd1
    MyParsingRequirement = parsingRequirement(filename)
    ucd1 = MyParsingRequirement.membacaCSV()
    data_ucd1 = MyParsingRequirement.data_raw(ucd1.flowOfEvents)

    list_index= [("data{}".format(idx)) for idx, num in enumerate(data_ucd1)]
    data_list = pd.DataFrame(data_ucd1, index= list_index)
    data_list = data_list.drop(index= "data5").reset_index().drop(labels= ['index'], axis= 1)
    ucd1['aksi'] = data_list

    ucd1_req = ucd1.aksi
    id_ucd1_req = ucd1.id
    text_to_clean_ucd1 = list(ucd1_req)
    cleaned1_ucd = MyParsingRequirement.apply_cleaning_function_to_list(text_to_clean_ucd1)

    data1_aktor = []
    data1_aksi = []
    for num in cleaned1_ucd:
      dt_aksi_aktor = MyParsingRequirement.aksi_aktor(num)
      data1_aktor.append(dt_aksi_aktor[0])
      data1_aksi.append(dt_aksi_aktor[1])

    ucd1['aksi'] = data1_aksi
    ucd1['aktor'] = data1_aktor
    print("\nucd1")
    print(tabulate(ucd1, headers = 'keys', tablefmt = 'psql'))

    # parsing ucd2
    MyParsingRequirement = parsingRequirement(filename)
    ucd2 = MyParsingRequirement.membacaCSV()
    data_ucd2 = MyParsingRequirement.data_raw(ucd2.flowOfEvents)

    list2_index= [("data{}".format(idx)) for idx, num in enumerate(data_ucd2)]
    data2_list = pd.DataFrame(data_ucd2, index= list2_index)
    data2_list = data2_list.reset_index().drop(labels= ['index'], axis= 1)
    ucd2['aksi'] = data2_list

    ucd2_req = ucd2.aksi
    id_ucd2_req = ucd2.id
    text_to_clean_ = list(ucd2_req)
    cleaned2_ucd = MyParsingRequirement.apply_cleaning_function_to_list(text_to_clean_)

    data2_aktor = []
    data2_aksi = []
    for num in cleaned2_ucd:
      dt_aksi_aktor = MyParsingRequirement.aksi_aktor(num)
      data2_aktor.append(dt_aksi_aktor[0])
      data2_aksi.append(dt_aksi_aktor[1])

    ucd2['aksi'] = data2_aksi
    ucd2['aktor'] = data2_aktor
    print("\nucd2")
    print(tabulate(ucd2, headers = 'keys', tablefmt = 'psql'))

  except OSError as err:
      print("OS error: {0}".format(err))
