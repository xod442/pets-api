from mongoengine import signals

from application import db

class Store(db.Document):
    external_id = db.StringField(db_field="ei")
    neighborhood = db.StringField(db_field="n")
    name = db.StringField(db_field="na")
    street_address = db.StringField(db_field="sa")
    city = db.StringField(db_field="c")
    state = db.StringField(db_field="st")
    zip = db.StringField(db_field="z")
    phone = db.StringField(db_field="p")
    store_id = db.StringField(db_field="si")
    live = db.BooleanField(db_field="l", default=True)

    meta = {
        'indexes': [('external_id', 'live')]
    }
