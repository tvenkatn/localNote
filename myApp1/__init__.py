from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime
import json, os

app = Flask(__name__)
app.config.from_pyfile('../application.py')
cors = CORS(app)
db = SQLAlchemy(app)

dbName = "mynoteapp1"

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
        # record['date'] = note.noteTime.strftime("%Y%m%d %Hh %Mm %Ss")
        record['date'] = note.noteTime.strftime("%d/%m/%Y, %H:%M hrs")
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
    return str(newnote.id)
    
@app.route('/deleteNote', methods = ["DELETE"])
def deleteNote():
    Note.query.filter_by(id=int(request.json['id'])).delete()
    db.session.commit()
    return "deleted"

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

