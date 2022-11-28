# import date time for...date functions
from datetime import datetime


# define news class
class News:
    # make class init function with text and city as input
    def __init__(self, city, text):
        self.txt = text
        self.cty = city

    # function to return the output
    def show_news(self):
        output = self.cty + " - " + self.txt
        return output


class Ad:
    # make class init function with text and exp date as input,
    def __init__(self, text, exp_date_a):
        self.txt = text
        self.exp_date = exp_date_a

    # function to return the output
    def show_ad(self):
        output = self.txt + " .Expiration date is " + str(self.exp_date)
        return output


# the 'unique' record here due to a lack of inspiration is the nth fibonacci number ( please mind the hardware when inputting n :)) )
def fibonacci(x):
    if x in {0, 1}:  # Base case
        return x
    # calculate fibonacci
    return fibonacci(x - 1) + fibonacci(x - 2)


def fix_txt(t2):  # capitalization thing from prev module
    # splitting txt2 into sentences for capitalization of first word of each sentence
    ll = t2.split('. ')  # Split the sentences
    # capitalizing each word of every sentence and storing it into variable txt3
    for i, l2 in enumerate(ll):
        ll[i] = l2[0].capitalize() + l2[1:]
    txt3 = (". ".join(ll))
    return txt3


# asking user if he wants to truncate preexistent news. first time running there will be no preexisting news, but no functional impact
k = 0  # mark type variable to check if user gives 'incorrect' response when asked if they want to truncate preexistent newsfeed
while k == 0:
    file_input_type = input("Do you want to truncate current newsfeed output file content? yes/no:")
    if file_input_type == "yes":
        output_file1 = open(r"my_output_file.txt", "w")
        #  just using a file in the same directory as py script. if it doesn't exist, will be created. filename and filepath hardcoded as choice of filename or save path was not in request
        output_file1.write("---------------" + " NEWS FEED FOR " + str(datetime.today()) + "---------------\n")
        output_file1.write("\n")
        k = 1
    elif file_input_type == "no":
        output_file1 = open(r"my_output_file.txt", "a")
        output_file1.write("---------------" + " NEWS FEED FOR " + str(datetime.today()) + "---------------\n")
        output_file1.write("\n")
        k = 1
    else:
        k = 0
# output_file1.close()  # user does not escape while loop until he provides a correct answer which would open the file
# output_file1 = open(r"my_output_file.txt", "r")
# print(output_file1.read())
proc_file = open(r"proc_files.txt", "r")

file_input_type = input("How do you want to input records? m = manual input, txt = text file ")
# making loop marker variable to check if user wants to input additional records, initiated with yes to get user to input at least one record. using while for checking if user want to input new records
if file_input_type == "m":
    loop_marker = "yes"
    while loop_marker == "yes":
        input_type = input("Enter news type - news, ad, or fibonacci:")
        # if user want news input then he input text and city and record is published
        if input_type == "news":
            t = input("enter text:")
            c = input("enter city:")
            dt = str(datetime.now())
            n1 = News(c, t)
            output_file1.write("NEWS:      " + dt + " " + n1.show_news() + "\n")
            output_file1.write("\n")
            loop_marker = input("do you want to input another record: yes/no:")
        # if he wants an  add then he inputs text and date
        elif input_type == "ad":
            t = input("enter text:")
            corr_date = 0
            # try catch for when user inputs incorrect date,  if he enters incorrect date he is prompted to enter correct one. if he enters correct one the ad is recorded. lopping until he inputs correct date :D
            while corr_date == 0:
                try:
                    exp_date_string = input("enter expiration date in correct format (yyyy-mm-dd):")
                    exp_date = datetime.strptime(exp_date_string, "%Y-%m-%d")
                    corr_date = 1
                except ValueError:
                    corr_date = 0
            # editor says below exp_date can be undefined....its defined within try catch block which gets executed when an ad is inputted.
            a1 = Ad(t, exp_date)
            # my understanding here is if expiration date = current date, then ad is expired at current date, hour zero ( so when day began ). if  user looks during day x(today) at an ad that expires tomorrow - day x+1, then that ad expires today ( day x ). so zero days left means ad expires tomorrow at hour 0.
            days_left0 = exp_date - datetime.now()
            days_left = days_left0.days
            if days_left == 0:
                days_left = " Expires today."
            elif days_left < 0:
                days_left = " Already expired."
            output_file1.write("PRIVATE AD:" + a1.show_ad() + " .Days left: " + str(days_left) + "\n")
            output_file1.write("\n")
            loop_marker = input("do you want to input another record: yes/no:")
        elif input_type == "fibonacci":
            n = int(input(
                "enter nth fibonacci number desired ( mind the hardware ):"))  # converting to int so we don't get errors
            nth = fibonacci(n - 1)  # because 0 is the first
            output_file1.write("FIBONACCI: The " + str(n) + " fibonacci number is " + str(nth) + "\n")
            output_file1.write("\n")
            loop_marker = input("do you want to input another record: yes/no:")
        else:
            loop_marker = input("invalid record type - do you want to try again?: yes/no:")

