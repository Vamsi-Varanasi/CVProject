{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww14080\viewh17440\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # necessary packages\
from tensorflow.keras.preprocessing.image import img_to_array\
\
\
class ImageToArrayPreprocessor:\
    def __init__(self, dataFormat=None):\
        # store image\
        self.dataFormat = dataFormat\
\
    def preprocess(self, image):\
        return img_to_array(image, data_format=self.dataFormat)}