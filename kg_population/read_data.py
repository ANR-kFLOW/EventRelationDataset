import pandas as pd
import os

def read_file(path):
    if 'hong' in path:

        file=pd.read_csv(path, sep='\t')
    else:
        file = pd.read_csv(path)
    file.columns = ['pos1', 'trigger1', 'type1', 'sentence1', 'pos2', 'trigger2', 'type2', 'sentence2',
                    'id'] if 'onto' in path else ['trigger1', 'id1', 'trigger2', 'id2', 'rel', 'sentence',
                                                  'docid'] if 'Catena' in path else ['Unnamed: 0.1', 'Unnamed: 0',
                                                                                     'evnt1id', 'evnt1text', 'trigger1',
                                                                                     'evnt2id', 'evnt2text', 'trigger2',
                                                                                     'docname', 'rel1', 'rel2',
                                                                                     'rel3'] if 'hong' in path else [
                                                                                     'Unnamed: 0', 'trigger1', 'eid1', 'trigger2', 'eid2', 'signal',
                                                                                         'annotation', 'Doc name', 'Doc ID', 'sentence']

    return file


def get_events(row):
    event1 = row['trigger1']
    event2 = row['trigger2']
    return event1, event2

def get_relation(path,row):
    rel = [row['rel1'], row['rel2'], row['rel3']] if 'hong' in path else [row['rel']] if 'Catena' in path else [os.path.basename(path)[:-4]]
    return rel

def get_sentence(path,row):
    sent=(row['sentence1'] )+ "[ ...]"+row['sentence2']  if 'onto' in path else row["evnt1text"] + '[...]' + row["evnt1text"] if 'hong' in path else row['sentence']
    return sent
file = read_file('/Users/youssrarebboud/mapped_data_hong.csv')
#for idx, row in file.iterrows():
    #print(get_events(row))

import os
folder=['well aligned rows Timebank','well alligned eventCausality']
bases=['/Users/youssrarebboud/Documents/GitHub/EventRelationDataset/annotation_csv/','/Users/youssrarebboud/Desktop/PhD/ontoED']
paths=[]


for base in bases  :

      for f in folder:
          if 'onto' in base :
              f=''


          for dd in os.listdir(base + f):
            paths.append(base + f +'/'+ dd)
paths.append('/Users/youssrarebboud/Desktop/PhD/Extracted relations/Catena Timelink.csv')

