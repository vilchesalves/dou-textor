import pandas as pd
import re

parsed = []
unparsed = []
lines = []

with open('../dates.txt') as file:
    for line in file:
        lines.append(line)

regs = [
    re.compile(r'(?P<month>[0-9]{1,2})[/-](?P<day>[0-9]{1,2})?[/-]?(?P<year>(19|20)?[0-9]{2}?)'),
    re.compile(r'(?P<day>[0-9]{2}) (?P<month>[a-zA-z]{3,8}) (?P<year>[0-9]{4})'),
    re.compile(r'(?P<month>[a-zA-Z]{3,8})\.? ?(?P<day>[0-9]{1,2})?,? ?(?P<year>[0-9]{4})'),
    re.compile(r'(?P<year>[0-9]{4})'),
]

i = 0

def match_to_regs (agg, curr):
    if type(agg) is not dict:
        agg = match_to_regs({
            'parsed': [],
            'unparsed': [],
        }, agg)
    
    for reg in regs:
        match = reg.search(curr)
        
        if match:
            agg['parsed'].append(match.groupdict())
            break
    else:
        agg['unparsed'].append(curr)

    return agg

lines = reduce(match_to_regs, lines)
# df = pd.Series(doc)

print({
    'parsed': len(lines['parsed']),
    'unparsed': len(lines['unparsed']),
})

for date in lines['parsed']:
    print(date)
