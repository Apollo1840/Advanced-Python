# -*- coding: utf-8 -*-

# txt file

# create and write
with open('material/abc.txt', 'w') as f:
    for i in range(10):
        f.write('this is {} line\n'.format(str(i)))

# read    
with open('material/abc.txt', 'r') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')

# --------------------------------------------------------------------
import csv

# creat a csv file
with open('material/abc.csv', 'w') as f:
    writer = csv.writer(f)
    writer.write('header 1, header 2, header 3\n')
    for i in range(10):
        writer.writerow([i, i * 10, i * 100])

# --------------------------------------------------------------------
# JSON 
# creat a json file
import json

d = {'first': 1, 'second': 2, 'third': 3}

# .json_file  <--->  dictionary  <---> Json_string

# create and write
with open('material/a_json_file.json', 'w') as f:
    json.dump(d, f)

# read a json
with open('... .txt', 'r', encoding='utf-8') as f:
    a_dict = json.load(f)

# json is readable, want to see what is it look like in Json by dict?
a_string_of_json_file = json.dumps(a_dict, ensure_ascii=False, sort_keys=True,
                                   indent=4)  # this will output a json_file_string
# json.dumps can also be used as a method to show dictionary

# if you got json text, you can also change it to a dict
dikt = json.loads(a_string_of_json_file)  # this will output a dict

# --------------------------------------------------------------------   
# pickle (more flexible than json, but json is human readable)
import pickle

d = {'first': 1, 'second': 2, 'third': 3}

# create and write
with open('material/a_json_file.pkl', 'w') as f:
    pickle.dump(d, f)

# read a json
with open('... .pkl', 'r') as f:
    a_dict = pickle.load(f)

'''
    txt
    csv
    json
    pkl
'''

# --------------------------------------------------------------------


# logging
import logging

logging.basicConfig(filename='material/logger01.log')

logger1 = logging.getLogger()
logger1.info('you can not see this line !')

# go to material/logger01.log, you will find nothing in log file, why?

print(logger1.level)

# levels : debug, Info, warning, error, critical
import logging

logging.basicConfig(filename='material/logger02.log', level=logging.DEBUG)

logger2 = logging.getLogger()
logger2.info('you can see this line ! ')
logger2.warning('you can see this line 2 time! ')

# you will not see it either (even the logger02.log), because second time the basicConfig does not work.
# you need to restart the script

import logging

# you can even format each entry of log information

# where to find log_formats: https://docs.python.org/3/library/logging.html
log_format = '%(levelname)s %(asctime)s - %(message)s'

logging.basicConfig(filename='material/logger03.log',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filemode="w",  # rewrite everytime
                    level=logging.DEBUG,
                    format=log_format)

logger3 = logging.getLogger()
logger3.info('you can the see the asctime of this entry')

# really handle loging system in projects: https://www.youtube.com/watch?v=jxmzY9soFXg&ab_channel=CoreySchafer