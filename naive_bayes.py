from os import walk
from collections import Counter
import math
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

    w = []
    for i in range(0, len(train_data)):
        w.extend(train_data[i][2])

    print("all words in all docs:", len(w))
    v = len(Counter(w).keys())  # amount of unique values
    print("v =", v)

    lc = []
    dc = []
    w_legit = []
    tmp_count = 0
    for i in range(0, len(train_data)):
        if legit_msg in train_data[i][0]:
            w_legit.extend(train_data[i][2])
            tmp_count += 1
    lc.append(len(w_legit))
    dc.append(tmp_count)
    w_spam = []
    tmp_count = 0
    for i in range(0, len(train_data)):
        if spam_msg in train_data[i][0]:
            w_spam.extend(train_data[i][2])
            tmp_count += 1
    lc.append(len(w_spam))
    dc.append(tmp_count)
    print("lc =", lc)
    print("dc =", dc)

    #get all words from test
    q = []
    for i in range(0, len(test_data)):
        q.extend(test_data[i][2])
    print("all words in train doc:", len(q))

    result = []
    for i in range(0, len(test_data)):
        legit_exp = math.log(dc[0] / d)
        spam_exp = math.log(dc[1] / d)
        #print(len(test_data[i][2]))
        for word in test_data[i][2]:
            #print(w_spam[word])
            legit_exp += math.log((w_legit[word] + 1) / (v + lc[0]))
            spam_exp += math.log((w_spam[word] + 1) / (v + lc[1]))
        if (legit_exp > spam_exp):
            result.append(legit_msg)
        else:
            result.append(spam_msg)

    return result


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
    res = classify(train, test, 2)

    base_check = []
    for j in range(0, len(test)):
        if res[j] in train[j]:
            base_check.append(1)
        else:
            base_check.append(0)

    print(base_check)