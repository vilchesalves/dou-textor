import textract
import os.path
from io import open
from random import randint

def load_file ():
    script_folder = os.path.dirname(os.path.realpath(__file__))

    file_name = 'DOU1_20180315'
    txt_path = '{}/txt/{}.txt'.format(script_folder, file_name)

    if os.path.exists(txt_path):
        fh = open(txt_path, encoding="utf-8")
    else:
        extracted_text = textract.process('./dou/{}.pdf'.format(file_name))
        fh = open(txt_path, 'w')
        fh.write(extracted_text)
    
    file_content = fh.read()
    
    return file_content

def load_random_substring (string, length):
    start = randint(0, len(string) - length)
    end = start + length

    return string[start:end]
