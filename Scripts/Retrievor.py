{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww6460\viewh17440\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # necessary packages\
import os\
import pickle\
import numpy as np\
from sklearn.metrics.pairwise import cosine_similarity\
from sklearn.metrics.pairwise import manhattan_distances\
from sklearn.metrics.pairwise import euclidean_distances\
\
\
class Retrievor:\
    def __init__(self, compressor):\
        if not os.path.isfile(compressor):\
            raise ValueError("File of features doesn't exist")\
        self.__load_compressor(compressor)\
\
    def __load_compressor(self, compressor):\
        with open(compressor, 'rb') as fp:\
            features = pickle.load(fp)\
        styles = [f[2] for f in features]\
        colors = [f[1] for f in features]\
        matrix = [f[0] for f in features]\
        self.matrix = np.array(matrix)\
        self.colors = np.array(colors)\
        self.styles = np.array(styles)\
\
    def compute_distance(self, vector, distance='cosinus'):\
        v = vector.reshape(1, -1)\
        if distance == 'cosinus':\
            return cosine_similarity(self.matrix, v)\
        elif distance == 'manhattan':\
            return manhattan_distances(self.matrix, v)\
        elif distance == 'euclidean':\
            return euclidean_distances(self.matrix, v)\
\
    def search(self, wanted, distance='cosinus', depth=1):\
        distances = self.compute_distance(wanted, distance).flatten()\
        nearest_ids = np.argsort(distances)[:depth].tolist()\
        return [\
            self.colors[nearest_ids].tolist(),\
            self.styles[nearest_ids].tolist(),\
            distances[nearest_ids].tolist()\
        ]}