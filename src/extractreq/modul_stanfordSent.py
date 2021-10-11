__copyright__ = "Copyright (c) 2021"
__author__ = "Rakha Asyrofi"
__date__ = "2021-10-08:18:07:39"

#@title Modul: Stanford Clause { vertical-output: true }
url_param = "http://corenlp.run" #@param {type:"string"}
model_param = "/content/drive/MyDrive/stanford-corenlp-4.0.0" #@param {type:"string"}
dataFile = "/content/drive/MyDrive/dataset/dataset_2.xlsx" #@param {type:"string"}
srs_param = "2005 - Grid 3D" #@param ["0000 - cctns", "0000 - gamma j", "0000 - Inventory", "1998 - themas", "1999 - dii", "1999 - multi-mahjong", "1999 - tcs", "2000 - nasa x38", "2001 - ctc network", "2001 - esa", "2001 - hats", "2001 -libra", "2001 - npac", "2001 - space fractions", "2002 - evia back", "2002 - evia corr", "2003 - agentmom", "2003 - pnnl", "2003 - qheadache", "2003 - Tachonet", "2004 - colorcast", "2004 - eprocurement", "2004 - grid bgc", "2004 - ijis", "2004 - Phillip", "2004 - rlcs", "2004 - sprat", "2005 - clarus high", "2005 - clarus low", "2005 - Grid 3D", "2005 - nenios", "2005 - phin", "2005 - pontis", "2005 - triangle", "2005 - znix", "2006 - stewards", "2007 - ertms", "2007 - estore", "2007 - nde", "2007 - get real 0.2", "2007 - mdot", "2007 - nlm", "2007 - puget sound", "2007 - water use", "2008 - caiso", "2008 - keepass", "2008 - peering", "2008 - viper", "2008 - virtual ed", "2008 - vub", "2009 - email", "2009 - gaia", "2009 - inventory 2.0", "2009 - library", "2009 - library2", "2009 - peazip", "2009 - video search", "2009 - warc III", "2010 - blit draft", "2010 - fishing", "2010 - gparted", "2010 - home", "2010 - mashboot", "2010 - split merge"]
col_param = "Requirement Statement" #@param ["Requirement Statement", "req"]
id_param = "ID" #@param ["ID"]

import re, nltk, json, pandas as pd
# from pycorenlp import StanfordCoreNLP
from stanfordcorenlp import StanfordCoreNLP
from tabulate import tabulate

