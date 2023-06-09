import pandas as pd
import numpy as np
import os
import gc
import copy
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta, date
import time
from dateutil.relativedelta import relativedelta 

import pyarrow.parquet as pq
import pyarrow as pa

from tqdm import tqdm

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

pd.options.display.float_format = '{:,.2f}'.format

import warnings
warnings.filterwarnings("ignore")
count = 0
counter = 0
unique_names = set()
train_file = "/home/goode/Desktop/elusa/tweets.jsonl"
with open(train_file, 'r') as file:
    for line in file:
        data = json.loads(line)

        name = data['tweet']['user']['username']
        
        #if count == 3:
        #    break
        if name is not None and name not in unique_names:
            unique_names.add(name)
            counter += 1
        count = count + 1
print(unique_names)
print(counter)

with open('users_2016.txt', 'w') as file:
    file.write(str(counter))