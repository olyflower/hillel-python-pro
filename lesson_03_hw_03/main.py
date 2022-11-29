""" Views for
1. def generate_students():
2. def get_bitcoin_value():
"""

import csv

import pandas
import pandas as pd
import requests

from faker import Faker
from flask import Flask, request
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

app = Flask(__name__)

faker_instance = Faker()


@app.route("/students")
@use_kwargs(
    {
        'count': fields.Int(
            missing=5,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location='query'
)
def generate_students(count):
    """Function generates student first name, last name, email, password, date of birth.
    """
    count = request.args.get('count', default='10')
    count = int(count)
    with open('students.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['First_name', 'Last_name', 'Email', 'Password', 'Date_of_Birth'])
        for _ in range(count):
            writer.writerow([faker_instance.first_name(), faker_instance.last_name(), faker_instance.email(),
                             faker_instance.password(), faker_instance.date_of_birth()])
    return str(pandas.read_csv('students.csv'))


@app.route("/bitcoin_rate")
def get_bitcoin_value():
    """Function get value currency of bitcoin, symbol of input currency code and quantity of bitcoins.
    """
    bitcoin_value = 0
    symbol_currency_code = 0
    currency = request.args.get('currency', default='USD')
    count = request.args.get('count', default=1)
    count = int(count)
    for i in requests.get('https://bitpay.com/api/rates').json():
        if i['code'] == currency:
            bitcoin_value = i['rate']
    for j in requests.get('https://bitpay.com/currencies').json()['data']:
        if j['code'] == currency:
            symbol_currency_code = j['symbol']
    bitcoins = int(count / bitcoin_value)
    return f'Bitcoin value: {bitcoin_value}, Symbol of input currency code: {symbol_currency_code},' \
           f' Quantity of bitcoins: {bitcoins}'


app.run(port=5000, debug=True)
