[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5528399.svg)](https://doi.org/10.5281/zenodo.5528399)
![image](https://visitor-badge.laobi.icu/badge?page_id=asyrofist/Extraction-Requirement) 
<!-- [![Contributors][contributors-shield]][contributors-url] 
[![Forks][forks-shield]][forks-url] 
[![Stargazers][stars-shield]][stars-url] 
[![Issues][issues-shield]][issues-url] 
[![MIT License][license-shield]][license-url] 
[![LinkedIn][linkedin-shield]][linkedin-url] 
[![Discord][discord-shield]][discord-url] 
[![Medium][medium-shield]][medium-url]
 -->
# Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing

Author  | [Rakha Asyrofi](https://scholar.google.com/citations?user=WN9T5UUAAAAJ&hl=id&oi=ao)
 -------|-----------
Version | 0.0.1
Updated | 2021-09-12

# overview
[live_demo](https://share.streamlit.io/asyrofist/extraction-requirement/main/app.py) How to make Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing

Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing described in our Proceeding Conference at [ISRITI2020](https://ieeexplore.ieee.org/document/9315489). Please kindly cite the following paper when you use this tool. It would also be appreciated if you send me a courtesy [website](https://www.researchgate.net/profile/Rakha_Asyrofi) and [google scholar](https://scholar.google.com/citations?user=WN9T5UUAAAAJ&hl=id&oi=ao), so I could survey what kind of tasks the tool is used for. 

Developed by Asyrofi (c) 2021

## How to install

installation using pypi:

    pip install extractreq

## Look how easy it is to use:

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

## Features
- Dapat digunakan untuk mengekstraksi kebergantungan kebutuhan
- Dapat digunakan untuk mencari relasi kebergantungan kebutuhan

## Contribute

- Issue Tracker: https://github.com/asyrofist/Extraction-Requirement/issues
- Source Code: https://github.com/asyrofist/Extraction-Requirement

## Support

If you are having issues, please let us know. We have a mailing list located at: asyrofi.19051@mhs.its.ac.id

## Citation

If you find this repository useful for your research, please use the following.

```
@INPROCEEDINGS{9315489,  author={Asyrofi, Rakha and Siahaan, Daniel Oranova and Priyadi, Yudi},  
booktitle={2020 3rd International Seminar on Research of Information Technology and Intelligent Systems (ISRITI)},   
title={Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing},   
year={2020},  
volume={},  
number={},  
pages={332-337},  
doi={10.1109/ISRITI51436.2020.9315489}}
```

## License

The project is licensed under the MIT License
