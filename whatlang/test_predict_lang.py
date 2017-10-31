#coding=utf-8

from predict_lang import WhatLang
from os import path

class WhatLangTest():

    def __init__(self):
        self.model_file = path.join(path.dirname(__file__),'model','lid.176.ftz')
        self.wl = WhatLang()

    def test_model_present(self):
        assert path.isfile(self.model_file) == True

    def test_english(self):
        pred = self.wl.predict_lang("This is an English sentence")
        assert pred == 'en'

    def test_batch(self):
        pred = self.wl.predict_lang(["English sentence",u"അമ്മ"])
        assert pred == ['en','ml']

    def test_num_langs(self):
        assert len(self.wl._get_langs()) ==176

    def test_all(self):

        self.test_model_present()
        self.test_num_langs()
        self.test_english()
        self.test_batch()


if __name__ == "__main__":
    wlt = WhatLangTest()
    wlt.test_all()
