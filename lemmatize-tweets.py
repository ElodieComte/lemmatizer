#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:17:04 2019

@author: elodiecomte
"""

import lettria
import pickle

client = lettria.Client(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWxwaGEiLCJ1c2VySWQiOiI1Y2MwMDg3ZDA4YmEyYzJhMTNkNDE4N2YiLCJjcmVhdGVkQXQiOjE1NTYwOTg4NjA2NDcsImlhdCI6MTU1NjA5ODg2MCwiZXhwIjoxNTgwMjkwODYwfQ.2sMCPFepFk9FwJzLgOxZnn9ob1IvrAw4kaE1LQAI_NU"
)

file = open("clean_tweets_doc.tsv", "r")
list_dico = []

for line in file:
    data = client.request(line, raw=False)

    def getPostagger(sentence):
        out = sentence.nlp.data
        for elem in out:
            dico = {}
            for key, value in elem.items():
                test = elem["lemmatizer"]
                if type(test) == dict:
                    for key, value in test.items():
                        if key == "lemma":
                            dico[key] = value
                else:
                    for obj in value:
                        if type(obj) == dict:
                            for key, value in obj.items():
                                if key == "infinit":
                                    dico[key] = value
                for key, value in elem.items():
                    if key == "source":
                        dico[key] = value
                    if key == "tag":
                        dico[key] = value
            list_dico.append(dico)

    data.map(getPostagger)

pickle.dump(list_dico, open("lemmatized_tweets_doc.tsv", "wb"))
file.close()