class stanford_clause:
    def __init__(self, fileName= dataFile, url_stanford= url_param, 
                 model_stanford = model_param):
        """ parameter inisialisasi, data yang digunakan pertama kali 
        untuk contruct data
        """
        # self.nlp = StanfordCoreNLP(url_stanford) # pycoren;lp
        self.nlp = StanfordCoreNLP(url_stanford, port= 80) #stanfordcorenlp
        # self.nlp = StanfordCoreNLP(model_stanford) #stanfordcorenlp
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

    def get_verb_phrases(self, t):
        verb_phrases = []
        num_children = len(t)
        num_VP = sum(1 if t[i].label() == "VP" else 0 for i in range(0, num_children))

        if t.label() != "VP":
            for i in range(0, num_children):
                if t[i].height() > 2:
                    verb_phrases.extend(stanford_clause.get_verb_phrases(self, t[i]))
        elif t.label() == "VP" and num_VP > 1:
            for i in range(0, num_children):
                if t[i].label() == "VP":
                    if t[i].height() > 2:
                        verb_phrases.extend(stanford_clause.get_verb_phrases(self, t[i]))
        else:
            verb_phrases.append(' '.join(t.leaves()))

        return verb_phrases

    def get_pos(self, t):
        vp_pos = []
        sub_conj_pos = []
        num_children = len(t)
        children = [t[i].label() for i in range(0,num_children)]

        flag = re.search(r"(S|SBAR|SBARQ|SINV|SQ)", ' '.join(children))
        if "VP" in children and not flag:
            # print(t[i].label())
            for i in range(0, num_children):
                if t[i].label() == "VP":
                    vp_pos.append(t[i].treeposition())
        elif not "VP" in children and not flag:
            for i in range(0, num_children):
                if t[i].height() > 2:
                    temp1,temp2 = stanford_clause.get_pos(self, t[i])
                    vp_pos.extend(temp1)
                    sub_conj_pos.extend(temp2)
        else:
            for i in range(0, num_children):
                if t[i].label() in ["S","SBAR","SBARQ","SINV","SQ"]:
                    temp1, temp2 = stanford_clause.get_pos(self, t[i])
                    vp_pos.extend(temp1)
                    sub_conj_pos.extend(temp2)
                else:
                    sub_conj_pos.append(t[i].treeposition())

        return (vp_pos,sub_conj_pos)


    def get_clause_list(self, sent):
        parser = self.nlp.annotate(sent, properties={"annotators":"parse","outputFormat": "json"})
        # sent_tree = nltk.tree.ParentedTree.fromstring(parser["sentences"][0]["parse"])
        parser_json = json.loads(parser)
        sent_tree = nltk.tree.ParentedTree.fromstring(parser_json["sentences"][0]["parse"])
        clause_level_list = ["S","SBAR","SBARQ","SINV","SQ"]
        clause_list = []
        sub_trees = []

        # break the tree into subtrees of clauses using
        # clause levels "S","SBAR","SBARQ","SINV","SQ"
        for sub_tree in reversed(list(sent_tree.subtrees())):
            # print(sub_tree.label() == 'CC')
            if sub_tree.label() in clause_level_list:
                if sub_tree.parent().label() in clause_level_list:
                    continue
                if (len(sub_tree) == 1 and sub_tree.label() == "S" and sub_tree[0].label() == "VP"
                    and not sub_tree.parent().label() in clause_level_list):
                    continue
                sub_trees.append(sub_tree)
                del sent_tree[sub_tree.treeposition()]

        
        for t in sub_trees: # for each clause level subtree, extract relevant simple sentence
            verb_phrases = stanford_clause.get_verb_phrases(self, t) # get verb phrases from the new modified tree
            vp_pos,sub_conj_pos = stanford_clause.get_pos(self, t)
            for i in vp_pos:
                del t[i]
            for i in sub_conj_pos:
                del t[i]
            subject_phrase = ' '.join(t.leaves())
            for i in verb_phrases: # update the clause_list
                clause_list.append(subject_phrase + " " + i)
        return clause_list

    def __del__(self):
        pass

    def main(self, srs_param, id_param, col_param):
        id_req = stanford_clause.fulldataset(self, srs_param)[id_param]
        req = stanford_clause.fulldataset(self, srs_param)[col_param]
        data_clausa = []
        for id, num in zip(id_req, req):
            sent = re.sub(r"(\.|,|\?|\(|\)|\[|\])"," ",num)
            clause_list = [idx for idx in stanford_clause.get_clause_list(self, sent)]
            jml_clausa = len(clause_list)
            label_df = []
            if jml_clausa > 1: # non atomik berdasarkan jumlah
                label_df.append('non_atomik')
            elif jml_clausa == 1:
                label_df.append('atomik')
            else:
                label_df.append('unknown')            
            data_clausa.append([id, num, clause_list, label_df[0], jml_clausa])
        clausa_df = pd.DataFrame(data_clausa, columns= ['id', 'req', 'data', 'label', 'jumlah'])
        stanford_clause.__del__(self)
        return clausa_df

if __name__ == "__main__":
  try:
    klausa = stanford_clause(dataFile).main(srs_param, id_param, col_param)
    print(tabulate(klausa, headers = 'keys', tablefmt = 'psql'))

    # sent =  'Joe waited for the train, but the train was late.'
    # sent = re.sub(r"(\.|,|\?|\(|\)|\[|\])"," ",sent)
    # clause_list = stanford_clause().get_clause_list(sent)
    # print(clause_list)

  except OSError as err:
    print("OS error: {0}".format(err))