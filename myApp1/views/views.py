from app import db

# class Bmi(db.Model):
#     __tablename__="bmi"
#     id=db.Column(db.Integer, primary_key=True)
#     name_=db.Column(db.String(120), unique=True)
#     weight_=db.Column(db.Numeric)
#     height_=db.Column(db.Numeric)
#     queryTime = db.Column(db.DateTime, default=datetime.datetime.now)

#     def __init__(self, name_, weight_, height_):
#         self.name_=name_
#         self.weight_=weight_
#         self.height_=height_


class Note(db.Model):
    __tablename__ = "Note"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.BLOB)
    noteTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, note):
        self.note = note
 
    def __repr__(self):
        return '<Note: %r>' % self.note
