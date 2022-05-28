import csv
from scrape import *
from amazon import *
from flask import render_template
from flask import Flask
# You need to use following line [app Flask(__name__]
#app = Flask(__name__)


# @app.route('/')
def details(val, writer):

    result = page(val[4])
    count = 0
    start = 0
    string1 = 'a'
    string1 = []
    # print(result['images'][1])
    for i in range(len(result['images'])):
        if result['images'][i] == '{':
            i = i+2
            start = 1
            print('a')
        if start == 1:
            string1.append(result['images'][i])
            print('b')
        if result['images'][i] == 'j':
            if result['images'][i+1] == 'p':
                if result['images'][i+2] == 'g':
                    string1.append(result['images'][i+1])
                    string1.append(result['images'][i+2])
                    print('c')
                    break

    # print(result)
    string1.pop(0)
    string1.pop(0)

    str1 = ''.join(string1)
    print(string1)
    print(str1)
    list1 = []
    list1.append(str(list([val[0]]))[2:-2])
    list1.append(str(list([val[1]]))[2:-2])
    list1.append(str(list([val[2]]))[2:-2])
    list1.append(str(list([val[3]]))[2:-2])
    list1.append(str(list([val[4]]))[2:-2])
    list1.append((str1))
    # val.append(str1)
    writer.writerows([list1])

    #to_send = [list1]
    # return render_template("searchpage.html", to_send=to_send)


def product_search(to_search):
    f = open('file1.csv', "w", newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(['Description', 'Price', 'Rating',
                     'Review Count', 'Product URL', 'Product Image'])
    val = list(work(to_search))
    for i in range(6):  # len(val)):
        details(val[i], writer)

    #result = page(val[0][4])

    # print(string2)
    f.close()


product_search('water')
