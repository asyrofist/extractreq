[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5528399.svg)](https://ponselharian.com/P0m2Kr)
![image](https://visitor-badge.laobi.icu/badge?page_id=asyrofist/Extraction-Requirement) 
![PyPI - Python Version](https://img.shields.io/badge/python-3.7.0-blue.svg)
[![PyPI](https://img.shields.io/pypi/v/extractreq.svg)](https://ponselharian.com/pgPXV5m4GRJh)
[![Documentation Status](https://readthedocs.org/projects/extraction-requirement/badge/?version=latest)](https://ponselharian.com/3cNwdU)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[![Build Status](https://app.travis-ci.com/asyrofist/Extraction-Requirement.svg?branch=main)](https://ponselharian.com/Tu5x7pyIw)
[![Paper](http://img.shields.io/badge/Paper-PDF-red.svg)](https://ponselharian.com/SNUKbnCs)
[![Slide](http://img.shields.io/badge/Slides-PDF-orange.svg)](https://ponselharian.com/gVyGBgAsQ)
![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=nltk&package-manager=pip&previous-version=3.2.5&new-version=3.6.5)
[![Maintainability](https://api.codeclimate.com/v1/badges/e7007abd72e445009895/maintainability)](https://ponselharian.com/oes)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e7007abd72e445009895/test_coverage)](https://ponselharian.com/SBniefiUY)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://ponselharian.com/IP9qQuFZw8)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ponselharian.com/3c6DDa6MH)

# Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing

[live_demo](https://ponselharian.com/hXj9uI5g44) How to make Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing, berikut ini penjelasan singkat data yang telah dibuat. Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing described in our Proceeding Conference at [ISRITI2020](https://ponselharian.com/SNUKbnCs). Please kindly cite the following paper when you use this tool. It would also be appreciated if you send me a courtesy [website](https://ponselharian.com/ZAjl8) and [google scholar](https://ponselharian.com/JO8ZMfIe), so I could survey what kind of tasks the tool is used for. 

Developed by Asyrofi (c) 2021

## How to install

installation using pypi:

    pip install extractreq

## How easy to use

### ekspart module:

```python
from extractreq.modul_ekspart import partOf
grd_param = "grd.xlsx"
file_param = "test.xlsx"
srs_param = "indeks_parameter"

# output_mode = ['pertama', 'kedua', 'ketiga', 'stat']
partOf().extractPart(grd_param, file_param, srs_param, 'pertama')
```
[check out my video explanation](https://ponselharian.com/0eCjkc) 

### Stanford modul:
```python
from extractreq.modul_stanfordSent import stanford_clause
sent = "I have friends, but nobody cares me"
stanford_clause().get_clause_list(sent)
# stanford_clause(file_param).main(srs_param)
```

### Spacy modul:
```python
from extractreq.modul_spacySent import spacyClause, spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("I love you 300, but I don't like you")
spacyClause().extractData(doc)
# spacyClause(file_param).main(srs_param)
```

### Triplet modul:
```python
from extractreq.modul_triplet import extractNlp
sent = "I have friends, but nobody cares me"
# output_mode = ['parse_tree', 'spo', 'result']
extractNlp().triplet_extraction(sent, 'parse_tree')
# extractNlp(file_param).main(srs_param, output)
```


## Features
- Dapat digunakan untuk mengekstraksi kebergantungan kebutuhan
- Dapat digunakan untuk mencari relasi kebergantungan kebutuhan
- Dapat digunakan memisahkan kalusa dari setiap kalimat menggunakan stanford, spacy
- Dapat memisahkan triplet dari sebua kalimat

## Contribute

- [Issue Tracker](https://github.com/asyrofist/Extraction-Requirement/issues)
- [Source Code](https://ponselharian.com/9Eq9zlrI)

## Support

If you are having issues, please let us know. We have a mailing list located at: asyrofi.19051@mhs.its.ac.id

## Citation

If you find this repository useful for your research, please use the following.

```
@INPROCEEDINGS{9315489,  author={Asyrofi, Rakha and Siahaan, Daniel Oranova and Priyadi, Yudi},  
booktitle={2020 3rd International Seminar on Research of Information Technology and Intelligent Systems (ISRITI)},   
title={Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing},   
year={2020},  
pages={332-337},  
doi={10.1109/ISRITI51436.2020.9315489}}
```

## License

The project is licensed under the MIT License


## Reference

- [Sentence-to-clauses](https://github.com/rahulkg31/sentence-to-clauses)
- [spacy sentence to clauses](https://subscription.packtpub.com/book/data/9781838987312/2/ch02lvl1sec13/)
- [sentence-triplet](https://github.com/kj-lai/SentenceTriplet)
- [proceeding conference ISRITI 2020](https://ponselharian.com/0eCjkc)
