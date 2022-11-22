""" Views for
1. def generate_password()
2. def calculate_average()
"""

import random
from statistics import mean
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


@app.route("/average")
def calculate_average(path='hw.csv'):
    """ Function to calculate average height and weight.
    """
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        average_high = mean([float(row[' Height(Inches)']) for row in reader])
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        average_weight = mean([float(row[' Weight(Pounds)']) for row in reader])
    return f'Average high: {average_high} (inches), Average weight : {average_weight} (pounds)'


app.run(port=5000, debug=True)
