import os
from time import sleep
file = open('Modules.txt', 'r')
fileline = file.readlines()
file.close()

def install():

    for line in fileline:
        line = line.replace('\n', '')
        try:
            os.system(f'pip install {line}')
            #print(f'pip install {line}')
        except:
            print(f'{line} was not installed properly!')
