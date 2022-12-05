{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww13480\viewh17440\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # --------------------------------------------------------\
# Fast R-CNN\
# Copyright (c) 2015 Microsoft\
# Licensed under The MIT License [see LICENSE for details]\
# Written by Ross Girshick\
# --------------------------------------------------------\
\
import time\
\
\
class Timer(object):\
    """A simple timer."""\
    def __init__(self):\
        self.total_time = 0.\
        self.calls = 0\
        self.start_time = 0.\
        self.diff = 0.\
        self.average_time = 0.\
\
        self.duration = 0.\
\
    def tic(self):\
        # using time.time instead of time.clock because time time.clock\
        # does not normalize for multithreading\
        self.start_time = time.time()\
\
    def toc(self, average=True):\
        self.diff = time.time() - self.start_time\
        self.total_time += self.diff\
        self.calls += 1\
        self.average_time = self.total_time / self.calls\
        if average:\
            self.duration = self.average_time\
        else:\
            self.duration = self.diff\
        return self.duration\
\
    def clear(self):\
        self.total_time = 0.\
        self.calls = 0\
        self.start_time = 0.\
        self.diff = 0.\
        self.average_time = 0.\
        self.duration = 0.}