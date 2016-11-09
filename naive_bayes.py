from os import walk
from os import path

def get_files_in_dir(dir):
    files = []
    for (d, dirs, file_names) in walk(dir):
        files = [(d + "\\" + f) for f in file_names]
    return files

legit_msg = 'legit'
spam_msg = 'spmsg'

def parse_file(filename):

    label = legit_msg if legit_msg in filename else spam_msg
    subject = []
    body = []
    file = open(filename)
    for line in file:
        print(line)
        if "Subject" in line:
            #print(line)
            subject = [int(s) for s in (line.split()) if s.isdigit()]
        elif not line.isspace():
            [body.append(int(s)) for s in (line.split()) if s.isdigit()]

    return label, subject, body
files = []
for i in range(1, 11):
    files.append(get_files_in_dir("pu1\\part" + str(i)))
#print (files[0])
#print(parse_file(files[0][4]))

label, subject, body = parse_file(files[0][0])
