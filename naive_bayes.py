from os import walk
from collections import Counter

def get_files_in_dir(dir):
    files = []
    for (d, dirs, file_names) in walk(dir):
        files = [(d + "\\" + f) for f in file_names]
    return files

legit_msg = "legit"
spam_msg = "spmsg"


def parse_file(filename):
    label = legit_msg if legit_msg in filename else spam_msg
    subject = []
    body = []
    file = open(filename)
    for line in file:
        #print(line)
        if "Subject" in line:
            #print(line)
            subject = [int(s) for s in (line.split()) if s.isdigit()]
        elif not line.isspace():
            [body.append(int(s)) for s in (line.split()) if s.isdigit()]

    return label, subject, body


def classify(train_data, test_data, class_amount):
    d = len(train_data)
    print ("d =", d)

    tmp = []
    for i in range(0, len(train_data)):
        tmp.extend(train_data[i][2])

    print("all words in all docs:", len(tmp))
    v = len(Counter(tmp).keys())  # amount of unique values
    print("v =", v)

    lc = []
    dc = []
    tmp = []
    tmp_count = 0
    for i in range(0, len(train_data)):
        if legit_msg in train_data[i][0]:
            tmp.extend(train_data[i][2])
            tmp_count += 1
    lc.append(len(tmp))
    dc.append(tmp_count)
    tmp = []
    tmp_count = 0
    for i in range(0, len(train_data)):
        if spam_msg in train_data[i][0]:
            tmp.extend(train_data[i][2])
            tmp_count += 1
    lc.append(len(tmp))
    dc.append(tmp_count)
    print("lc =", lc)
    print("dc =", dc)


files = []
for i in range(1, 11):
    files.append(get_files_in_dir("pu1\\part" + str(i)))


for i in range(0, 1):
    #cross-validation
    train = []
    test = []
    #generate data for test
    for j in range(0, len(files[i])) :
        label, subject, body = parse_file(files[i][j])
        test.append([label, subject, body])

    #generate data for train
    tmp_train = [files[f] for f in range(0, 10) if f != i]
    for j in range(0, len(tmp_train)):
        for k in range(0, len(tmp_train[j])):
            label, subject, body = parse_file(tmp_train[j][k])
            train.append([label, subject, body])
    classify(train, test, 2)
