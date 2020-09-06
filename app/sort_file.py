#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 01:07:08 2020

@author: breyneroc
"""

import pandas as pd
import sys

infname = sys.argv[1]
outfname = sys.argv[2]
sortby = sys.argv[3]

df = pd.read_csv(infname)
df.sort_values(inplace=True)
df.to_csv(outfname,index=False)