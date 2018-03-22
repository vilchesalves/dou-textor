from calendar import month_abbr
from functools import reduce
import pandas as pd
import re

parsed = []
unparsed = []
lines = []

with open('../dates.txt') as file:
    for line in file:
        lines.append(line)

regs = [
    re.compile(r'(?P<month>[0-9]{1,2})/?(?P<day>[0-9]{1,2})?/(?P<year>(19|20)?[0-9]{2}?)[^/]'),
    re.compile(r'(?P<month>[0-9]{1,2})-(?P<day>[0-9]{1,2})?-(?P<year>(19|20)?[0-9]{2}?)'),
    re.compile(r'(?P<day>[0-9]{2}) (?P<month>[a-zA-z]{3,8}) (?P<year>[0-9]{4})'),
    re.compile(r'(?P<month>(.(an[au]{2}ry|ebruary|arch|pril|ay|une|uly|ugust|eptember|ctober|ovember|eceme?ber)|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)))\.? ?(?P<day>[0-9]{1,2})?,? ?(?P<year>[0-9]{4})'),
    re.compile(r'(?P<year>[0-9]{4})'),
]

enumerate_months = {v: k for k,v in enumerate(month_abbr)}

def match_to_regs (agg, curr):
    global enumerate_months

    for reg in regs:
        match = reg.search(curr)
        
        if match:
            parsed = match.groupdict()
            
            # fill in empty indexes
            
            if (
                'day' not in match.groupdict()
                or parsed['day'] == None
            ):
                parsed['day'] = '1'
            
            if 'month' not in match.groupdict():
                parsed['month'] = '1'

            # transform months into indexes
            
            if (
                isinstance(parsed['month'], str)
                and len(parsed['month']) > 2
            ):
                month_index = enumerate_months[parsed['month'][:3]]
                parsed['month'] = str(month_index)
            
            # fill in incomplete numbers
            
            if len(parsed['day']) == 1:
                parsed['day'] = '0' + parsed['day']
            
            if len(parsed['month']) == 1:
                parsed['month'] = '0' + parsed['month']
            
            if len(parsed['year']) == 2:
                parsed['year'] = '19' + parsed['year']
                
            agg['parsed'].append(parsed)
            break
    else:
        agg['unparsed'].append(curr)

    return agg

lines = reduce(match_to_regs, lines, {
            'parsed': [],
            'unparsed': [],
        })

# sort data
df = pd.DataFrame(lines['parsed']).sort_values(['year', 'month', 'day'])

#  insert rank into original array
for rank, data in enumerate(df.iterrows()):
    lines['parsed'][data[0]]['rank'] = rank

#  return panda serie for the ranks
df = pd.DataFrame(lines['parsed'])['rank']

# not really returning, just printing
print(df)
