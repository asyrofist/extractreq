Extraction Dependency Based on Evolutionary Requirement Using Natural Language Processing
=========================================================================================

Overview
------------

Secara garis besar, library ini dibuat untuk mengembangkan metode ekstraksi kebergantungan kebutuhan menggunakan pemrosesaan bahasa alamiah, yang telah diterangkan pada proceeding conference di  `ISRITI2021`_. Jika anda menggunakan library ini, saya sangat mengapresiasi, dengan cara mengirimkan segala macam bentuk kiriman melalui `courtesy`_  dan `scholar`_, Semoga data yang saya publikasikan, berguna untuk orang banyak, terima kasih. 

Abstrak
------------
Changes in requirements are one of the critical problems that occur during requirement specification. A change in a requirement could trigger changes in other requirements. Thus the identification process requirement to respond and correct the truth, realistic, require, specific, measurable aspects. Previous work has focused on building a model of interdependency between the requirements. This study proposes a method to identify dependencies among requirements. The dependency relations refer to evolutionary requirements. The technique uses natural language processing to extract dependency relations. This research analyzes how to obtain feature extractions by including the following: 1) Gathering requirements statement from the SRS document, 2) Identifying dependencies between requirements, 3) Developing interdependency extraction methods and, 4) Modeling of the interdependency requirement. The expectation of this experiment indicates the interdependency graph model. This graph defines the interdependency in the (Software Requirement Specification) SRS document. This method gathers interdependency between SRS document requirements such as PART OF, AND, OR, & XOR. Therefore, getting the feature extraction to identify the interdependency requirement will be useful for solving specified requirements changing.

.. _ISRITI2021: https://ieeexplore.ieee.org/document/9315489
.. _courtesy: https://www.researchgate.net/profile/Rakha_Asyrofi
.. _scholar: https://scholar.google.com/citations?user=WN9T5UUAAAAJ&hl=id&oi=ao

Dikembangkan oleh Rakha Asyrofi (c) 2021

Cara menginstall
--------------

installation using pypi:

    pip install extractreq

Fitur yang digunakan
------------
Berikut ini adalah beberapa fitur yang telah digunakan sebagai berikut:
- library ini dapat mengekstraksi kebergantungan kebutuhan
- Library ini dapat mencari relasi antar kebutuhan

Kontribusi
------------
Sebagai bahan pengemabangan saya, maka saya apresiasi apabila anda, dapat mengecek issue dari repository library ini.
- Issue Tracker: https://github.com/asyrofist/Extraction-Requirement/issues
- Source Code: https://github.com/asyrofist/Extraction-Requirement

Support
------------
Jika anda memiliki masalah, saat menggunakan library ini. Mohon dapat membuat mailing list ke at: asyrofi.19051@mhs.its.ac.id

Lisensi
------------
Proyek ini dapat lisensi atas MIT License
