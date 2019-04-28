#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:30:03 2019

@author: elodiecomte
"""

import re
import codecs


file = codecs.open("tweets_corpus.txt", "r", "utf-8")
out = open("clean_tweets_corpus.tsv", "w")

regex_url = re.compile("(https://)[a-zA-Z0-9_\-\.\/]+")
regex_hashtag = re.compile("#[a-zA-Z0-9\_]+")
regex_aro = re.compile("@[a-zA-Z0-9\_]+")
regex_ponct = re.compile("[\.\,\;\:\)\!\(\?\…\-\_\^\=\/]")
regex_zero = re.compile("^(0)")


for line in file:

    if regex_url.search(line):
        modif_url = re.sub(regex_url, r"", line)
    else:
        modif_url = line

    if regex_hashtag.search(modif_url):
        modif_h = re.sub(regex_hashtag, r"", modif_url)
    else:
        modif_h = modif_url

    if regex_aro.search(modif_h):
        modif_aro = re.sub(regex_aro, r"", modif_h)
    else:
        modif_aro = modif_h

    if regex_ponct.search(modif_aro):
        modif_ponct = re.sub(regex_ponct, r"", modif_aro)
    else:
        modif_ponct = modif_aro

    if regex_zero.search(modif_ponct):
        modif_zero = re.sub(regex_zero, r"", modif_ponct)
    else:
        modif_zero = modif_ponct

    modif_final = modif_zero.lower()

    out.write(modif_final)

file.close()
out.close()
