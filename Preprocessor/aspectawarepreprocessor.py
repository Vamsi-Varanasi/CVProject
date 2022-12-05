{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww14080\viewh17440\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # necessary packages\
import cv2\
import imutils\
\
\
class AspectAwarePreprocessor:\
    def __init__(self, width, height, inter=cv2.INTER_AREA):\
        # store the target image width, height, and interpolation\
        self.width = width\
        self.height = height\
        self.inter = inter\
\
    def preprocess(self, image):\
        # grab the dimensions of the image and then initialize\
        # the deltas to use when cropping\
        (h, w) = image.shape[:2]\
        dW, dH = 0, 0\
\
        # crop\
        if w < h:\
            image = imutils.resize(image, width=self.width, inter=self.inter)\
            dH = int((image.shape[0] - self.height) / 2.0)\
        else:\
            image = imutils.resize(image, height=self.height, inter=self.inter)\
            dW = int((image.shape[1] - self.width) / 2.0)\
\
        (h, w) = image.shape[:2]\
        image = image[dH:h - dH, dW:w - dW]\
\
        return cv2.resize(image, (self.width, self.height),\
                          interpolation=self.inter)}