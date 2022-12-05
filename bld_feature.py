{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww14080\viewh18000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # -*- coding: utf-8 -*-\
import cv2\
import pickle\
import progressbar\
import numpy as np\
import pandas as pd\
from scripts import Extractor\
from preprocessors import AspectAwarePreprocessor\
from preprocessors import ImageToArrayPreprocessor\
\
# data\
data = pd.read_csv('./outputs/train.csv')\
# initialize process\
iap = ImageToArrayPreprocessor()\
aap = AspectAwarePreprocessor(224, 224)\
\
# loop over types\
types = [\
    'AKAZE', 'ORB', 'SURF',\
    'VGG16', 'VGG19', 'MobileNet',\
    'MobileNet'\
    'autoencoder'\
]\
\
# loop over images\
for dType in types:\
    print('[INFO]: Working with \{\} ...'.format(dType))\
    extractor = Extractor(dType)\
    db = []\
    widgets = [\
        "Extract features: ", progressbar.Percentage(), " ",\
        progressbar.Bar(), " ", progressbar.ETA()\
    ]\
    pbar = progressbar.ProgressBar(maxval=len(data), widgets=widgets).start()\
    for index, row in data.iterrows():\
        # preprocessing\
        image = cv2.imread(row.path)\
        image = aap.preprocess(image)\
        if dType in ['VGG16', 'VGG19', 'MobileNet', 'autoencoder']:\
            image = iap.preprocess(image)\
        features = extractor.extract(image)\
        if isinstance(features, np.ndarray):\
            db.append([features, row.color, row.type])\
        pbar.update(index)\
    pbar.finish()\
\
    with open('./features/' + dType + '_features.pck', 'wb') as fp:\
        pickle.dump(db, fp)\
    print('Extraction finish. DB saved.')}