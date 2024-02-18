import pandas as pd
import spacy
from spacy import displacy
import requests
from bs4 import BeautifulSoup
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob

def remove_newlines(content):
    split_content = content.split("\n")
    non_zero_conetn = [value for value in split_content if value]
    clean_content = '. '.join(non_zero_conetn)
    return clean_content

def get_entities(content):
    pd.set_option("display.max_rows", 200)
    nlp = spacy.load("en_core_web_trf")
    nlp.add_pipe('spacytextblob')

    content = remove_newlines(content)
    doc = nlp(content)
    print(doc._.blob.polarity)
    print(doc._.blob.sentiment_assessments.assessments)

    entities = set()
    IGNORED_LABELS = ["TIME", "CARDINAL", "DATE", "ORDINAL", "NORP", "PERCENT"]
    for ent in doc.ents:
        if ent.label_ not in IGNORED_LABELS:
            print(ent.text, ent.start_char, ent.end_char, ent.label_, ent._.blob.sentiment_assessments.assessments)
            entities.add(ent.text)
    res = '"' + '":, "'.join(entities) + '"'
    print(res)
    return res
    # displacy.serve(doc, style="ent")

