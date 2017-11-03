from pyfasttext import FastText
from os import path
from __future__ import unicode_literals
import re

MODEL_FILE = path.join(path.dirname(__file__), 'model', 'lid.176.ftz')

class WhatTheLang(object):
    def __init__(self):
        self.model_file = MODEL_FILE
        self.model = self.load_model()
        self.unknown = "CANT_PREDICT"

    def load_model(self):
        return FastText(self.model_file)

    def _clean_up(self,txt):
        txt = re.sub(r"\b\d+\b", "", txt)
        return txt

    def _flatten(self,pred):
        return [item[0] if len(item)!=0 else self.unknown for item in pred]


    def _get_langs(self):
        return self.model.labels


    def predict_lang(self,inp):
        if type(inp) != list:
            cleaned_txt = self._clean_up(inp)
            if cleaned_txt == "":
                raise ValueError("Not enough text to predict language")
            pred = self.model.predict([cleaned_txt])[0]
            if len(pred) == 0:
                return self.unknown
            return pred[0]
        else:
            batch = [self._clean_up(i) for i in inp]
            return self._flatten(self.model.predict(batch))


    def pred_prob(self,inp):
        if type(inp) == str:
            inp = self._clean_up(inp)
            return self.model.predict_proba([inp])
        return self.model.predict_proba(inp)



