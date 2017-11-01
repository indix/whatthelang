#coding=utf-8

from predict_lang import WhatTheLang
from os import path

class WhatTheLangTest():

    def __init__(self):
        self.model_file = path.join(path.dirname(__file__),'model','lid.176.ftz')
        self.wtl = WhatTheLang()

    def test_model_present(self):
        assert path.isfile(self.model_file) == True

    def test_english(self):
        pred = self.wtl.predict_lang("This is an English sentence")
        assert pred == 'en'

    def test_batch(self):
        pred = self.wtl.predict_lang(["English sentence",u"അമ്മ"])
        assert pred == ['en','ml']

    def test_num_langs(self):
        assert len(self.wtl._get_langs()) ==176

    def test_all(self):

        self.test_model_present()
        self.test_num_langs()
        self.test_english()
        self.test_batch()


if __name__ == "__main__":
    wtlt = WhatTheLangTest()
    wlt.test_all()
