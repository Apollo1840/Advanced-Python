# -*- coding: utf-8 -*-
"""
@author: zouco
"""


# txt file

# create and write
with open('material/abc.txt','w') as f:
    for i in range(10):
        f.write('this is {} line\n'.format(str(i)))

# read    
with open('material/abc.txt','r') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')



# --------------------------------------------------------------------
import csv
# creat a csv file
with open('material/abc.csv','w') as f:
    writer = csv.writer(f)
    writer.write('header 1, header 2, header 3\n')
    for i in range(10):
        writer.writerow([i,i*10,i*100])



# --------------------------------------------------------------------
# JSON 
# creat a json file
import json

d = {'first':1, 'second':2, 'third': 3}

# create and write
with open('material/a_json_file.txt','w') as f:   
    json.dump(d,f)

# read a json
with open('... .txt','r',encoding = 'utf-8') as f:
    a_dict = json.load(f)
    

# json is readable, want to see what is it look like in Json by dict?
json.dumps(a_dict, ensure_ascii = False, sort_keys=True, indent=4) # this will output a json_file_string
# json.dumps can also be used as a method to show dictionary
   
# if you got json text, you can also change it to a dict
json.loads(a_string_of_json_file) # this will output a dict  
    


# --------------------------------------------------------------------   
# pickle (more flexible than json, but json is human readable)
import pickle

d = {'first':1, 'second':2, 'third': 3}

# create and write
with open('material/a_json_file.pkl','w') as f:   
    pickle.dump(d,f)

# read a json
with open('... .pkl','r') as f:
    a_dict = pickle.load(f)



