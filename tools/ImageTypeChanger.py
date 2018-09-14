# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:53:03 2018

@author: zouco
"""

from PIL import Image
from glob import glob
import os

def image2webp(inputFile):
    try:
        image = Image.open(inputFile)
        if image.mode != 'RGBA' and image.mode != 'RGB':
            image = image.convert('RGBA')

        outputFile = os.getcwd() + "/output" + "/" + inputFile[0:inputFile.index('.')] + ".webp"
        image.save(outputFile, 'WEBP')
        print(inputFile + ' has converted to ' + outputFile)
    except Exception as e:
        print('Error: ' + inputFile + ' converte failed to ' + outputFile)

matchFileList = glob('*.png')
if len(matchFileList) <= 0:
    print("There are no *.png file in this directory (you can run this script in your *png directory)!")
    exit(-1)

outputDir = os.getcwd() + "/output"    
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for pngFile in matchFileList:
    fileName = pngFile[0:pngFile.index('.')]
    image2webp(pngFile)

print("Converted done! all webp file in the output directory!")