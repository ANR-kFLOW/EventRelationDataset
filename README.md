# EventRelationDataset
Data and scripts for building a dataset of relation between events from texts covering different types of relations: (Causality, Enabling, Prevention, Intention, Not causality).
##Datasets 
the new generated datasets with RLINKS are found in The Datasets Folder, in TimeMl format.
- TB: Generated files from Timebank 1.2
- EventCausality data: Generated files from EventCausality Dataset 

##scripts
scripts are provided in Jupyter Notebooks, in which all required function to run the whole code are in the same file.
- Get_relation_tml_*.ipynb: to extract relations from datasets and save them in CSV files (Raw data without annotation).
- generate LINKS.ipynb: extract all pairs of events and the relation between them from CSV annotated files.

