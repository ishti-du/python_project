from string import punctuation

with open('From_Wikipedia_About_Python.txt') as file_object:
    lines = file_object.readlines()

my_set = {}

for line in lines:
    line = line.strip()
    line = line.replace('-', ' ')
    line = ''.join(c for c in line if c not in punctuation)
    for word in line.split():
        word = word.lower()
        if word.isdigit():
            continue
        if word in my_set.keys():
            my_set[word] = my_set[word] + 1
        else:
            my_set[word] = 1

with open('writing_text.txt', 'a') as writeObj:
    for k in sorted(my_set.keys()):
        writeObj.write('\n' + k + ' - ' + str(my_set[k]))
