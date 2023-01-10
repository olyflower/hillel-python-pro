"""Implement the following view functions.
"""

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs

from lesson_04_hw_04.execute_query import execute_query
from lesson_04_hw_04.format import format_records

app = Flask(__name__)


@app.route("/order-price")
@use_kwargs(
    {
        'country': fields.Str(
            load_default=None)
    },
    location='query'
)
def order_price(country):
    """ Function calculate sales by country on page / if no country show all sales by all counties.
    """
    if country:
        query = "SELECT SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Sales, invoices.BillingCountry" \
            " FROM invoice_items JOIN invoices ON  invoice_items.InvoiceId==invoices.InvoiceId " \
            f"GROUP BY invoices.BillingCountry HAVING invoices.BillingCountry=='{country}'"
    else:
        query = "SELECT SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Sales, invoices.BillingCountry" \
            " FROM invoice_items JOIN invoices ON  invoice_items.InvoiceId==invoices.InvoiceId " \
            "GROUP BY invoices.BillingCountry"

    records = execute_query(query)
    return format_records(records)


@app.route("/track-info")
@use_kwargs(
    {
        'id': fields.Int(
            required=True
        )
    },
    location='query'
)
def get_all_info_about_track(id):
    """Function gives information about track.
    """
    query = "SELECT tracks.TrackId, tracks.Name, tracks.Composer, albums.Title," \
            " artists.Name, genres.Name, media_types.Name" \
            " FROM tracks JOIN albums ON tracks.AlbumId = albums.AlbumId" \
            " JOIN artists ON albums.ArtistId = artists.ArtistId" \
            " JOIN genres ON tracks.GenreId = genres.GenreId" \
            " JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId" \
            f" GROUP BY tracks.TrackId HAVING tracks.TrackId=='{id}'"
    records = execute_query(query)
    if len(records) == 0:
        return f'Track {id} is not exist!'
    else:
        return records


@app.route("/track-time")
def get_all_info_about_track_time():
    """Function calculate all track time in albums.
    """
    query = "SELECT albums.Title, (SUM(tracks.Milliseconds) / 1000.0 / 3600.0)" \
            " FROM tracks JOIN albums ON tracks .AlbumId = albums.AlbumId" \
            " GROUP BY albums.Title"

    records = execute_query(query)
    return format_records(records)


app.run(port=5000, debug=True)
