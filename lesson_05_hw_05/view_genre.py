"""Створити view яка на вхід приймає стиль музики. Має вивести місто
в якому найбільше слухають цей стиль музики. Якшо жанра немає вивести повідомлення.
genre - обов'язковий параметер.
/stats_by_city?genre=HipHop"""

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from lesson_05_hw_05.execute_query import execute_query
from lesson_05_hw_05.format import format_records

app = Flask(__name__)


@app.route("/stats-by-city")
@use_kwargs(
    {
        'genre': fields.Str(
            required=True
        )
    },
    location='query'
)
def city_music(genre):
    query = "SELECT invoices.BillingCity FROM invoices " \
            "JOIN invoice_items ON invoices.InvoiceId=invoice_items.InvoiceId " \
            "JOIN tracks ON invoice_items.TrackId = tracks.TrackId " \
            "JOIN genres ON tracks.GenreId = genres.GenreId " \
           f"WHERE genres.Name='{genre}' GROUP BY invoices.BillingCity " \
            "ORDER BY Sum(invoice_items.Quantity) DESC LIMIT 1"

    records = execute_query(query)
    if len(records) == 0:
        return f'There is no such genre - {genre}'
    else:
        return format_records(records)


app.run(port=5001, debug=True)
