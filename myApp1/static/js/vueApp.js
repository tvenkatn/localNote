const API_URL = 'http://192.168.1.8:5005'
// const API_URL = 'http://localhost:5005'


var app = new Vue(
    {
        el: "#app",
        delimiters: ["[[","]]"],
        data: function () {
            return {
                title: "local Note",
                isLoading: false,
                remainingCount: 1000,
                maxCount: 1000,
                newIdForNote: 1,
                latestIdForNote: 0,
                note: {
                    text: ""
                },
                notes: [
                ]
            }
        },
        methods: {
            addNote() {
                if (/^ *$/.test(this.note.text) || this.note.text.trim() == "") {
                    console.log("empty string!")
                } else {
                    let { text } = this.note
                    this.postNote(this.note.text)
                    this.notes.push(
                        { id: this.newIdForNote, text, date: new Date(Date.now()).toLocaleString() }
                    )
                
                    this.note.text = "";
                    // this.updateLatestNote(this.latestIdForNote);
                    
                }
            },
            
            postNote(arg1) {
                // var that = this.latestIdForNote;
                axios.post(`${API_URL}/postNote`, {
                    text: arg1
                })
                    .then(function (response) {
                        console.log("ID of new note is " + response.data);
                        that = parseInt(response.data);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
                // console.log("that is " + that);
                // this.latestIdForNote = that;
            },

            removeNote(note) {
                // console.log(note.id);
                this.notes.pop(note); // delete from UI
                axios.delete(`${API_URL}/deleteNote`, { data: { id: note.id } })
                    .then((response) => {
                        // console.log(response)
                    }, (error) => {
                        // error callback
                    });
            },
            
            countdown() {
                this.remainingCount = this.maxCount - this.note.text.length;
                this.hasError = this.remainingCount < 0;
            },

            updateLatestNote(thisid) {
                // not working as axios is async and it is executing last, even after this function!
                var tnote = this.notes
                var nid = this.newIdForNote
                console.log("updating notes id with " + thisid);
                for (var i in tnote) {
                    console.log("in for loop!" + tnote[i].id);
                    if (tnote[i].id == nid) {
                        console.log("Found the note. Text is " + tnote[i].text);
                        tnote[i].id = thisid;
                        break; //Stop this loop, we found it!
                    }
                }
                this.notes = tnote;
                // this.notes.filter(ob => ob.id == this.newIdForNote)[0].id = thisid
            }
        },

        created() {
            // https://stackoverflow.com/questions/40996344/axios-cant-set-data
            axios.get(`${API_URL}/getAllNotes`)
                .then((response) => {
                    this.notes = response.data.map(JSON.parse);
                    this.notes.sort(function (a, b) {
                        return a.id - b.id;
                    })
                }).catch(function (error) {
                    // handle error
                    console.log(error);
                })
                .then(function () {
                    // always executed
                });
        }
    }
) 
