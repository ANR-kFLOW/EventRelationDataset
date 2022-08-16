# This is a sample Python script.
import os

from  read_data import *
import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot
from declaration import *
from bindings import  *
from rdflib import Graph
from rdflib import Graph, Literal, RDF, URIRef
from rdflib import URIRef, SDO, PROV, DC, DCTERMS
from rdflib import URIRef, RDF, RDFS, TIME
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD
import uuid

out_folder = '/Users/youssrarebboud/Desktop/PhD'
g = Graph()
binding = {
"faro" :'http://purl.org/faro/',
"fabio" : 'http://purl.org/spar/fabio/',
"dc": DC,
"dcterms":  DCTERMS,
    'xmls': 'http://www.w3.org/2001/XMLSchema#',
    'prov': 'http://www.w3.org/ns/prov#'

}

for i in binding:
    bind(g,i,binding[i])
# create the provenance nodes for different datasets
hong_node = create_provenance_nodes(g,hong)
onto_node= create_provenance_nodes(g,OntoED)
timebank_node=create_provenance_nodes(g,timebank)
faro_node= create_provenance_nodes(g,faro)


#path='/Users/youssrarebboud/Documents/GitHub/EventRelationDataset/annotation_csv/well aligned rows Timebank/intends.csv'

for path in paths:
    #print(path)
    file = read_file(path)
    for index, row in file.iterrows():

        event1, event2 = get_events(row)

        rel = get_relation(path, row)


        # # provenance
        sent = get_sentence(path,row)

        prov_node = node_creation(sent, 'provenance')
        provenance= hong_node if 'hong' in path else onto_node if 'onto' in path else timebank_node if 'Catena' in path else faro_node
        g.add((prov_node, RDF.type, PROV.Activity))
        g.add((prov_node, PROV.used, provenance))
        g.add((prov_node, PROV.used, Literal(sent)))
        #
        for r in rel:
             if str(r).strip('2').strip().lower() not in relations:
                 continue  # relation not known

             if '2' in str(r):  # swap the event order
                temp = event1
                event1 = event2
                event2 = temp

             evt1 = node_creation(path, event1)
             evt2 = node_creation(path, event2)
             statement = add_relation(g,evt1, URIRef(relations[str(r).strip('2').strip().lower()]), evt2)
             gx=Graph()
             for i in binding:
                 bind(gx, i, binding[i])
             add_relation(gx,evt1, URIRef(relations[str(r).strip('2').strip().lower()]), evt2)
             #statement=wrap_statement(statement)
             gxt = gx.serialize(format='ttl').split(' .')[-2].strip()
             statement=Literal(f"<< {gxt} >>")
             add_label(g,evt1, event1)
             add_label(g,evt2, event2)
             add_type(g,evt1, 'condition' if 'enables' in r else 'event')
             add_type(g,evt2, 'event')

             add_provenance(g,statement, prov_node)



#Print the number of "triples" in the Graph
print(f"Graph g has {len(g)} statements.")


#Print out the entire Graph in the RDF Turtle format
grph= g.serialize(format="turtle")
out = grph.replace('"<<', '<<').replace('>>"', '>>')
with open(f"{out_folder}/KG.ttl", 'w') as outfile:
    outfile.write(out)
#visualize(g)
