# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:18:22 2018

@author: zouco
"""
import csv

# create a txt file
with open('material/abc.txt','w') as f:
    for i in range(10):
        f.write('this is {} line\n'.format(str(i)))
    

# creat a csv file
with open('material/abc.csv','w') as f:
    writer = csv.writer(f)
    writer.write('header 1, header 2, header 3\n')
    for i in range(10):
        writer.writerow([i,i*10,i*100])

# creat a json file
import json
with open('material/a_json_file.txt','w') as f:
    d = {'first':1, 'second':2, 'third': 3}
    json.dump(d,f)
    
    