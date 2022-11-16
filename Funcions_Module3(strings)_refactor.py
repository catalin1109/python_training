# assigning text to variable
txt = "homEwork:\n" " tHis iz your homeWork, copy these Text to variable.\n"" \n"" You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.\n"" \n"" it iZ misspeLLing here. fix"'"iZ"'" with correct “is”, but ONLY when it Iz a mistAKE.\n"" \n"" last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

print(" original text is:")
print(txt)


# function for fixing the test, all fixes in one function, 1 input parameter - the text , and returns the fixed text ( for counting whitespaces further on)
def fix_text(a):
    # capitalizing first letter of each paragraph and putting them in variable txt2
    res = [i.strip().capitalize() for i in a.split('\n')]
    txt2 = ('\n '.join(res))

    # debug, ignore, print('-----------------------txt2 ------------------------')
    txt2 = txt2.replace(' iz ', ' is ')
    # debug, ignore print(txt2)

    # splitting txt2 into sentences for capitalization of first word of each sentence
    lines = txt2.split('. ')  # Split the sentences

    # capitalizing each word of every sentence and storing it into variable txt3
    for index, line in enumerate(lines):
        lines[index] = line[0].upper() + line[1:]
    txt3 = (". ".join(lines))
    return txt3


# function to count whitespaces in fixed text, input parameter is the text, returns the count of white spaces
def count_w(a):
    # variable to store number of whitespace
    count = 0
    # looping through text and counting blanks
    for i in a:
        if i.isspace():
            count = count + 1
    return count


print("--------------------FIXED TEXT IS---------------------------------")
print(fix_text(txt))
# for format purposes
print("------------------------------------------------------------------")
print("number of white spaces is "+ str(count_w(fix_text(txt))))

