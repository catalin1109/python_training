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


# function for generating nr number of dicts via loop, 3 arguments:1.number of dicts, 2.number of keys in dict, 3.list of dicts, and returning list of dicts
def generator(a, b, c):
    for j in range(a):

        # dict variable to store dictionary
        d = {}

        # loop until each dict has the assigned random number of keys ( nrk ), using while because if same key repeats than it will be updated
        while len(d) < b:

            # generate random letter of dict key
            k = chr(random.randrange(97, 97 + 26))
            # generate random number 0-100 for dict value
            n = random.randrange(0, 100, 1)
            # 'making'( or producing... i don't know ) key - value pair
            d[k] = n

        print(' dict is ')
        print(d)
        # appending dict to list
        c.append(d)
    print("original list is ")
    print(c)
    return c


# calling function generator to generate the list of dicts
generator(nr, nrk, lst)
# merged dict variable
d_merged = {}


# function to merge dicts in list, 1 arguments - list which has dicts, prints merged list
def merge(a):
    # looping through dicts in list
    for i in range(len(a)):
        # looping through keys in dict
        for j in a[i]:
            # if key is duplicate then delete duplicate key and add new key value pair where key is transformed per requirement and value is max value
            if j in d_merged:
                if int(d_merged[j[:1]]) < a[i][j]:
                    del d_merged[j]
                    d_merged[j+str(i+1)] = str(a[i][j])

            # if key is not duplicate then insert value
            else:
                d_merged[j] = a[i][j]

    # printing merged list
    print('dict merged')
    print(d_merged)


# calling function to merge dicts
merge(lst)
