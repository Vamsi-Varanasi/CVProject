{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww14080\viewh17440\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # -*- coding: utf-8 -*-\
import cv2\
import pickle\
import argparse\
import progressbar\
import numpy as np\
from scripts import Extractor\
from scripts import Retrievor\
from preprocessors import AspectAwarePreprocessor\
from preprocessors import ImageToArrayPreprocessor\
\
\
# initialize process\
aap = AspectAwarePreprocessor(224, 224)\
\
image = cv2.imread('./data/test/105239817.jpg')\
image = aap.preprocess(image)\
\
extractor = Extractor("autoencoder")\
retrievor = Retrievor('./features/autoencoder_features.pck')\
\
features = extractor.extract(image)\
\
distance = retrievor.search(features, depth=5)\
print(distance)}