import pandas as pd
import re

parsed = []
unparsed = []
lines = []

with open('../dates.txt') as file:
    for line in file:
        lines.append(line)

regs = [
    re.compile('(?P<year>[0-9]{4})'),
    # re.compile('([0-9]{2})\/([0-9]{2})\/([0-9]{4})'),
]

def match_to_regs (line, regs):
    for reg in regs:
        match = reg.match(line)
        if match:
            return match
    
    return line


lines = map(lambda line: match_to_regs(line, regs), lines)
# df = pd.Series(doc)

print(lines)

print({
    'lines': len(lines),
    'parsed': len(parsed),
    'unparsed': len(unparsed),
})
