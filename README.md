# Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing

Author  | [Rakha Asyrofi](https://scholar.google.com/citations?user=WN9T5UUAAAAJ&hl=id&oi=ao)
 -------|-----------
Version | 0.0.1
Updated | 2021-09-12

# overview
![extraction_req](https://github.com/asyrofist/Extraction-Requirement/blob/main/streamlit-app-2021-09-11-02-09-60%20(3).gif)
[live_demo](https://share.streamlit.io/asyrofist/extraction-requirement/main/app.py) How to make Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing

Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing described in our Proceeding Conference at [ISRITI2020](https://ieeexplore.ieee.org/document/9315489). Please kindly cite the following paper when you use this tool. It would also be appreciated if you send me a courtesy [website](https://www.researchgate.net/profile/Rakha_Asyrofi) and [google scholar](https://scholar.google.com/citations?user=WN9T5UUAAAAJ&hl=id&oi=ao), so I could survey what kind of tasks the tool is used for. 
```
@INPROCEEDINGS{9315489,  
  author={R. {Asyrofi} and D. O. {Siahaan} and Y. {Priyadi}},  
  booktitle={2020 3rd International Seminar on Research of Information Technology and Intelligent Systems (ISRITI)},   
  title={Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing},   
  month={January},
  year={2021},  
  address={"Yogyakata, Indonesia"},  
  publisher = "IEEE",
  url = "https://ieeexplore.ieee.org/document/9315489",
  pages={332-337},  
  language = "English",
  doi={10.1109/ISRITI51436.2020.9315489}}
  ISBN = "978-1-7281-8406-7",
```

Developed by Asyrofi (c) 2021

## Cara menginstal

instalasi melalui pypi:

    pip install extractreq


## Cara menggunakan program

```python
from extractreq.partof_modul1 import partOf
myPart = partOf(inputData= 'dataset.xlsx', # dataset
                dataStanford= 'stanford-corenlp-4.0.0',  #diambil dari https://stanfordnlp.github.io/CoreNLP/download.html
                urlStanford= 'http://corenlp.run/')
myPart.preprocessing()
myPart.fulldataset(inputData= '2005 - Grid 3D')
myPart.parsing(data)
myPart.stanfordPostag(data)
```

Check out: https://youtu.be/-d96h9mhh9s



