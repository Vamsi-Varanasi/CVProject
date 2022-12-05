{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww14080\viewh17440\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # -*- coding: utf-8 -*-\
import numpy as np\
\
\
def mean_reciprocal_rank(retrievals, labels):\
    rr = []\
    for (retrieval, label) in zip(retrievals, labels):\
        rank = 0\
        if label in retrieval:\
            rank = retrieval.index(label) + 1\
        rr.append(rank / len(retrieval))\
    return np.mean(rr)\
\
\
def rank1_accuracy(retrievals, labels):\
    first = []\
    for (retrieval, label) in zip(retrievals, labels):\
        if retrieval[0] == label:\
            first.append(1)\
        else:\
            first.append(0)\
    return np.mean(first)\
\
\
def mean_mean_average_precision(retrievals, labels):\
    precisions = []\
    for (retrieval, label) in zip(retrievals, labels):\
        precision, hit = [], 0\
        for i, name in enumerate(retrieval):\
            if name == label:\
                hit += 1\
                precision.append(hit / (i + 1))\
        if hit == 0:\
            precisions.append(0.)\
        else:\
            precisions.append(np.mean(precision))\
    return np.mean(precisions)}