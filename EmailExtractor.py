"""
python EmailExtractor.py
"""

import os
def load_txt_as_str(txt_filepath):
    with open(txt_filepath,'r') as fh:
        string = fh.read()
    return string

import re

def solve(line):
    
    """
    client@server.com
    client[at]server[dot]com
    client@server[dot]com
    client[at]server.com
    """
    regexold = '\S+(?:[at]|[dot]|@)\S'
    regex1 = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex2 = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    regex3 = '\S+@\S+'
    regex4 = '\S+@\S+\.\S+'
    regex4 = '(\S+(@|\[at\])\S+(\.|\[dot\])\S+)'
    emailMatch = re.findall(regex4, line)
    # emailMatch = sorted(emailMatch)
    MAILS = []
    for FullEmails in emailMatch:
        MAILS.append(FullEmails[0])
        
    return MAILS



line = "test@gmail.com <Subject>Testing <body>My email ID is heena.syed221997[at]hacker[dot]com heena.syed221997[at]hacker.com and my phone number is 9663508766. Also, Hello shubhamg199630@gmail.com is Mutiara Damansara:+60 (0)3 2723 7900</p> +6 (03) 8924 8000"

emailMatch = solve(line)
for email in emailMatch:
    print(email)
"""
if __name__ == '__main__':
    ROOT_DIR = os.getcwd()
    FilePath = os.path.join(ROOT_DIR,"Data","SampleJargon.txt")
    txt = load_txt_as_str(FilePath)
    print(txt)
"""

    