""" Views for
1. def generate_password()
2. def calculate_average()
"""

import pandas as pd
import random
import csv
from flask import Flask
app = Flask(__name__)


@app.route("/")
def gen_password():
    """ Function to generate password.
    """
    def letters_eq(lst):
        """Function to check for two identical characters next to each other.
        """
        for i in range(len(lst) - 1):
            if lst[i] == lst[i+1]:
                return True

    list_password = '_!*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.choice(list_password) for _ in range(10, 21))
    while (not any(map(str.isdigit, password)) or
           not any(map(str.isupper, password)) or
           not any(map(str.islower, password)) or
           letters_eq(password)):
        password = ''.join(random.choice(list_password) for _ in range(10, 21))
    return f'Password: {password}'


@app.route("/password_easy")
def gen_password_easy():
    """ Function to generate password.
    """
    lst = list('!*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    random.shuffle(lst)
    password = ''.join(random.choice(lst) for _ in range(10, 21))
    return f'Password: {password}'


@app.route("/average")
def calculate_average(path='hw.csv'):
    """ Function to calculate average height and weight.
    """
    with open(path) as f:
        reader = csv.DictReader(f, delimiter=",")
        all_heights = []
        all_weights = []
        for row in reader:
            all_heights.append(float(row[" Height(Inches)"]))
            all_weights.append(float(row[" Weight(Pounds)"]))
        average_high = sum(all_heights) / len(all_heights)
        average_weight = sum(all_weights) / len(all_weights)
    return f'Average high: {average_high} (inches), Average weight : {average_weight} (pounds)'


@app.route("/average_pandas")
def calculate_average_pandas():
    """Function to calculate average height and weight.
    """
    df = pd.read_csv('hw.csv', index_col=0)
    return f'{df.mean(axis=0)}'


app.run(port=5000, debug=True)
