from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated

from py4web_weasy import WeasyTemplate

import datetime



@action("invoice")
@action.uses(WeasyTemplate("invoice.html"))
def invoice():
    return dict(
        address_from=dict(
            company="Mars Postal Services Inc",
            street="Red Street",
            zip="x1y2z3",
            city="Mars Colony 1",
            planet="Mars",
        ),
        address_to=dict(
            company="We sell things everywhere",
            street="Online Shopping street",
            zip="12345",
            city="New York",
            planet="Earth",
        ),
        invoice_no="123456",
        date=datetime.datetime(2060, 5, 4, 0, 1, 2).strftime("%b %d, %Y"),
        products=[
            dict(description="Big package handling", price=600.4, qty=12),
            dict(description="3d printed meals", price=10.0, qty=100),
            dict(description="Old fashioned mails", price=1.0, qty=20000),
        ],
    )
