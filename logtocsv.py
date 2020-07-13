import csv
import re

log_file_name = "access_logcess_log"
csv_file_name = "parsed_log.csv"

parts = [
    r'(?P<host>\S+)',                   # host %h
    r'\S+',                             # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<agent>.*)"',                 # user agent "%{User-agent}i"
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

file = open(log_file_name)

with open(csv_file_name, 'w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['Host', 'User', 'Time', 'Request', 'Status', 'Data_Size', 'Page_Name', 'User_agent'])

    for line in file:
        m = pattern.match(line)
        result = m.groups()
        csv_out.writerow(result)
