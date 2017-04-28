# -*- coding: utf-8 -*-

from sumy._compat import to_unicode
from sumy.nlp.stemmers import Stemmer

def stem(word, LANGUAGE = "portuguese"):
    stemmer = Stemmer(LANGUAGE)
    return stemmer(to_unicode(word).lower())

print stem("declarações")