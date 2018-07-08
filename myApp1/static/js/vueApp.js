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
                note: {
                    text: ""
                },
                notes: [
                ]
            }
        },
        methods: {
            addNote() {
                if (/^ *$/.test(this.note)) {
                    console.log("empty string!")
                } else {
                    let { text } = this.note
                    var idd = 1
                    this.postNote(this.note.text)
                    this.notes.push(
                        { id: idd, text, date: new Date(Date.now()).toLocaleString() }
                    )
                    
                }
            },
            
            postNote(arg1) {
                axios.post(`${API_URL}/postNote`, {
                    text: arg1
                })
                    .then(function (response) {
                        console.log("ID of new note is " + response.data);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
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
            }
        },

        created() {
            // https://stackoverflow.com/questions/40996344/axios-cant-set-data
            axios.get(`${API_URL}/getAllNotes`)
                .then((response) => {
                    this.notes = response.data.map(JSON.parse);
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
