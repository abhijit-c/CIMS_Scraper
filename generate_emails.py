import html
import json
import os
import pprint
import re
import sys

def strip_htmltags(txt):
    return re.sub('<[^<]+?>', '', txt)

if len(sys.argv) == 1:
    print('Supply as cmdline argument /path/to/file.json')
json_path = sys.argv[1]

with open(json_path, 'r') as f:
    data = json.load(f)

num_people = len(data)

failed_read = []

is_profiles_generated = os.path.isdir('profiles')
for k in range(num_people):
    URL = data[k]['URL']
    basename = os.path.basename(URL)

    if not is_profiles_generated:
        os.system('wget -P ./profiles/ ' + URL) 
    if basename == '':
        failed_read.append(data[k]['Name'])
        continue

    with open('./profiles/' + basename, 'r') as f:
        prof = [line.strip() for line in f]
        coded_email = [x for x in prof if '&#' in x]
        if len(coded_email) != 0:
            print(
                    strip_htmltags(
                        html.unescape(
                            strip_htmltags(coded_email[0])
                        ).strip()
                    )
                )
        else: #maybe uncoded
            email = [x for x in prof if '@' in x][0]
            print(strip_htmltags(email))

print('Failed to automatically read the following profiles:')
pprint.pprint(failed_read)
