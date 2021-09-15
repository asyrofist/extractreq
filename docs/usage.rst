============
Instalasi
============

Install langsung dari pypi
-------------------

Install the package with pip::

    $ pip install extractreq

Cara ini digunakan untuk pengguna dapat menggunakan library ini. adapun untuk menginstal dapat menggunakan cara lain, seperti langsung menginstal dari repository package library ini dari 

Install Langsung dari Repository
-------------------

Atau jika terlalu susah untuk menginstalnya, tinggal download berkas dari laman berikut ini. Cukup mudah dan simpel tinggal klik bagian code dan download zip tersebut.

**Download extract-req**: https://github.com/asyrofist/Extraction-Requirement

::

    cd Extraction-Requirement
    python setup.py install
    # If root permission is not available, add --user command like below
    # python setup.py install --user

Currently, pip install is not supported but will be addressed.


Instalasi Extraksi Kebergantungan Kebutuhan
------------------------------------------
Library ini dapat digunakan menggunakan spesifikasi dibawah ini, dimana python dan requirement yang dibutuhkan adalah sebagai berikut.
karena pengembangan menggunakan environment 3.7 maka disarankan untuk menginstal diatas versi tersebut.

- Python :code:`>= 3.7`

Requirements
------------
Dalam instalasi ini, membutuhkan package yang lain seperti daftar berikut ini. anda bisa melihatnya di 
(bagian depan repository github saya yang berada di :doc:`/requirement.txt` section.) 
Segala macam detail saya jelaskan pada sebagai berikut.

- pywsd :code:`1.1.0`
- wn :code:`0.0.2`
- sklearn 
- stanfordcorenlp
- nltk
- openpyxl
- pandas
- numpy


========
Penggunaan
========
Contoh Penggunaan Library
------------

Bagaimana cara menggunakan template ini, dapat dilihat dari contoh syntax berikut ini::

	from extractreq.partof_modul1 import partOf
	myPart = partOf(inputData= 'dataset.xlsx', # dataset
			dataStanford= 'stanford-corenlp-4.0.0',  #diambil dari https://stanfordnlp.github.io/CoreNLP/download.html
			urlStanford= 'http://corenlp.run/')
	myPart.preprocessing()
	myPart.fulldataset(inputData= '2005 - Grid 3D')
	myPart.parsing(data)
	myPart.stanfordPostag(data)
