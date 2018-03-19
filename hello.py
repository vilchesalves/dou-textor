# -*- coding: utf-8 -*-

import re
from util import load_random_substring, load_file

random_file_content = load_random_substring(load_file(), 5000)

lines = random_file_content.split('\n')[1:-1]
words = re.compile(r'\s').split(random_file_content)

print([(len(w), w) for w in words])
