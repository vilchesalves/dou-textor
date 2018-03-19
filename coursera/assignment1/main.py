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

def match_to_regs (agg, curr):
    if type(agg) is not dict:
        agg = {
            'lines': [],
            'parsed': [],
            'unparsed': [],
        }
    agg['lines'].append(curr)
    return agg

# print(2, lines[:3])

# lines = map(lambda line: match_to_regs(line, regs), lines)
lines = reduce(match_to_regs, lines[:5])
# df = pd.Series(doc)

print(lines)

# print({
#     'lines': len(lines),
#     'parsed': len(parsed),
#     'unparsed': len(unparsed),
# })
