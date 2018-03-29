import datetime
import random
import time
import os
import csv
from csv import reader
import argparse
from influxdb import client as influxdb


influx_ip = "10.0.0.10"
port = 8086
username = "centos"
password ="root"
database_name = "sensors_data"

db = influxdb.InfluxDBClient(influx_ip,port,username,password,database_name)


import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

import numpy as np
data=df.as_matrix()

for metric in data:
    influx_metric = [{
        'measurement': 'celcus',
        'time': metric[0],
        'fields': {
             'value': metric[1]
        }
    }]
    db.write_points(influx_metric)
