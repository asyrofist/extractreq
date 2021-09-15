.. _install:

=======
Install
=======

Instalasi Extraksi Kebergantungan Kebutuhan
=================
SIMPLE-NN is tested and supported on the following versions of Python:

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

Install from source
-------------------

Atau jika terlalu susah untuk menginstalnya, tinggal download berkas dari laman berikut ini. Cukup mudah dan simpel tinggal klik bagian code dan download zip tersebut.

**Download extract-req**: https://github.com/asyrofist/Extraction-Requirement

::

    cd Extraction-Requirement
    python setup.py install
    # If root permission is not available, add --user command like below
    # python setup.py install --user

Currently, pip install is not supported but will be addressed.
