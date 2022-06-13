# EventRelationDataset

Data and scripts for building a dataset of relation between events from texts, covering different types of relations: (Causality, Enabling, Prevention, Intention, Not causality).

## Dataset

The Event Relation dataset is released under the [TimeML format](http://timeml.org/), extending it with a new `RLINK` tag for expressing several type of relations, specified in the `relType` field in this way:

```xml
<RLINK eventInstanceID="ei264" lid="l42" relType="prevention" relatedEventInstance="ei268" />

```
It has been realised by re-annotating two existing datasets:
- [TimeBank 1.2](https://catalog.ldc.upenn.edu/LDC2006T08)
- The [EventCausality Dataset](https://github.com/CogComp/TCR)

## Outline of the repository

Scripts are provided in Jupyter Notebooks, in which all required function to run the whole code are in the same file.

- `datasets` includes the final dataset in TimeML format;
- `generation` includes the scripts for realising the dataset:
  - `Get_relation_*.ipynb`: to extract relations from datasets and save them in CSV files (Raw data without annotation) with different configurations for different datasets formats.
  - `generate LINKS.ipynb`: extract all pairs of events and the relation between them from CSV annotated files.
- `annotation_csv`: the csv files used during the annotation process