elif file_input_type == 'txt':
    file_path_type = input("Do you want default file path? yes/no:")
    if file_path_type == 'yes':
        input_file_name = input(
            "Please provide file name to be used as input e.g. /'filename.txt( spelling mistakes will result in error ):")
    elif file_path_type == 'no':
        input_file_name = input(
            "Please provide full path of file name to be used as input e.g. /'c:/user/filename.txt( spelling mistakes will result in error ):")
    else:
        print("cannot determine weather to use default path or relative path")
    p_lines = proc_file.readlines()
    k2 = 0
    for pline in p_lines:
        p_file = pline.split()[0]
        if p_file == input_file_name:
            k2 = 1  # means input file has been found in file containing processed filenames
    proc_file.close()
    if k2 == 0:
        input_file1 = open(input_file_name, "r")
        lines = input_file1.readlines()
        for line in lines:
            input_type = line.split()[0].lower()  # getting first word of each line to determine weather record is news, ad or fibonacci
            print(line)
            t0 = line.split()
            if input_type == "news:":
                t = ''
                for index, news_text in enumerate(t0):
                    t0[index] = news_text
                    if index >= 3:
                        t = t + ' ' + line.split()[index]
                t = fix_txt(t)
                c = line.split()[1]
                dt = str(datetime.now())
                n1 = News(c, t)
                output_file1.write("NEWS:      " + dt + " " + n1.show_news() + "\n")
                output_file1.write("\n")
            # if he wants an  add then he inputs text and date
            elif input_type == "ad:":
                t = ''
                for index, news_text in enumerate(t0):
                    t0[index] = news_text
                    if index >= 1:
                        t = t + ' ' + line.split()[index]
                t = fix_txt(t)
                corr_date = 0
                # try catch for when user inputs incorrect date,  if he enters incorrect date he is prompted to enter correct one. if he enters correct one the ad is recorded. lopping until he inputs correct date :D
                while corr_date == 0:
                    try:
                        exp_date_string = line.split()[-1]
                        exp_date = datetime.strptime(exp_date_string, "%Y-%m-%d")
                        corr_date = 1
                    except ValueError:
                        corr_date = 0
                # editor says below exp_date can be undefined....its defined within try catch block which gets executed when an ad is inputted.
                a1 = Ad(t, exp_date)
                # my understanding here is if expiration date = current date, then ad is expired at current date, hour zero ( so when day began ). if  user looks during day x(today) at an ad that expires tomorrow - day x+1, then that ad expires today ( day x ). so zero days left means ad expires tomorrow at hour 0.
                days_left0 = exp_date - datetime.now()
                days_left = days_left0.days
                if days_left == 0:
                    days_left = " Expires today."
                elif days_left < 0:
                    days_left = " Already expired."
                output_file1.write("PRIVATE AD: " + a1.show_ad() + " .Days left: " + str(days_left) + "\n")
                output_file1.write("\n")
            elif input_type == "fibonacci:":
                n = int(line.split()[-1])  # converting to int so we don't get errors
                nth = fibonacci(n - 1)  # because 0 is the first
                output_file1.write("FIBONACCI: The " + str(n) + " fibonacci number is " + str(nth) + "\n")
                output_file1.write("\n")
    elif k == 1:
        print('File ' + input_file_name + ' has already been processed.exiting')
# printing footer of news feed and closing file
output_file1.write("------------" + " END OF NEWS FEED FOR " + str(datetime.today()) + "------------\n")
output_file1.write("\n")
output_file1.close()
output_file1 = open(r"my_output_file.txt", "r")
print(output_file1.read())
output_file1.close()
proc_file = open(r"proc_files.txt", "a")
proc_file.write(input_file_name + '\n')
proc_file.close()
#  please note that  a record stretching on multiple lines will not be processed correctly a split between records needs to be added and processed file deletion needs to be added too. this is being done in the following module, csv parsing
