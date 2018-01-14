from laracunha import db

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_description = db.Column(db.String(80))
    full_description = db.Column(db.String(80))
    first_keyword = db.Column(db.String(80))

    def __init__(self, home_description, full_description, first_keyword):
        self.home_description = home_description
        self.full_description = full_description
        self.first_keyword = first_keyword

    def __repr__(self):
        return '<History: {}>'.format(self.home_description)

class Lawyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    oab = db.Column(db.String(80))

    def __init__(self, fullname, email, oab):
        self.fullname = fullname
        self.email = email
        self.oab = oab

    def __repr__(self):
        return '<Lawyer: {}>'.format(self.fullname)

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    url = db.Column(db.String(80))

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return '<Link: {}>'.format(self.name)

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    descriptions = db.relationship('Description', backref='area', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Area: {}>'.format(self.home_description)

class Description(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_description = db.Column(db.String(80))

    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Area: {}>'.format(self.home_description)
