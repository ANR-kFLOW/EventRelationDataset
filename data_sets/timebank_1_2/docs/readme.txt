1. Publication title
--------------------

TimeBank 1.2


2. Authors
----------

James Pustejovsky (jamesp@cs.brandeis.edu)
Marc Verhagen (marc@cs.brandeis.edu)
Roser Sauri (roser@cs.brandeis.edu)
Jessica Littman (jlittman@cs.brandeis.edu)
Robert Gaizauskas (r.gaizauskas@dcs.shef.ac.uk)
Graham Katz (gkatz@uos.de)
Inderjeet Mani (imani@mitre.org)
Robert Knippen (knippen@cs.brandeis.edu)
Andrea Setzer (A.Setzer@dcs.shef.ac.uk)

Contact email address: timebank@timeml.org


3. Data type
------------

Text.


4. Data sources
---------------

Transcribed broadcast reports from ABC, CNN, PRI, and VOA, and
newswire articles from AP and NYT, collected for the Automatic Content
Extraction (ACE) program.

Articles from the Wall Street Journal, collected for the PropBank
program.


5. Project
----------

TERQAS: definition of TimeML markup language and initiation of corpus
to illustrate TimeML.

TANGO: further development of corpus and creation of annotation tool.

TARSQI: further development of corpus and creation of automatic
tagging software.


6. Applications
---------------

- natural language processing
- temporal parsing
- machine learning


7. Language
-----------

US English


8. Special License
------------------

None.


9. Grant number and funding agency 
----------------------------------

Creation of TiemBank was partially funded under ARDA grant number
NBCHC040027.


10. Copyright
-------------

The annotations in this data collection are copyrighted by Brandeis
University. User acknowledges and agrees that: (i) as between User and
Brandeis University, Brandeis University owns all the right, title and
interest in the Annotated Content, unless expressly stated otherwise;
(ii) nothing in this Agreement shall confer in User any right of
ownership in the Annotated Content; and (iii) User is granted a
non-exclusive, royalty free, worldwide license (with no right to
sublicense) to use the Annotated Content solely for academic and
research purposes. This Agreement is governed by the law of the
Commonwealth of Massachusetts and User agrees to submit to the
exclusive jurisdiction of the Massachusetts courts.

Note: The textual news documents annotated in this corpus have been
collected from a wide range of sources and are not copyrighted by
Brandeis University. The user acknowledges that the use of these news
documents is restricted to research and/or academic purposes only.


11. Description of corpus structure and data attributes
-------------------------------------------------------


timebank_1.2/doc/

	This readme.txt file as well as a more prozaic version in
	timebank.html. Also includes the TimeML specifications and
	guidelines.

timebank_1.2/validation/

	Contains the XML schema and DTD as well as the Perl script and
	Java class used for validation of TimeBank.

timebank_1.2/files/timeml/

	Contains the 183 annotated documents with TimeML tags only.

timebank_1.2/data/extra/

	Contains the 183 annotated documents with TimeML tags and some
	extra tags like sentence markers, document-level tags and some
	entity tags.

The size of the corpus is approximately 3Mb, it contains 61,000 tokens
(excluding punctuation). 

See timebank.html in this distribution for a description of TimeML
tags as well as some statistics. See "http://timeml.org" for the
latest on TimeML.


12. Quality control
-------------------

TimeBank 1.2 has been validated against version 1.2.1 of the Document
Type Definition and XML Schema. Validity checking against the DTD was
performed using the Perl XML::Checker::Parser module, available as
part of XML-Checker-0.13 from www.cpan.org. The XML schema were
applied using the Xerces Java Parser, version 1.4.4, available at
xerces.apache.org. 

Please refer to the readme file in the dtd directory for more
information.




