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
	myPart = partOf(inputData, # dataset
			dataStanford,  #diambil dari https://stanfordnlp.github.io/CoreNLP/download.html
			urlStanford) # url corenlp 'http://corenlp.run/' 
	myPart.preprocessing()
	myPart.fulldataset(inputData)
	myPart.parsing(data)
	myPart.stanfordConstinuityParsing(data)

Berikut ini penjelasan singkat darri contoh syntax tersebut.

- myPart.preprocessing()
bagian ini menunjukkan bagaimana cara pengembang melihat daftar dataset yang digunakan. Daftar dataset ini diambil dari excel dengan memilah daftar sheet yang digunakan. sehingga dengan jelas memperlihatkan daftar data yang digunakan.

- myPart.fulldataset(inputData) 
Bagian ini memperlihatkan dataset secara secara spesifik, sehingga cocok digunakan untuk data_raw awal sebelum dilakukan pra-pemrosesan maupun kegiatan lainnya. Karena data tersebut cenderung berbeda-beda terhadap setiap hasil yang diambil. 

- myPart.parsing(data)
Sesuai dengan perintahnya menunjukkan hasil parsing dari sebuah dokumen, sehingga hasil data berupa parse tree dari dari visualisasi corenlp dari uril berikut ini 'http://corenlp.run/' 

- myPart.stanfordConstinuityParsing(data)
cara kerjanya sama halnya dengan syntax sebelumnya yaitu parsing, namun bedanya hanya pada visualisasi parse tree dengan menggunakan instalasi package stanford yang telah didownload sebelumnya dari laman berikut ini  https://stanfordnlp.github.io/CoreNLP/download.html
