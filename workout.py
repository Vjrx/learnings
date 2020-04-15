from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
import itertools
import re
import csv
import os
import random
import sqlite3
import logging



def collection_examples():
    #namedtuple
    k = namedtuple('student', ['name','age','course'])
    s = k('vijay', 25, 'mech')
    print(s.name)

    #deque
    name = 'vijayanand'
    deque_name = deque(name)
    deque_name.appendleft('Mr ')
    print(deque_name)

    #Chainmap
    a = {1:'vijay', 2:'anand'}
    b = {3:"vahi",4:"sathya"}
    k = ChainMap(a,b)
    print(k)
    for items in k:
        print(items)

    #Counter
    li = [1,2,3,2,3,4,3,4,5,3]
    c = Counter(li)
    print(list(c.elements()))
    print(c.most_common(2))

    # defaultdict
    k = 'vijayanand jagadeesan'
    ss = defaultdict(int)
    for letter in k:
        ss[letter] +=1

    print(ss)

    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    k = defaultdict(int)
    for i,j in s:
        k[i] += j
    print(k)


def iter_tools():
    k = itertools.combinations([1,2,3,4], 2)
    print(list(k))
    k = itertools.permutations([1,2,3,4], 2)
    print(list(k))
    k = itertools.accumulate([1,2,3,4])
    print(list(k))
    #k = itertools.accumulate([1, 2, 3, 4], func=operator.mul)
    #print(list(k))
    a = [1,2,3,4,5]
    b=[True, True, False, False, False]
    k = itertools.compress(a,b)
    print(list(k))
    k = itertools.chain.from_iterable([[1,2],[3,4,5]])
    print(list(k))


def regex():
    stri = 'weriughq;oernaf;vijay@gmail.com jhbsdfi ijsb999-555-0986fivasvnbatcatmatfat'
    pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+'
    pattern = '\d{3}-\d{3}-\d{4}'
    pattern = '[^b]at'
    result = re.findall(pattern, stri)
    print(result)


def map_lambda():
    a = ['sachin', 'vijay', 'sathya', 'divya', 'vahi']
    k = map(lambda x: x+'is a stupid' if x[0] !='s' else x, a)
    print(list(k))

    k = filter(lambda x: x[0]!='s', a)
    print(list(k))

    a = dir('k')
    k = [x for x in a if not x.startswith('_')]
    print(k)

    k = filter(lambda x: x[0]!='_', a)
    print(list(k))


def list_comp():
    li = [1,2,3,4,5,6,7,8,9]
    k = [x for x in li]
    print(k)

    k = [x for x in li if x%2==0]
    print(k)

    k = [x+10 if x%2==0 else x for x in li]
    print(k)

    k = [(x,y) for x in 'abcd' for y in range(5)]
    print(k)


#Generator
def square_no(num):
    for i in num:
        yield i*i

    for i in num:
        yield i*i*i


def xls_read_write():
    pass


def decorator_function(original_function):
    def wrapper_fun(*args, **kwargs):
        print("Executed before ", original_function.__name__)
        result = original_function(*args, **kwargs)
        return result
    return wrapper_fun


class DecoratorClass:
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        result = self.original_func(*args, **kwargs)
        return result


def csv_operation():
    # Reading a csv file
    with open('file.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        with open('write.csv', 'w') as wf:
            writer = csv.writer(wf)

            for line in reader:
                writer.writerow(line)


def sorting():
    k = [2,3,1,9,5,3,8,5]
    s = sorted(k)
    print(s)

    l = [('vijay', 25), ("Anand", 27), ("sathya", 32), ("vahini", 45)]
    k = sorted(l, key=lambda x: x[1], reverse=True)
    print(k)


def os_operations():
    print(os.getcwd())
    os.chdir('//Users//vijayanand')
    os.rename('workout.py', 'workouts.py')
    os.stat('//Users//vijayanand//PycharmProjects//learnings//task.py')
    os.environ.get('HOME')
    if os.path.exists("//Users//vijayanand//PycharmProjects//learnings"):
        pass
    os.path.join(os.environ.get("HOME"), 'test.txt')
    os.path.basename("/tmp/get/test.txt")
    os.path.isdir()
    os.path.isfile()


def random_operation():
    k = random.random()
    print(k)    # prints value from (0 to 1)
    k = random.uniform(1, 10)
    print(k)    # prints a float value within the specified range
    k = random.randint(1,6)
    print(k)     # prints a int between 1 and 6(6 also included)
    k = random.choice(['red', 'blue', 'green', 'black'])
    print(k)
    colour = ['red', 'blue', 'green']
    k = random.choices(colour, weights=[18, 18, 2], k=38)
    print(k)
    random.shuffle(list)   #  Shuffles the list
    #Inorder to get a ungique elements from a list.. dont use choices...use sample
    random.sample(colour, k=3)


def sqlite_operation():
    conn = sqlite3.connect("meta.db")  #or conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE employee (
                first text,
                last  text,
                pay   integer
                )""")
    cursor.execute(""" SELECT * FROM employee""")
    cursor.fetchone()  # returns one row in db
    cursor.fetchall()   # fetches all rows in table
    # For adding values to db from a class
    emp = DecoratorClass()
    cursor.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp.first, emp.last, emp.pay))
    conn.commit()
    conn.close()


def logging_operation():
    #DEBUG INFO  WARNING  ERROR  CRITICAL   default is warning...
    logging.basicConfig(filename='file.log', level=logging.DEBUG, format='')


def virtual_env():
    # python3 - m  venv tutorial - env
    # tutorial-env\Scripts\activate.bat   ----> on windows
    # source tutorial-env/bin/activate    -------> Linux/mac
    # For leaving venv   deactivate   or source deactivate
    pass


def set_operations():
    engineers = {'John', 'Jane', 'Jack', 'Janice'}
    programmers = {'Jack', 'Sam', 'Susan', 'Janice'}
    managers = {'Jane', 'Jack', 'Susan', 'Zack'}

    print(engineers.difference(programmers))
    print(engineers.intersection(programmers))
    print(programmers.union(managers))

if __name__ == '__main__':
    #iter_tools()
    #k = square_no([1,2,3,4,5])
    #or i in k:
    #    print(i)
    #list_comp()
    #map_lambda()
    #regex()
    #csv_operation()
    #sorting()
    #random_operation()
    #sqlite_operation()
    #logging_operation()
    #virtual_env()
    #set_operations()
    pass