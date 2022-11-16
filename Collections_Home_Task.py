# importing random in order to generate random numbers
import random

# generate  and print random number of dicts
nr = random.randrange(2, 10, 1)
print(' number of dicts : ' + str(nr))

# generate empty list
lst = []

# generate and print random number of keys in dicts
nrk = random.randrange(1, 26, 1)
print(' number of keys in a dict: ' + str(nrk))

# generating nr number of dicts via loop
for j in range(nr):

    # dict variable to store dictionary
    d = {}

    # loop until each dict has the assigned random number of keys ( nrk ), using while because if same key repeats than it will be updated
    while len(d) < nrk:

        # generate random letter of dict key
        k = chr(random.randrange(97, 97 + 26))
        # generate random number 0-100 for dict value
        n = random.randrange(0, 100, 1)
        # 'making'( or producing... i don't know ) key - value pair
        d[k] = n

    print(' dict is ')
    print(d)
    # appending dict to list
    lst.append(d)
print("original list is ")
print(lst)

# merged dict variable
d_merged = {}
# looping through dicts in list
for i in range(len(lst)):
    # looping through keys in dict
    for j in lst[i]:
        # if key is duplicate then delete duplicate key and add new key value pair where key is transformed per requirement and value is max value
        if j in d_merged:
            if int(d_merged[j[:1]]) < lst[i][j]:
                del d_merged[j]
                d_merged[j+str(i+1)] = str(lst[i][j])

        # if key is not duplicate then insert value
        else:
            d_merged[j] = lst[i][j]

# printing merged list
print('dict merged')
print(d_merged)
