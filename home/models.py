from laracunha import db, uploaded_images

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_description = db.Column(db.Text)
    complete_description = db.Column(db.Text)
    office_name = db.Column(db.String(256))
    active = db.Column(db.Boolean, default=True)

    def __init__(self, short_description, complete_description):
        self.short_description = short_description
        self.complete_description = complete_description

    def __repr__(self):
        return '<History: {}>'.format(self.short_description)

    def get_short_description(self):
        return self.short_description

    def get_complete_description(self):
        return self.complete_description


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
    image = db.Column(db.String(255))

    descriptions = db.relationship('Description', backref='area', lazy='dynamic')

    @property
    def imgsrc(self):
        return uploaded_images.url(self.image)

    def __init__(self, name, image=None):
        self.name = name
        self.image = image

    def __repr__(self):
        return '<Area: {}>'.format(self.name)


class Description(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_description = db.Column(db.String(80))

    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Area: {}>'.format(self.home_description)
