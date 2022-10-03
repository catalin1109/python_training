# assigning text to variable
txt = "homEwork:\n" " tHis iz your homeWork, copy these Text to variable.\n"" \n"" You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n"" \n"" it iZ misspeLLing here. fix"'"iZ"'" with correct “is”, but ONLY when it Iz a mistAKE.\n"" \n"" last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

print(" original text is:")
print(txt)

# capitalizing first letter of each paragraph and putting them in variable txt2

res = [i.strip().capitalize() for i in txt.split('\n')]
txt2 = ('\n'.join(res))

# debug, ignore, print('-----------------------txt2 ------------------------')
txt2 = txt2.replace(' iz ', ' is ')
# debug, ignore print(txt2)

# splitting txt2 into sentences for capitalization of first word of each sentence
lines = txt2.split('. ')  # Split the sentences

# capitalizing each word of every sentence and storing it into variable txt3
for index, line in enumerate(lines):
    lines[index] = line[0].upper() + line[1:]
txt3 = (". ".join(lines))

print(' adjusted text is ')
print(txt3)
# variable to store number of whitespace
count = 0
# looping through text and counting blanks
for i in txt3:
    if i.isspace():
        count = count + 1

print("The number of blank spaces is: ", count)
