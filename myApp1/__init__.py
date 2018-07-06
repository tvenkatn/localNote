from flask import Flask, jsonify, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime
import json

app = Flask(__name__)
app.config.from_pyfile('../application.cfg')
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
cors = CORS(app)

db = SQLAlchemy(app)
dbName = "mynoteapp1"

from bin.reference import createDb

class Note(db.Model):
    __tablename__="Note"
    id = db.Column(db.Integer, primary_key=True)
    note =db.Column(db.String(1000))
    noteTime = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, note):
        self.note = note
        
    def __repr__(self):
        return '<Note: %r>' % self.note
###

@app.route('/')
def index():
    dbe = createDb.findDb(dbName)
    if dbe:
        dbex = "{} Exists".format(dbName)
    else:
        dbex = "{} Does not exist".format(dbName)
        createDb.createDbase(dbName)
    return dbex

@app.route('/vueApp')
def vueApp():
    return render_template('index.html')

@app.route('/getAllNotes', methods = ["GET"])
def getAllNotes():
    notes = Note.query.all() # always returns a list

    allNotes = []
    record = {}
    for note in notes:
        record['id'] = note.id
        record['text'] = note.note
        record['date'] = note.noteTime.strftime("%Y%m%d_%Hh%Mm%Ss")
        allNotes.append(json.dumps(record))
    return jsonify(allNotes)
    # return "I have a total of {} notes stored!".format(Note.query.count())

@app.route('/postNote', methods = ["POST"])
def postNote():
    """
    test using this on terminal!

    curl --header "Content-Type: application/json" \
      --request POST \
      --data '{"text":"test note 1","password":"xyz"}' \
      http://localhost:5005/postNote

    """
    
    db.create_all()
    thisNote = request.json['text']
    newnote = Note(thisNote)
    db.session.add(newnote)
    db.session.commit()
    return "Note posted at {1}: {0}".format(newnote.note, newnote.noteTime.strftime("%Y%m%d_%Hh%Mm%Ss"))
    
