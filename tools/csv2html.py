# -*- coding: utf-8 -*-

import csv
def csv2html(path):
    with open(path, 'r') as d:
        csv_data = csv.reader(d)
        
        html_output = '<table>'
        for row in csv_data:
            html_output += '<tr>'
            for item in row:
                html_output += '<td>{}</td>\n'.format(item)
            html_output += '</tr>\n'
        html_output += '</table>\n'
    
    save_path = os.path.splitext(path)[0]+'.html'
    
    with open(save_path,'w') as f:
        f.write(html_output)
        
    return html_output

import os
path = os.path.join(os.path.split(os.getcwd())[0],'material/abc.csv')
csv2html(path)     
