# importing random in order to generate random numbers
import random

# Create an empty list
lst = []

# loop through 100 iteration
for i in range(100):
    # Append random number in each iteration
    lst.append(random.randrange(1, 100, 1))

# printing original list
print("original list is")
print(lst)

# repeating loop 100(number of elements in list) times
for j in range(100):

    # initially swapped is false
    swapped = False
    i = 0
    while i < len(lst) - 1:
        # comparing the adjacent elements
        if lst[i] > lst[i + 1]:
            # swapping
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            # Changing the value of swapped
            swapped = True
        i = i + 1
    # if swapped is false then the list is sorted
    # we can stop the loop
    if not swapped:
        break

# print sorted list
print("sorted list is")
print(lst)

# declaring variables for sums of ods and evens and number of odds and evens
sum_odds = 0
sum_even = 0
odds = 0
evens = 0

# calculating sum for ods and number of odd numbers and sum for evens and number of even numbers by iterating through the list
for i in range(100):
    if (lst[i] % 2) == 0:
        sum_even = sum_even + lst[i]
        evens = evens + 1
    else:
        sum_odds = sum_odds + lst[i]
        odds = odds + 1

# printing averages, converting floats to string to avoid conversion errors
print("Average for odds is " + str(sum_odds/odds) + " and average for evens is " + str(sum_even/evens))
