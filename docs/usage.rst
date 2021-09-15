============
Installation
============

Install the package with pip::

    $ pip install extractreq

========
Usage
========

To use this template, simply update it::

	from extractreq.partof_modul1 import partOf
	myPart = partOf(inputData= 'dataset.xlsx', # dataset
			dataStanford= 'stanford-corenlp-4.0.0',  #diambil dari https://stanfordnlp.github.io/CoreNLP/download.html
			urlStanford= 'http://corenlp.run/')
	myPart.preprocessing()
	myPart.fulldataset(inputData= '2005 - Grid 3D')
	myPart.parsing(data)
	myPart.stanfordPostag(data)
