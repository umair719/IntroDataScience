import csv


def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:

    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        f_in = open(name, 'r')
        f_out = open("updated1_" + name, 'w')
        reader_in = csv.reader(f_in, delimiter=',')
        writer_out = csv.writer(f_out, delimiter=',')
        for row in reader_in:
            # print row[:3]
            # print row[3:8]
            # print row[8:8 + 5]
            # print row[8 + 5:8 + 5 + 5]
            s = 3
            # a = len(row[3:]) / 5
            a = 8
            for x in xrange(0, len(row[3:]) / 5):
                e = a + x * 5
                print "{}-{}".format(s, e)
                if len(row[s:e]):
                    r = row[:3] + row[s:e]
                    writer_out.writerow(r)
                    print r
                else:
                    # m = 5 - len(row[s:e])
                    # r = row[:3] + row[s:e] + [1] * m
                    print "row missing data"
                    #writer_out.writerow(r)
                s = e
        f_in.close()
        f_out.close()  # your code here

fix_turnstile_data(['turnstile-110528.csv'])

'''
Quiz: 5 - Fixing Turnstile Data
For this exercise we recommend that you use the Python csv reader/writer module, 
rather than pandas. Check out the Python documentation examples with csv reader, 
writer (only the first three examples are applicable to our problem) :

http://docs.python.org/2/library/csv.html#examples

Note that one single row in the input file will generate multiple different rows in the output file. 
For example, this one line from an input file:

A002,R051,02-00-00,05-21-11,00:00:00,REGULAR,003169391,001097585,05-21-11,04:00:00,REGULAR,003169415,
001097588,05-21-11,08:00:00,REGULAR,003169431,001097607,05-21-11,12:00:00,REGULAR,003169506,001097686,
05-21-11,16:00:00,REGULAR,003169693,001097734,05-21-11,20:00:00,REGULAR,003169998,001097769,05-22-11,
00:00:00,REGULAR,003170119,001097792,05-22-11,04:00:00,REGULAR,003170146,001097801

will produce the following lines in the output file:
A002,R051,02-00-00,05-21-11,00:00:00,REGULAR,003169391,001097585
A002,R051,02-00-00,05-21-11,04:00:00,REGULAR,003169415,001097588
A002,R051,02-00-00,05-21-11,08:00:00,REGULAR,003169431,001097607
A002,R051,02-00-00,05-21-11,12:00:00,REGULAR,003169506,001097686
A002,R051,02-00-00,05-21-11,16:00:00,REGULAR,003169693,001097734
A002,R051,02-00-00,05-21-11,20:00:00,REGULAR,003169998,001097769
A002,R051,02-00-00,05-22-11,00:00:00,REGULAR,003170119,001097792
A002,R051,02-00-00,05-22-11,04:00:00,REGULAR,003170146,001097801
In other words, one line in the input contains multiple records, and we want to separate them into different lines. 
The first three elements in the input line (A002,R051,02-00-00) are repeated for each of the 8 lines in 
the output file.
'''
