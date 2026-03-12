import re
import json

filepath = 'c:/Users/rafae/Desktop/WebTech/docs/data/python-libs.json'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '"codigo": "' in line:
        prefix_idx = line.find('"codigo": "') + len('"codigo": "')
        suffix_idx = line.rfind('"')
        
        prefix = line[:prefix_idx]
        suffix = line[suffix_idx:]
        codigo_content = line[prefix_idx:suffix_idx]
        
        # Replace all double quotes with single quotes
        codigo_content = codigo_content.replace('\\"', "'").replace('"', "'")
        
        lines[i] = prefix + codigo_content + suffix

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        json.load(f)
    print('JSON válido')
except Exception as e:
    print('Error:', e)
