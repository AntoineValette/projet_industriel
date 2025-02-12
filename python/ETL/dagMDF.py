#!/usr/bin/env python3

# name : dagMDF.py
# author :
# version :
# desc : python script to transform raw data to a time serie data frame

import time
import pandas as pd
import matplotlib.pyplot as plt
from python.core import Settings

class DagMDF:

    def extract(self):
        print(time.time(),' - Extracting DagMDF')


    def transform(self):
        print(time.time(),' - Transforming DagMDF')

    def load(self):
        print(time.time(),' - Loading DagMDF')


if __name__ == "__main__":
    print(time.time(),' - debut du script')
    dagMDF = DagMDF()
    dagMDF.extract()
    dagMDF.transform()
    dagMDF.load()
