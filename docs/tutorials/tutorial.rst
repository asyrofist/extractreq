=========
Tutorials
=========

Cara menjalankan program
=================
cara menggunakannya cukup simepl. tinggal masukkan sesuai dengan command berikut ini dibawah, jika sudah sesuai dengan yang ditulis maka akan muncul data yang akan dinginkan.  
You can check if the output file contains the appropriate information by using the following command:


::

    from extractreq.partof_modul1 import partOf
    myPart = partOf(inputData= 'dataset.xlsx', # dataset
                    dataStanford= 'stanford-corenlp-4.0.0',  #diambil dari https://stanfordnlp.github.io/CoreNLP/download.html
                    urlStanford= 'http://corenlp.run/')
    myPart.preprocessing() # data ini digunakan untuk melakukan preprocessing berupa list dataset yang digunakan
    myPart.fulldataset(inputData= '2005 - Grid 3D') # command ini digunakan untuk melihat dataset secara spesifik
    myPart.parsing(data) # dilakukan parsing data
    myPart.stanfordPostag(data) # dilakukan untuk mendapatkan data yang diinginakn.
