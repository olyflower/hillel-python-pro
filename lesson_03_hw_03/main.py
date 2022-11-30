""" Views for
1. def generate_students():
2. def get_bitcoin_value():
"""

import csv
import requests

from faker import Faker
from flask import Flask
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

app = Flask(__name__)

faker_instance = Faker()


@app.route("/students")
@use_kwargs(
    {
        'count': fields.Int(
            missing=10,
            validate=[validate.Range(min=1, max=1000)]
        )
    },
    location='query'
)
def generate_students(count):
    """Function generates student first name, last name, email, password, date of birth.
    """
    with open('students.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['First_name', 'Last_name', 'Email', 'Password', 'Date_of_Birth'])
        for _ in range(count):
            writer.writerow([faker_instance.first_name(), faker_instance.last_name(), faker_instance.email(),
                             faker_instance.password(), faker_instance.date_of_birth()])
    with open('students.csv', 'r') as file:
        return file.read().replace('\n\n', '<br>')


@app.route("/bitcoin-rate")
@use_kwargs(
    {
        'count': fields.Int(
            missing=1
        ),
        'currency': fields.Str(
            load_default='USD'
        )
    },
    location='query'
)
def get_bitcoin_value(count, currency):
    """Function get value currency of bitcoin, symbol of input currency code and quantity of bitcoins.
    """
    symbol_currency_code = 0
    bitcoin_value = requests.get('https://bitpay.com/api/rates/' + currency).json()['rate']
    for i in requests.get('https://bitpay.com/currencies').json()['data']:
        if i['code'] == currency:
            symbol_currency_code = i['symbol']
    bitcoins = int(count / bitcoin_value)
    return f'Bitcoin value: {bitcoin_value}, Symbol of input currency code: {symbol_currency_code},' \
           f' Quantity of bitcoins: {bitcoins}'


app.run(port=5000, debug=True)
