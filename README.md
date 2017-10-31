whatlang
=========

Lightning Fast Language Prediction :rocket:

Dependencies
=============

The below dependencies must be installed.

```
$ pip install future==0.16.0
$ pip install Cython==0.27.2
$ pip install cysignals==1.6.5
$ pip install pyfasttext==0.4.3
```

Install
=======

```
$ pip install whatlang
```


Basic Usage
============

Predicting Language using ``whatlang``

```python
>>> from whatlang import WhatLang
>>> wl = WhatLang()
>>> wl.predict_lang("Mother")
'en'
>>> wl.predict_lang(u"தாய்")
'ta'
>>> wl.predict_lang(u"അമ്മ")
'ml'
```

Batch Prediction is also supported

```python
>>>wl.predict_lang(["English sentence",u"അമ്മ"])
['en','ml']
```


Supported Language
==================

Supports 176 languages . The ISO codes for the corresponding languages are as below.

```
af als am an ar arz as ast av az azb ba bar bcl be bg bh bn bo bpy br bs bxr ca cbk
ce ceb ckb co cs cv cy da de diq dsb dty dv el eml en eo es et eu fa fi fr frr fy ga
gd gl gn gom gu gv he hi hif hr hsb ht hu hy ia id ie ilo io is it ja jbo jv ka kk km
kn ko krc ku kv kw ky la lb lez li lmo lo lrc lt lv mai mg mhr min mk ml mn mr mrj ms
mt mwl my myv mzn nah nap nds ne new nl nn no oc or os pa pam pfl pl pms pnb ps pt qu
rm ro ru rue sa sah sc scn sco sd sh si sk sl so sq sr su sv sw ta te tg th tk tl tr
tt tyv ug uk ur uz vec vep vi vls vo wa war wuu xal xmf yi yo yue zh
```

Reference
==========

``whatlang`` is powered by ``FastText``

### Enriching Word Vectors with Subword Information

[1] P. Bojanowski\*, E. Grave\*, A. Joulin, T. Mikolov, [*Enriching Word Vectors with Subword Information*](https://arxiv.org/abs/1607.04606)

```
@article{bojanowski2016enriching,
  title={Enriching Word Vectors with Subword Information},
  author={Bojanowski, Piotr and Grave, Edouard and Joulin, Armand and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.04606},
  year={2016}
}
```

### Bag of Tricks for Efficient Text Classification

[2] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, [*Bag of Tricks for Efficient Text Classification*](https://arxiv.org/abs/1607.01759)

```
@article{joulin2016bag,
  title={Bag of Tricks for Efficient Text Classification},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.01759},
  year={2016}
}
```

### FastText.zip: Compressing text classification models

[3] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, [*FastText.zip: Compressing text classification models*](https://arxiv.org/abs/1612.03651)

```
@article{joulin2016fasttext,
  title={FastText.zip: Compressing text classification models},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Douze, Matthijs and J{\'e}gou, H{\'e}rve and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1612.03651},
  year={2016}
}
```
